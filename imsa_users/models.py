from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    CLASS_CHOICES = [
        ('GTP', 'GTP (Grand Touring Prototype)'),
        ('LMP2', 'LMP2 (Le Mans Prototype 2)'),
        ('GTD', 'GTD (Grand Touring Daytona)'),
        ('GTD_PRO', 'GTD Pro'),
    ]
    
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='teams/logos/', blank=True, null=True)
    description = models.TextField()
    car_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_teams')
    created_at = models.DateTimeField(auto_now_add=True)
    sponsors = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('DRIVER', 'Пилот'),
        ('ENGINEER', 'Инженер'),
        ('MECHANIC', 'Механик'),
        ('MANAGER', 'Менеджер'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_confirmed = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('team', 'user')

class TeamVacancy(models.Model):
    ROLE_CHOICES = [
        ('DRIVER', 'Пилот'),
        ('ENGINEER', 'Инженер'),
        ('MECHANIC', 'Механик'),
        ('MANAGER', 'Менеджер'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='vacancies')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    description = models.TextField()
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class TeamApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'На рассмотрении'),
        ('APPROVED', 'Одобрена'),
        ('REJECTED', 'Отклонена'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(TeamVacancy, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    applied_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

class TournamentRegistration(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'На рассмотрении'),
        ('APPROVED', 'Одобрена'),
        ('REJECTED', 'Отклонена'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='registrations')
    tournament_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_number = models.IntegerField()
    license_info = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    applied_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)