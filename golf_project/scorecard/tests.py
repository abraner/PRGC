from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from django.utils import timezone

from scorecard.models import Cost, GolfRound, Hole, HoleScore, MensLeagueRoundScore, Player, WomensLeagueRoundScore
from scorecard.views import (
    _member_last_name_key,
    adjust_9_team_chicago_quota_for_player,
    adjust_18_chicago_quota_for_player,
    adjust_ladies_handicap_for_player,
    adjust_mens_handicap_for_player,
    chicago_quota_step,
    compute_round_skins,
    mens_league_handicap_from_scores,
    womens_league_handicap_from_scores,
)


class CostAmountTests(TestCase):
    def test_each_game_reads_its_own_cost_and_the_shared_course_amount(self):
        row = Cost.objects.first()
        row.mens_league_18 = Decimal('15.00')
        row.gross_net_18 = Decimal('7.50')
        row.scramble_9 = Decimal('8.00')
        row.team_chicago_9 = Decimal('9.00')
        row.womens_league_9 = Decimal('5.00')
        row.chicago_18 = Decimal('11.00')
        row.golf_course_amount = Decimal('3.25')
        row.save()

        expectations = {
            '18_HOLE_MENS_LEAGUE': Decimal('15.00'),
            '18_gross_net': Decimal('7.50'),
            '9_hole_scramble': Decimal('8.00'),
            'team_chicago_points_9': Decimal('9.00'),
            '9_WOMENS_LEAGUE': Decimal('5.00'),
            'chicago_points_18': Decimal('11.00'),
        }
        for fmt, game_cost in expectations.items():
            cost, course = Cost.amounts_for_format(fmt)
            self.assertEqual(cost, game_cost)
            self.assertEqual(course, Decimal('3.25'))

    def test_leaderboard_pot_uses_the_cost_row(self):
        User.objects.create_user('keeper', password='pw')
        self.client.login(username='keeper', password='pw')
        row = Cost.objects.first()
        row.gross_net_18 = Decimal('8.00')
        row.golf_course_amount = Decimal('1.00')
        row.save()

        player = Player.objects.create(name='Ada')
        active_round = GolfRound.objects.create(game_format='18_GROSS_NET', is_active=True)
        hole = Hole.objects.create(hole_number=1, par=4)
        HoleScore.objects.create(round=active_round, player=player, hole=hole, gross_value=4)

        response = self.client.get('/leaderboard/')
        self.assertEqual(response.context['entry_fee_display'], '8.00')
        self.assertEqual(response.context['course_cut_display'], '1.00')
        self.assertEqual(response.context['total_pot'], '8')
        self.assertEqual(response.context['course_money'], '1')
        self.assertContains(response, 'Course Cut ($1.00)')

    def test_individual_chicago_pool_is_entry_minus_course_and_pays_out(self):
        User.objects.create_user('keeper', password='pw')
        self.client.login(username='keeper', password='pw')
        row = Cost.objects.first()
        row.chicago_18 = Decimal('12.00')
        row.golf_course_amount = Decimal('2.00')
        row.save()

        players = [
            Player.objects.create(name=name, chicago_points_18=36)
            for name in ('Ada', 'Bea', 'Cia', 'Dee')
        ]
        active_round = GolfRound.objects.create(game_format='18_IND_CHICAGO', is_active=True)
        hole = Hole.objects.create(hole_number=1, par=4)
        for player, strokes in zip(players, (2, 3, 4, 5)):
            HoleScore.objects.create(round=active_round, player=player, hole=hole, gross_value=strokes)

        response = self.client.get('/leaderboard/?format=18_ind_chicago')
        self.assertEqual(response.context['total_pot'], '48')
        self.assertEqual(response.context['course_money'], '8')
        self.assertEqual(response.context['net_pool'], '40')
        self.assertEqual(response.context['skins_pool'], '0')
        self.assertEqual(response.context['closest_pin_pool'], '0')
        payouts = sorted((row['payout'] for row in response.context['net_leaderboard']), reverse=True)
        self.assertEqual(payouts, [20, 12, 8, 0])


