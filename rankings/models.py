from django.db import models
from . import utils

class Team(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.PositiveIntegerField()
    away_score = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        
        utils.update_score(self, 1)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        utils.update_score(self, -1)
        super().delete(*args, **kwargs)