# models.py
from django.db import models

class Participant(models.Model):
    CAR_CHOICES = [
        ('Porsche', 'Porsche'),
        ('Ferrari', 'Ferrari'),
        ('BMW', 'BMW'),
        ('Audi', 'Audi'),
        ('Mercedes', 'Mercedes'),
        ('Corvette', 'Corvette'),
    ]
    
    name = models.CharField(max_length=100)
    car = models.CharField(max_length=20, choices=CAR_CHOICES)
    daytona = models.FloatField()
    sebring = models.FloatField()
    weathertech = models.FloatField()
    virginia = models.FloatField()
    atlanta = models.FloatField()
    total = models.FloatField()

    def save(self, *args, **kwargs):
        self.total = self.daytona + self.sebring + self.weathertech + self.virginia + self.atlanta
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.car})"