class ChicagoQuotaStepTests(TestCase):
    def test_step_drops_a_remainder_of_one(self):
        expected = {
            0: 0, 1: 0, -1: 0,
            2: 1, 3: 1, -2: -1, -3: -1,
            4: 2, 5: 2, -4: -2, -5: -2,
            6: 3, 7: 3, -6: -2, -7: -2,
            8: 4, 9: 4, -8: -2, -9: -2,
            10: 5, 11: 5, -10: -2, -11: -2,
            12: 6, 13: 6, -12: -2, -13: -2,
        }
        for differential, step in expected.items():
            self.assertEqual(chicago_quota_step(differential), step, differential)

    def test_eighteen_hole_quota_moves_by_that_step(self):
        player = Player.objects.create(name='Fay', chicago_points_18=10)
        active = GolfRound.objects.create(game_format='18_IND_CHICAGO', is_active=True)
        # Five bogeys are 1 point each. Differential 5 − 10 = −5 → step −2 → quota 8.
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 6)]
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        old_quota, new_quota, differential = adjust_18_chicago_quota_for_player(
            player, HoleScore.objects.filter(round=active, player=player)
        )
        player.refresh_from_db()
        self.assertEqual((old_quota, differential, new_quota), (10, -5, 8))
        self.assertEqual(player.chicago_points_18, 8)

    def test_nine_hole_team_quota_moves_by_that_step(self):
        player = Player.objects.create(name='Gia', team_chicago_points_9=8)
        active = GolfRound.objects.create(game_format='9_TEAM_CHICAGO', is_active=True)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 5)]
        # Four birdies are 4 points each = 16. Differential 16 − 8 = +8 → step +4 → quota 12.
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=3)

        old_quota, new_quota, differential = adjust_9_team_chicago_quota_for_player(
            player, HoleScore.objects.filter(round=active, player=player)
        )
        player.refresh_from_db()
        self.assertEqual((old_quota, differential, new_quota), (8, 8, 12))
        self.assertEqual(player.team_chicago_points_9, 12)


class MensLeagueHandicapTests(TestCase):
    def test_formula_is_eighty_percent_of_average_minus_60(self):
        self.assertEqual(mens_league_handicap_from_scores([90]), 24)
        self.assertEqual(mens_league_handicap_from_scores([85, 88, 90, 82, 95]), 22)
        self.assertEqual(mens_league_handicap_from_scores([55]), 0)

    def test_full_card_uses_only_the_last_five_grosses(self):
        player = Player.objects.create(name='Alan', handicap=10)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 19)]
        for days_ago, gross in ((6, 100), (5, 100), (4, 80), (3, 80), (2, 80), (1, 80)):
            past = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=False)
            MensLeagueRoundScore.objects.create(
                player=player,
                golf_round=past,
                gross_score=gross,
                played_on=timezone.now() - timezone.timedelta(days=days_ago),
            )

        active = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=True)
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        old_hcp, new_hcp, total_gross = adjust_mens_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        player.refresh_from_db()
        # Today is 90. Last five are 90, 80, 80, 80, 80. The 100s fall off.
        self.assertEqual(total_gross, 90)
        self.assertEqual(old_hcp, 10)
        self.assertEqual(new_hcp, 18)
        self.assertEqual(player.handicap, 18)
        self.assertEqual(player.mens_league_scores.count(), 7)

        adjust_mens_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        self.assertEqual(player.mens_league_scores.count(), 7)

    def test_partial_card_does_not_change_handicap(self):
        player = Player.objects.create(name='Ben', handicap=12)
        active = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=True)
        hole = Hole.objects.create(hole_number=1, par=4)
        HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        result = adjust_mens_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        player.refresh_from_db()
        self.assertIsNone(result)
        self.assertEqual(player.handicap, 12)
        self.assertEqual(MensLeagueRoundScore.objects.count(), 0)

    def test_gross_net_round_shares_mens_league_history(self):
        player = Player.objects.create(name='Cal', handicap=4)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 19)]
        past = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=False)
        MensLeagueRoundScore.objects.create(
            player=player,
            golf_round=past,
            gross_score=80,
            played_on=timezone.now() - timezone.timedelta(days=7),
        )
        active = GolfRound.objects.create(game_format='18_GROSS_NET', is_active=True)
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        old_hcp, new_hcp, total_gross = adjust_mens_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        player.refresh_from_db()
        # Prior men's 80 and today's gross/net 90 average 85. (85 − 60) × 0.8 = 20.
        self.assertEqual((old_hcp, new_hcp, total_gross), (4, 20, 90))
        self.assertEqual(player.handicap, 20)
        self.assertEqual(player.mens_league_scores.count(), 2)

    def test_mens_league_update_caps_at_20(self):
        player = Player.objects.create(name='Dan', handicap=4)
        holes = [Hole.objects.create(hole_number=n, par=4, handicap_index=n) for n in range(1, 19)]
        active = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=True)
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        _, new_hcp, total_gross = adjust_mens_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        player.refresh_from_db()
        # 90 gross would be 24 before the men's league cap.
        self.assertEqual(total_gross, 90)
        self.assertEqual(new_hcp, 20)
        self.assertEqual(player.handicap, 20)

    def test_gross_net_update_is_not_capped_at_20(self):
        player = Player.objects.create(name='Eli', handicap=4)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 19)]
        active = GolfRound.objects.create(game_format='18_GROSS_NET', is_active=True)
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        _, new_hcp, _total = adjust_mens_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        self.assertEqual(new_hcp, 24)

    def test_mens_league_leaderboard_and_skins_use_20(self):
        User.objects.create_user('keeper', password='pw')
        self.client.login(username='keeper', password='pw')
        high = Player.objects.create(name='High', handicap=30)
        even = Player.objects.create(name='Even', handicap=0)
        hole = Hole.objects.create(hole_number=1, par=4, handicap_index=10)
        active = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=True)
        HoleScore.objects.create(round=active, player=high, hole=hole, gross_value=5)
        HoleScore.objects.create(round=active, player=even, hole=hole, gross_value=4)

        response = self.client.get('/leaderboard/')
        rows = {row['player'].name: row for row in response.context['net_leaderboard']}
        self.assertEqual(rows['High']['playing_handicap'], 20)
        self.assertEqual(rows['High']['net_score'], 5 - 20)

        # Uncapped, a 30 handicap gets 2 strokes on index 10 (net 3) and wins.
        # Capped at 20, that hole gets 1 stroke (net 4), which ties and voids the skin.
        self.assertEqual(compute_round_skins(active, use_net=True, max_handicap=20), [])


