from django.db import models

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
        if self.home_score > self.away_score:
            self.home_team.points += 3
        elif self.home_score < self.away_score:
            self.away_team.points += 3
        else:
            self.home_team.points += 1
            self.away_team.points += 1

        self.home_team.goal_difference += self.home_score - self.away_score
        self.away_team.goal_difference += self.away_score - self.home_score

        self.home_team.save()
        self.away_team.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        if self.home_score > self.away_score:
            self.home_team.points -= 3
        elif self.home_score < self.away_score:
            self.away_team.points -= 3
        else:
            self.home_team.points -= 1
            self.away_team.points -= 1

        self.home_team.goal_difference -= self.home_score - self.away_score
        self.away_team.goal_difference -= self.away_score - self.home_score

        self.home_team.save()
        self.away_team.save()

        super().delete(*args, **kwargs)