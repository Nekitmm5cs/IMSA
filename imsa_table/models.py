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

    def save(self, *args, **kwargs):
        self.total = self.daytona + self.sebring + self.weathertech + self.virginia + self.atlanta
        super().save(*args, **kwargs)