class WomensLeagueHandicapTests(TestCase):
    def test_formula_is_eighty_percent_of_average_minus_30(self):
        self.assertEqual(womens_league_handicap_from_scores([45]), 12)
        self.assertEqual(womens_league_handicap_from_scores([43, 44, 45, 46, 47]), 12)
        self.assertEqual(womens_league_handicap_from_scores([28]), 0)

    def test_full_nine_uses_only_the_last_five_grosses(self):
        player = Player.objects.create(name='Ada', ladies_league_handicap=8)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 10)]
        for days_ago, gross in ((6, 55), (5, 55), (4, 40), (3, 40), (2, 40), (1, 40)):
            past = GolfRound.objects.create(game_format='9_WOMENS_LEAGUE', is_active=False)
            WomensLeagueRoundScore.objects.create(
                player=player,
                golf_round=past,
                gross_score=gross,
                played_on=timezone.now() - timezone.timedelta(days=days_ago),
            )

        active = GolfRound.objects.create(game_format='9_WOMENS_LEAGUE', is_active=True)
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        old_hcp, new_hcp, total_gross = adjust_ladies_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        player.refresh_from_db()
        # Today is 45. Last five are 45, 40, 40, 40, 40. The 55s fall off.
        self.assertEqual(total_gross, 45)
        self.assertEqual(old_hcp, 8)
        self.assertEqual(new_hcp, 9)
        self.assertEqual(player.ladies_league_handicap, 9)
        self.assertEqual(player.womens_league_scores.count(), 7)

        adjust_ladies_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        self.assertEqual(player.womens_league_scores.count(), 7)

    def test_partial_card_does_not_change_handicap(self):
        player = Player.objects.create(name='Bea', ladies_league_handicap=6)
        active = GolfRound.objects.create(game_format='9_WOMENS_LEAGUE', is_active=True)
        hole = Hole.objects.create(hole_number=1, par=4)
        HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        result = adjust_ladies_handicap_for_player(
            player, HoleScore.objects.filter(round=active, player=player), active
        )
        player.refresh_from_db()
        self.assertIsNone(result)
        self.assertEqual(player.ladies_league_handicap, 6)
        self.assertEqual(WomensLeagueRoundScore.objects.count(), 0)


class MemberListOrderTests(TestCase):
    def test_members_sort_by_last_name(self):
        players = [
            Player.objects.create(name='Zoe Adams'),
            Player.objects.create(name='Ann'),
            Player.objects.create(name='Bob Smith'),
            Player.objects.create(name='Cara Smith'),
        ]
        ordered = [player.name for player in sorted(players, key=_member_last_name_key)]
        self.assertEqual(ordered, ['Zoe Adams', 'Ann', 'Bob Smith', 'Cara Smith'])
