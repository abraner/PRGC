import json
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from django.utils import timezone

from scorecard.forms import designated_scorekeeper_label, player_squad_choice_label
from scorecard.models import Cost, GolfRound, Hole, HoleScore, MensLeagueRoundScore, Player, Squad, WomensLeagueRoundScore
from scorecard.views import (
    _member_last_name_key,
    adjust_9_team_chicago_quota_for_player,
    adjust_18_chicago_quota_for_player,
    adjust_ladies_handicap_for_player,
    adjust_mens_handicap_for_player,
    apply_mens_handicap_updates,
    apply_womens_handicap_updates,
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

    def test_direct_points_are_not_converted_from_strokes(self):
        player = Player.objects.create(name='Hope', team_chicago_points_9=0)
        active = GolfRound.objects.create(game_format='9_TEAM_CHICAGO', is_active=True)
        # 4 on a par 3 would be a bogey (1 point) if this were still strokes.
        hole = Hole.objects.create(hole_number=1, par=3)
        HoleScore.objects.create(
            round=active, player=player, hole=hole, gross_value=4, net_value=1
        )

        old_quota, new_quota, differential = adjust_9_team_chicago_quota_for_player(
            player, HoleScore.objects.filter(round=active, player=player)
        )
        self.assertEqual((old_quota, differential, new_quota), (0, 4, 2))

    def test_zero_points_still_count_as_a_played_hole(self):
        User.objects.create_user('keeper', password='pw')
        self.client.login(username='keeper', password='pw')
        player = Player.objects.create(name='Ivy', chicago_points_18=10)
        active = GolfRound.objects.create(game_format='18_IND_CHICAGO', is_active=True)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 4)]
        for hole, points in zip(holes, (8, 0, 2)):
            HoleScore.objects.create(
                round=active, player=player, hole=hole, gross_value=points, net_value=1
            )

        response = self.client.get('/leaderboard/?format=18_ind_chicago')
        row = response.context['net_leaderboard'][0]
        self.assertEqual(row['holes_played'], 3)
        self.assertEqual(row['strokes'], 10)
        self.assertEqual(row['net_score'], '10 Pts')

    def test_scorecard_save_stores_points_for_chicago_and_strokes_otherwise(self):
        player = Player.objects.create(name='Jan')
        hole = Hole.objects.create(hole_number=1, par=4)
        chicago = GolfRound.objects.create(game_format='18_IND_CHICAGO', is_active=True)

        saved = self.client.post(
            '/scorecard/save-stroke-api/',
            data=json.dumps({
                'player_id': player.id,
                'hole_id': hole.id,
                'round_id': chicago.id,
                'gross_value': 0,
            }),
            content_type='application/json',
        )
        self.assertEqual(saved.status_code, 200)
        row = HoleScore.objects.get(round=chicago, player=player, hole=hole)
        self.assertEqual((row.gross_value, row.net_value), (0, 1))

        rejected = self.client.post(
            '/scorecard/save-stroke-api/',
            data=json.dumps({
                'player_id': player.id,
                'hole_id': hole.id,
                'round_id': chicago.id,
                'gross_value': 3,
            }),
            content_type='application/json',
        )
        self.assertEqual(rejected.status_code, 400)
        row.refresh_from_db()
        self.assertEqual(row.gross_value, 0)

        cleared = self.client.post(
            '/scorecard/save-stroke-api/',
            data=json.dumps({
                'player_id': player.id,
                'hole_id': hole.id,
                'round_id': chicago.id,
                'gross_value': None,
            }),
            content_type='application/json',
        )
        self.assertEqual(cleared.status_code, 200)
        self.assertFalse(HoleScore.objects.filter(round=chicago, player=player, hole=hole).exists())

        stroke_round = GolfRound.objects.create(game_format='18_GROSS_NET', is_active=False)
        stroke_saved = self.client.post(
            '/scorecard/save-stroke-api/',
            data=json.dumps({
                'player_id': player.id,
                'hole_id': hole.id,
                'round_id': stroke_round.id,
                'gross_value': 5,
            }),
            content_type='application/json',
        )
        self.assertEqual(stroke_saved.status_code, 200)
        stroke_row = HoleScore.objects.get(round=stroke_round, player=player, hole=hole)
        self.assertEqual((stroke_row.gross_value, stroke_row.net_value), (5, 0))


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


