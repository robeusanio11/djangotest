from django.db import models

# Create your models here.

class Teams(models.Model):
    id = models.IntegerField(primary_key="true")
    abbr = models.CharField(max_length=3, null="true")

class Roster(models.Model):
    id = models.IntegerField(primary_key="true");
    teamID = models.ForeignKey(Teams, on_delete=models.CASCADE)
    playerName = models.CharField(max_length=50)