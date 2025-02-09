from django.db import models

class RaceParticipant(models.Model):
    name = models.CharField(max_length=100)
    daytona = models.FloatField(default=0)
    sebring = models.FloatField(default=0)
    weathertech = models.FloatField(default=0)
    virginia = models.FloatField(default=0)
    atlanta = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Leader(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    date_achieved = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name