class MensLeagueScorecardTests(TestCase):
    def test_card_shows_each_hole_plus_front_back_and_total(self):
        staff = User.objects.create_user('staff', password='pw', is_staff=True)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 19)]
        alan = Player.objects.create(name='Alan Braner')
        doug = Player.objects.create(name='Doug Anderson')
        active = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=True)
        for hole in holes[:9]:
            HoleScore.objects.create(round=active, player=alan, hole=hole, gross_value=4)
        HoleScore.objects.create(round=active, player=alan, hole=holes[9], gross_value=5)
        HoleScore.objects.create(round=active, player=alan, hole=holes[17], gross_value=0)
        HoleScore.objects.create(round=active, player=doug, hole=holes[10], gross_value=6)

        self.client.force_login(staff)
        response = self.client.get('/admin-dashboard/mens-league-scorecard/?from_hole=10')
        self.assertContains(response, 'Alan Braner')
        self.assertContains(response, 'max-width: 520px')
        self.assertContains(response, 'var hole = 10')
        self.assertContains(response, '/play/hole/')
        self.assertContains(response, 'Doug Anderson')
        self.assertContains(response, '>Out<')
        self.assertContains(response, '>In<')
        self.assertContains(response, '>Total<')
        self.assertContains(response, 'width: 200%')
        self.assertContains(response, 'Slide for the back nine.')
        page = response.content.decode()
        alan_at = page.find('Alan Braner')
        doug_at = page.find('Doug Anderson')
        self.assertLess(doug_at, alan_at)
        alan_row = page[alan_at:doug_at if doug_at > alan_at else None]
        # Front nine is nine 4s. Back is the 5 on hole 10. The zero on 18 is blank.
        self.assertIn('>36<', alan_row)
        self.assertIn('>5<', alan_row)
        self.assertIn('>41<', alan_row)

        self.client.logout()
        guest = self.client.get('/admin-dashboard/mens-league-scorecard/')
        self.assertEqual(guest.status_code, 302)


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


