from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('DRIVER', 'Пилот'),
        ('ENGINEER', 'Инженер'),
        ('MECHANIC', 'Механик'),
        ('MANAGER', 'Менеджер'),
        ('ORGANIZER', 'Организатор'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    license_type = models.CharField(max_length=50, blank=True)
    experience_years = models.IntegerField(default=0)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='DRIVER')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class UserSkill(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='skills')
    speed = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    endurance = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    technique = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    strategy = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Skills"

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.CharField(max_length=20)  # Может быть годом или полной датой
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class FavoriteTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_tracks')
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    length = models.CharField(max_length=20, blank=True)
    record = models.CharField(max_length=20, blank=True)
    is_favorite = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class FavoriteCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_cars')
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    year = models.CharField(max_length=10, blank=True)
    power = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    is_favorite = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

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

    def __str__(self):
        return f"{self.user.username} in {self.team.name} as {self.role}"

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

    def __str__(self):
        return f"{self.team.name} - {self.role} vacancy"

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

    def __str__(self):
        return f"{self.user.username} application to {self.team.name}"

class Tournament(models.Model):
    STATUS_CHOICES = [
        ('UPCOMING', 'Предстоящий'),
        ('ONGOING', 'Текущий'),
        ('COMPLETED', 'Завершен'),
        ('CANCELLED', 'Отменен'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='organized_tournaments')
    max_teams = models.IntegerField()
    registration_deadline = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='UPCOMING')
    rules = models.TextField(blank=True)
    prize_pool = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TournamentRegistration(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'На рассмотрении'),
        ('APPROVED', 'Одобрена'),
        ('REJECTED', 'Отклонена'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='registrations')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='registrations')
    car_model = models.CharField(max_length=100)
    car_number = models.IntegerField()
    license_info = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    applied_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('team', 'tournament')

    def __str__(self):
        return f"{self.team.name} registration for {self.tournament.name}"