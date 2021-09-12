from django.db import models


class Comand(models.Model):
    rating = models.CharField(max_length=10)
    logo = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    games = models.CharField(max_length=10)
    wins = models.CharField(max_length=10)
    draws = models.CharField(max_length=10)
    losses = models.CharField(max_length=10)
    goals_in = models.CharField(max_length=10)
    goals_out = models.CharField(max_length=10)
    scores = models.CharField(max_length=10)
    difference = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name