class NineHolePracticeHandicapTests(TestCase):
    def test_practice_round_does_not_change_handicaps(self):
        player = Player.objects.create(name='Pat', handicap=11, ladies_league_handicap=7)
        holes = [Hole.objects.create(hole_number=n, par=4) for n in range(1, 10)]
        active = GolfRound.objects.create(game_format='9_HOLE_PRACTICE', is_active=True)
        for hole in holes:
            HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=6)

        played = HoleScore.objects.filter(round=active, player=player)
        self.assertIsNone(adjust_ladies_handicap_for_player(player, played, active))
        self.assertIsNone(adjust_mens_handicap_for_player(player, played, active))
        self.assertEqual(apply_womens_handicap_updates(active), [])
        self.assertEqual(apply_mens_handicap_updates(active), [])

        staff = User.objects.create_user('practice-staff', password='pw', is_staff=True)
        self.client.force_login(staff)
        board = self.client.get('/leaderboard/?format=9_hole_practice')
        self.assertNotContains(board, 'Update Ladies Handicaps')
        self.assertNotContains(board, 'Update Player Handicaps')
        self.assertNotContains(board, 'Handicap:')
        self.assertContains(board, 'Back to the Ninth Hole')
        self.assertContains(board, '/play/hole/9/')

        finish = self.client.get('/play/finish/')
        self.assertRedirects(finish, '/leaderboard/?format=9_hole_practice', fetch_redirect_response=False)

        self.client.post('/admin-dashboard/finalize-handicaps/')
        player.refresh_from_db()
        self.assertEqual(player.handicap, 11)
        self.assertEqual(player.ladies_league_handicap, 7)
        self.assertEqual(WomensLeagueRoundScore.objects.count(), 0)
        self.assertEqual(MensLeagueRoundScore.objects.count(), 0)

        GolfRound.objects.filter(is_active=True).update(is_active=False)
        again = GolfRound.objects.create(game_format='9_HOLE_PRACTICE', is_active=True)
        for hole in holes:
            HoleScore.objects.create(round=again, player=player, hole=hole, gross_value=6)
        self.client.post('/admin-dashboard/reset-game/')
        player.refresh_from_db()
        self.assertEqual(player.handicap, 11)
        self.assertEqual(player.ladies_league_handicap, 7)
        self.assertEqual(WomensLeagueRoundScore.objects.count(), 0)
        self.assertEqual(MensLeagueRoundScore.objects.count(), 0)

    def test_practice_leaderboard_logout_starts_a_fresh_game(self):
        keeper_user = User.objects.create_user('keeper', password='pw')
        partner = Player.objects.create(name='Pat Partner')
        player = Player.objects.create(
            name='Pat',
            user=keeper_user,
            handicap=11,
            ladies_league_handicap=7,
            is_playing_today=True,
            is_captain=True,
            riding_partner=partner,
        )
        hole = Hole.objects.create(hole_number=9, par=4)
        active = GolfRound.objects.create(game_format='9_HOLE_PRACTICE', is_active=True)
        squad = Squad.objects.create(
            round=active, squad_number=1, starting_hole=hole, scorekeeper=player
        )
        squad.players.add(player)
        HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=5)

        self.client.force_login(keeper_user)
        board = self.client.get('/leaderboard/?format=9_hole_practice')
        self.assertContains(board, 'name="erase_practice"')

        stayed = self.client.get('/logout/')
        self.assertRedirects(stayed, '/login/')
        self.assertTrue(GolfRound.objects.filter(id=active.id).exists())

        self.client.force_login(keeper_user)
        response = self.client.post('/logout/', {'erase_practice': '1'})
        self.assertRedirects(response, '/login/')
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertFalse(GolfRound.objects.filter(id=active.id).exists())
        self.assertFalse(HoleScore.objects.exists())
        self.assertFalse(Squad.objects.exists())
        fresh = GolfRound.objects.get(is_active=True)
        self.assertEqual(fresh.game_format, '')
        player.refresh_from_db()
        self.assertFalse(player.is_playing_today)
        self.assertFalse(player.is_captain)
        self.assertIsNone(player.riding_partner_id)
        self.assertEqual(player.handicap, 11)
        self.assertEqual(player.ladies_league_handicap, 7)

    def test_logout_does_not_erase_a_league_round(self):
        keeper_user = User.objects.create_user('keeper', password='pw')
        player = Player.objects.create(name='Pat', user=keeper_user, handicap=11, is_playing_today=True)
        hole = Hole.objects.create(hole_number=1, par=4)
        active = GolfRound.objects.create(game_format='18_HOLE_MENS_LEAGUE', is_active=True)
        HoleScore.objects.create(round=active, player=player, hole=hole, gross_value=4)

        self.client.force_login(keeper_user)
        response = self.client.post('/logout/', {'erase_practice': '1'})
        self.assertRedirects(response, '/login/')
        self.assertTrue(GolfRound.objects.filter(id=active.id).exists())
        self.assertTrue(HoleScore.objects.filter(round=active, gross_value=4).exists())
        player.refresh_from_db()
        self.assertTrue(player.is_playing_today)


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


