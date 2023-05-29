from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Team, Match
import csv
import io
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TeamListView(ListView):
    model = Team
    template_name = 'rankings/team_list.html'
    context_object_name = 'teams'
    ordering = ['-points', 'name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matches'] = Match.objects.all()
        return context

class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    template_name = 'rankings/match_form.html'
    fields = ['home_team', 'home_score', 'away_team', 'away_score']
    success_url = reverse_lazy('team_list')

class MatchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Match
    template_name = 'rankings/match_form.html'
    fields = ['home_team', 'home_score', 'away_team', 'away_score']
    success_url = reverse_lazy('team_list')

    
    def test_func(self):
        match = self.get_object()
        return self.request.user.is_superuser or self.request.user.username == match.home_team.name or self.request.user.username == match.away_team.name

class MatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Match
    template_name = 'rankings/match_confirm_delete.html'
    success_url = reverse_lazy('team_list')

    def test_func(self):
        match = self.get_object()
        return self.request.user.is_superuser or self.request.user.username == match.home_team.name or self.request.user.username == match.away_team.name

def process_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        Match.objects.all().delete()
        Team.objects.all().delete()
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        for row in reader:
            team1_name, team1_score, team2_name, team2_score = row
            team1_score = int(team1_score)
            team2_score = int(team2_score)

            try:
                team1 = Team.objects.get(name=team1_name)
            except Team.DoesNotExist:
                team1 = Team.objects.create(name=team1_name)

            try:
                team2 = Team.objects.get(name=team2_name)
            except Team.DoesNotExist:
                team2 = Team.objects.create(name=team2_name)

            Match.objects.create(home_team=team1, away_team=team2, home_score=team1_score, away_score=team2_score)

    return redirect('team_list')
