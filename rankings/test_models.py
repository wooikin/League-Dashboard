from django.test import TestCase
from .models import Team, Match

class TeamModelTestCase(TestCase):
    def test_points_default_value(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.points, 0)

    def test_goal_difference_default_value(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.goal_difference, 0)

class MatchModelTestCase(TestCase):
    def test_match_creation(self):
        home_team = Team.objects.create(name='Home Team')
        away_team = Team.objects.create(name='Away Team')

        match = Match.objects.create(home_team=home_team, away_team=away_team, home_score=2, away_score=1)

        self.assertEqual(match.home_team, home_team)
        self.assertEqual(match.away_team, away_team)
        self.assertEqual(match.home_score, 2)
        self.assertEqual(match.away_score, 1)
        self.assertEqual(home_team.points, 3)
        self.assertEqual(away_team.points, 0)
        self.assertEqual(home_team.goal_difference, 1)
        self.assertEqual(away_team.goal_difference, -1)