class AllMembersScorekeeperTests(TestCase):
    def test_members_page_shows_a_scorekeeper_checkbox(self):
        Player.objects.create(name='Kay Stone', scorekeeper=True)
        response = self.client.get('/admin-dashboard/all-members/')
        self.assertContains(response, 'Scorekeeper')
        self.assertContains(response, 'updateScorekeeper')
        self.assertContains(response, 'checked')

    def test_members_page_scrolls_nine_rows_and_has_a_search(self):
        for number in range(10):
            Player.objects.create(name=f'Player {number} Stone', member_id=f'GLF-TEST-{number}')
        response = self.client.get('/admin-dashboard/all-members/')
        self.assertContains(response, 'id="member-scroll"')
        self.assertContains(response, 'fitNineRows')
        self.assertContains(response, 'id="member-search"')
        self.assertContains(response, 'id="show-all-members"')
        self.assertContains(response, 'All Members')
        self.assertContains(response, 'Player 0 Stone')
        self.assertContains(response, 'Player 9 Stone')

    def test_checkbox_saves_the_scorekeeper_flag(self):
        player = Player.objects.create(name='Lee Stone', scorekeeper=False)
        response = self.client.post(
            '/admin-dashboard/toggle-scorekeeper/',
            data=json.dumps({'player_id': player.id, 'scorekeeper': True}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)
        player.refresh_from_db()
        self.assertTrue(player.scorekeeper)


class ManualSquadScorekeeperLabelTests(TestCase):
    def test_scorekeeper_label_follows_the_player_name(self):
        keeper = Player.objects.create(name='Ann Stone', is_playing_today=True, scorekeeper=True)
        other = Player.objects.create(name='Bob Smith', is_playing_today=True, scorekeeper=False)
        self.assertEqual(player_squad_choice_label(keeper), 'Ann Stone ( Score Keeper )')
        self.assertEqual(player_squad_choice_label(other), 'Bob Smith')
        self.assertEqual(designated_scorekeeper_label(keeper), 'Ann Stone (scorekeeper)')

        staff = User.objects.create_user('staff', password='pw', is_staff=True)
        self.client.force_login(staff)
        response = self.client.get('/admin-dashboard/manual-squad/')
        self.assertContains(response, 'Ann Stone ( Score Keeper )')
        self.assertNotContains(response, 'Bob Smith ( Score Keeper )')
        scorekeeper_names = list(
            response.context['form'].fields['scorekeeper'].queryset.values_list('name', flat=True)
        )
        self.assertEqual(scorekeeper_names, ['Ann Stone'])
        self.assertContains(response, 'Ann Stone (scorekeeper)')


class SquadViewerScorecardTests(TestCase):
    def setUp(self):
        self.keeper_user = User.objects.create_user('keeper', password='pw')
        self.member_user = User.objects.create_user('member', password='pw')
        self.keeper = Player.objects.create(name='Ann Stone', user=self.keeper_user, scorekeeper=True)
        self.member = Player.objects.create(name='Bob Smith', user=self.member_user)
        self.hole = Hole.objects.create(hole_number=1, par=4, handicap_index=1)
        self.round = GolfRound.objects.create(game_format='18_GROSS_NET', is_active=True)
        self.squad = Squad.objects.create(
            round=self.round, squad_number=1, starting_hole=self.hole, scorekeeper=self.keeper
        )
        self.squad.players.add(self.keeper, self.member)

    def test_squad_member_can_view_the_hole_and_leaderboard_but_not_enter_scores(self):
        self.client.force_login(self.member_user)
        response = self.client.get('/play/hole/1/')
        self.assertContains(response, 'Hole 1')
        self.assertContains(response, 'Leaderboard')
        self.assertContains(response, 'View only. The scorekeeper enters the scores.')
        self.assertContains(response, 'color:#c62828;')
        gross_html = response.content.decode()
        self.assertLess(
            gross_html.find('View only. The scorekeeper enters the scores.'),
            gross_html.find('class="gn-leaderboard"'),
        )
        self.assertContains(response, '-webkit-text-stroke: 1px #000')
        self.assertContains(response, 'net-locked')
        self.assertContains(response, 'disabled')

        denied = self.client.post(
            '/scorecard/save-stroke-api/',
            data=json.dumps({
                'player_id': self.member.id,
                'hole_id': self.hole.id,
                'round_id': self.round.id,
                'gross_value': 5,
            }),
            content_type='application/json',
        )
        self.assertEqual(denied.status_code, 403)
        self.assertFalse(HoleScore.objects.filter(player=self.member).exists())

    def test_scorekeeper_can_enter_a_squad_score(self):
        self.client.force_login(self.keeper_user)
        response = self.client.get('/play/hole/1/')
        self.assertNotContains(response, 'View only. The scorekeeper enters the scores.')
        self.assertNotContains(response, 'net-locked')
        net_tag = response.content.decode().split('class="num-input net-display"', 1)[1].split('>', 1)[0]
        self.assertIn('#e2e8f0', net_tag)

        saved = self.client.post(
            '/scorecard/save-stroke-api/',
            data=json.dumps({
                'player_id': self.member.id,
                'hole_id': self.hole.id,
                'round_id': self.round.id,
                'gross_value': 4,
            }),
            content_type='application/json',
        )
        self.assertEqual(saved.status_code, 200)
        self.assertTrue(HoleScore.objects.filter(player=self.member, gross_value=4).exists())

    def test_mens_league_handicap_stays_locked_for_the_scorekeeper(self):
        self.round.game_format = '18_HOLE_MENS_LEAGUE'
        self.round.save(update_fields=['game_format'])
        self.keeper.handicap = 12
        self.keeper.save(update_fields=['handicap'])
        self.client.force_login(self.keeper_user)
        response = self.client.get('/play/hole/1/')
        self.assertContains(response, 'value="12"')
        self.assertContains(response, 'readonly')
        self.assertContains(response, 'cursor: not-allowed')

    def test_gross_net_handicap_stays_locked_for_the_scorekeeper(self):
        self.keeper.handicap = 24
        self.keeper.save(update_fields=['handicap'])
        self.client.force_login(self.keeper_user)
        response = self.client.get('/play/hole/1/')
        self.assertContains(response, 'value="24"')
        self.assertContains(response, 'readonly')
        self.assertContains(response, 'cursor: not-allowed')

    def test_mens_league_hides_previous_on_the_starting_hole(self):
        hole_ten = Hole.objects.create(hole_number=10, par=4, handicap_index=10)
        Hole.objects.create(hole_number=11, par=4, handicap_index=11)
        self.squad.starting_hole = hole_ten
        self.squad.save(update_fields=['starting_hole'])
        self.round.game_format = '18_HOLE_MENS_LEAGUE'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.keeper_user)

        on_start = self.client.get('/play/hole/10/')
        self.assertNotContains(on_start, '⬅️ Prev')
        self.assertContains(on_start, 'flex: 1; order: 1')
        self.assertContains(on_start, 'flex: 1.5; order: 2')
        self.assertNotContains(on_start, ">Men's League Scorecard<")
        self.assertContains(on_start, '/admin-dashboard/mens-league-scorecard/?from_hole=10')
        self.assertContains(on_start, 'max-height: 520px')

        later = self.client.get('/play/hole/11/')
        self.assertContains(later, '⬅️ Prev')
        self.assertContains(later, 'flex: 1.5; order: 2')
        self.assertContains(later, 'flex: 1; order: 3')

        self.round.game_format = '18_GROSS_NET'
        self.round.save(update_fields=['game_format'])
        gross_start = self.client.get('/play/hole/10/')
        self.assertNotContains(gross_start, 'mens-league-scorecard')
        self.assertNotContains(gross_start, '⬅️ Prev')
        self.assertContains(gross_start, 'class="gn-nav"')
        self.assertContains(gross_start, 'class="gn-next"')
        self.assertContains(gross_start, 'grid-column: 1 / -1;')
        self.assertContains(gross_start, 'class="gn-leaderboard"')
        gross_later = self.client.get('/play/hole/11/')
        self.assertContains(gross_later, '⬅️ Prev')
        self.assertContains(gross_later, 'class="gn-prev"')
        self.assertContains(gross_later, 'grid-column: 2;')
        self.assertContains(gross_later, 'class="gn-leaderboard"')

    def test_mens_league_eighteenth_hole_uses_the_same_leaderboard_button(self):
        Hole.objects.create(hole_number=17, par=4, handicap_index=17)
        Hole.objects.create(hole_number=18, par=4, handicap_index=18)
        self.round.game_format = '18_HOLE_MENS_LEAGUE'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.keeper_user)

        seventeenth = self.client.get('/play/hole/17/')
        eighteenth = self.client.get('/play/hole/18/')
        self.assertContains(seventeenth, '🏆 Leaderboard')
        self.assertContains(seventeenth, 'standings=1&amp;from_hole=17')
        self.assertNotContains(eighteenth, 'Finish Match')
        self.assertContains(eighteenth, '🏆 Leaderboard')
        self.assertContains(eighteenth, 'standings=1&amp;from_hole=18')

        board = self.client.get('/leaderboard/?standings=1&from_hole=18')
        board_html = board.content.decode()
        self.assertContains(board, 'Return to Hole 18')
        self.assertContains(board, '🚪 Log Out')
        self.assertLess(board_html.find('Return to Hole 18'), board_html.find('🚪 Log Out'))
        self.assertIn('margin-left: auto', board_html)

    def test_team_chicago_matches_gross_net_navigation(self):
        hole_five = Hole.objects.create(hole_number=5, par=4, handicap_index=5)
        Hole.objects.create(hole_number=6, par=4, handicap_index=6)
        self.squad.starting_hole = hole_five
        self.squad.save(update_fields=['starting_hole'])
        self.round.game_format = '9_TEAM_CHICAGO'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.keeper_user)

        on_start = self.client.get('/play/hole/5/')
        self.assertNotContains(on_start, 'Previous Hole')
        self.assertContains(on_start, 'class="tc-nav"')
        self.assertContains(on_start, 'Next Hole')
        self.assertContains(on_start, 'grid-column: 1 / -1;')
        self.assertContains(on_start, 'class="btn-nav tc-leaderboard"')

        later = self.client.get('/play/hole/6/')
        self.assertContains(later, 'Previous Hole')
        self.assertContains(later, 'grid-column: 2;')
        self.assertContains(later, 'class="btn-nav tc-leaderboard"')

    def test_womens_league_matches_gross_net_navigation(self):
        hole_five = Hole.objects.create(hole_number=5, par=4, handicap_index=5)
        Hole.objects.create(hole_number=6, par=3, handicap_index=6)
        self.squad.starting_hole = hole_five
        self.squad.save(update_fields=['starting_hole'])
        self.round.game_format = '9_WOMENS_LEAGUE'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.keeper_user)

        on_start = self.client.get('/play/hole/5/')
        self.assertNotContains(on_start, '⬅️ Prev')
        self.assertContains(on_start, 'class="gn-nav"')
        self.assertContains(on_start, 'class="gn-next"')
        self.assertContains(on_start, 'grid-column: 1 / -1;')
        self.assertContains(on_start, 'class="gn-leaderboard"')

        later = self.client.get('/play/hole/6/')
        self.assertContains(later, '⬅️ Prev')
        self.assertContains(later, 'class="gn-prev"')
        self.assertContains(later, 'grid-column: 2;')
        self.assertContains(later, 'class="gn-leaderboard"')

    def test_nine_hole_practice_matches_womens_card_without_handicap_or_net(self):
        hole_five = Hole.objects.create(hole_number=5, par=4, handicap_index=5)
        Hole.objects.create(hole_number=6, par=3, handicap_index=6)
        self.squad.starting_hole = hole_five
        self.squad.save(update_fields=['starting_hole'])
        self.round.game_format = '9_HOLE_PRACTICE'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.keeper_user)

        on_start = self.client.get('/play/hole/5/')
        self.assertNotContains(on_start, '⬅️ Prev')
        self.assertContains(on_start, 'class="gn-nav"')
        self.assertContains(on_start, 'class="gn-next"')
        self.assertContains(on_start, '>Gross<')
        self.assertNotContains(on_start, 'Handicap:')
        self.assertNotContains(on_start, '>Net<')
        self.assertContains(on_start, 'Bob Smith')

        later = self.client.get('/play/hole/6/')
        self.assertContains(later, '⬅️ Prev')
        self.assertContains(later, 'class="gn-prev"')
        self.assertNotContains(later, 'Handicap:')
        self.assertNotContains(later, '>Net<')

    def test_eighteen_chicago_matches_paired_navigation(self):
        Hole.objects.create(hole_number=2, par=4, handicap_index=2)
        self.round.game_format = '18_IND_CHICAGO'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.keeper_user)

        on_start = self.client.get('/play/hole/1/')
        self.assertNotContains(on_start, '⬅️ Prev')
        self.assertContains(on_start, 'class="gn-nav"')
        self.assertContains(on_start, 'class="gn-next"')
        self.assertContains(on_start, 'grid-column: 1 / -1;')
        self.assertContains(on_start, 'class="gn-leaderboard"')

        later = self.client.get('/play/hole/2/')
        self.assertContains(later, '⬅️ Prev')
        self.assertContains(later, 'class="gn-prev"')
        self.assertContains(later, 'grid-column: 2;')
        self.assertContains(later, 'class="gn-leaderboard"')

    def test_eighteen_chicago_quota_comes_from_the_player_field(self):
        self.round.game_format = '18_IND_CHICAGO'
        self.round.save(update_fields=['game_format'])
        self.keeper.chicago_points_18 = 15
        self.keeper.handicap = 10
        self.keeper.save(update_fields=['chicago_points_18', 'handicap'])
        self.member.chicago_points_18 = 0
        self.member.handicap = 10
        self.member.save(update_fields=['chicago_points_18', 'handicap'])
        self.client.force_login(self.keeper_user)

        response = self.client.get('/play/hole/1/')
        self.assertContains(response, 'value="15"')
        self.assertContains(response, 'value="0"')
        self.assertNotContains(response, 'value="29"')

    def test_eighteen_chicago_view_only_note_is_below_the_leaderboard(self):
        self.round.game_format = '18_IND_CHICAGO'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.member_user)
        response = self.client.get('/play/hole/1/')
        html = response.content.decode()
        note = 'View only. The scorekeeper enters the scores.'
        self.assertLess(html.find('class="gn-leaderboard"'), html.find(note))
        self.assertNotContains(response, '-webkit-text-stroke')

    def test_team_chicago_viewer_total_matches_points_needed_background(self):
        self.round.game_format = '9_TEAM_CHICAGO'
        self.round.save(update_fields=['game_format'])

        self.client.force_login(self.member_user)
        viewer = self.client.get('/play/hole/1/')
        viewer_total = viewer.content.decode().split('class="net-display"', 1)[1].split('>', 1)[0]
        self.assertIn('background-color: #e0f2f1', viewer_total)
        self.assertContains(viewer, 'text-align: center;">View only. The scorekeeper enters the scores.')

        self.client.force_login(self.keeper_user)
        keeper = self.client.get('/play/hole/1/')
        keeper_total = keeper.content.decode().split('class="net-display"', 1)[1].split('>', 1)[0]
        self.assertIn('background-color: #f1f8e9', keeper_total)

    def test_scramble_hides_previous_on_the_starting_hole(self):
        hole_five = Hole.objects.create(hole_number=5, par=4, handicap_index=5)
        Hole.objects.create(hole_number=6, par=3, handicap_index=6)
        self.squad.starting_hole = hole_five
        self.squad.save(update_fields=['starting_hole'])
        self.round.game_format = '9_HOLE_SCRAMBLE'
        self.round.save(update_fields=['game_format'])
        self.client.force_login(self.keeper_user)

        on_start = self.client.get('/play/hole/5/')
        start_html = on_start.content.decode()
        self.assertContains(on_start, 'Scramble Live Card')
        self.assertNotContains(on_start, 'Prev')
        self.assertLess(start_html.find('Next'), start_html.find('Leaderboard'))

        later = self.client.get('/play/hole/6/')
        later_html = later.content.decode()
        self.assertLess(later_html.find('Prev'), later_html.find('Next'))
        self.assertLess(later_html.find('Next'), later_html.find('Leaderboard'))
        self.assertContains(later, 'btn-leaderboard')
        self.assertIn('grid-column: 1 / -1', later_html)

    def test_scramble_leaderboard_shows_team_places_and_returns_to_the_hole(self):
        hole_five = Hole.objects.create(hole_number=5, par=4, handicap_index=5)
        self.squad.starting_hole = hole_five
        self.squad.save(update_fields=['starting_hole'])
        self.round.game_format = '9_HOLE_SCRAMBLE'
        self.round.save(update_fields=['game_format'])
        HoleScore.objects.create(round=self.round, player=self.keeper, hole=hole_five, gross_value=4)
        self.client.force_login(self.keeper_user)

        card = self.client.get('/play/hole/5/')
        self.assertContains(card, 'format=9_hole_scramble')
        self.assertContains(card, 'standings=1')
        self.assertContains(card, 'from_hole=5')

        board = self.client.get('/leaderboard/?format=9_hole_scramble&standings=1&from_hole=5')
        self.assertContains(board, 'Return to Hole 5')
        self.assertContains(board, '/play/hole/5/')
        self.assertContains(board, 'Ann Stone')
        self.assertContains(board, 'Bob Smith')
        self.assertNotContains(board, 'Payout')
        self.assertNotContains(board, 'Outing Financial Matrix')

        full_board = self.client.get('/leaderboard/?format=9_hole_scramble')
        self.assertContains(full_board, 'Ann Stone')
        self.assertNotContains(full_board, 'Payout')
        self.assertNotContains(full_board, 'Outing Financial Matrix')


class LoginPasswordToggleTests(TestCase):
    def test_login_page_has_a_control_that_shows_the_password(self):
        response = self.client.get('/login/')
        self.assertContains(response, 'id="toggle-password"')
        self.assertContains(response, 'aria-label="Show password"')
        self.assertContains(response, 'id="id_password"')
        self.assertContains(response, 'field.type = showing ? "password" : "text"')
