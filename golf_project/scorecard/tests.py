from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from scorecard.models import Cost, GolfRound, Hole, HoleScore, Player


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
