from django.test import TestCase, Client
from django.urls import reverse
from .models import Team, Match

class TeamListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('team_list')

    def test_team_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rankings/team_list.html')

class MatchCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('match_create')

    def test_match_create_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rankings/match_form.html')

    def test_match_create_view_post(self):
        home_team = Team.objects.create(name='Home Team')
        away_team = Team.objects.create(name='Away Team')
        data = {
            'home_team': home_team.id,
            'home_score': 2,
            'away_team': away_team.id,
            'away_score': 1
        }
        response = self.client.post(self.url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rankings/team_list.html')

        home_team.refresh_from_db()
        away_team.refresh_from_db()
        self.assertEqual(home_team.points, 3)
        self.assertEqual(away_team.points, 0)
        self.assertEqual(home_team.goal_difference, 1)
        self.assertEqual(away_team.goal_difference, -1)
