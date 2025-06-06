from django import forms
from .models import Team, TeamVacancy, TeamApplication, TournamentRegistration

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'logo', 'car_class', 'description', 'sponsors']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'sponsors': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }
        labels = {
            'name': 'Название команды',
            'logo': 'Логотип',
            'car_class': 'Класс автомобиля',
            'description': 'Описание команды',
            'sponsors': 'Спонсоры',
        }

class TeamVacancyForm(forms.ModelForm):
    class Meta:
        model = TeamVacancy
        fields = ['role', 'description', 'requirements']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'requirements': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class TeamApplicationForm(forms.ModelForm):
    class Meta:
        model = TeamApplication
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class TournamentRegistrationForm(forms.ModelForm):
    class Meta:
        model = TournamentRegistration
        fields = ['tournament', 'car_model', 'car_number', 'license_info', 'notes']
        widgets = {
            'tournament': forms.Select(attrs={'class': 'form-control'}),
            'license_info': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }
        labels = {
            'tournament': 'Турнир',
            'car_model': 'Модель автомобиля',
            'car_number': 'Номер автомобиля',
            'license_info': 'Информация о лицензии',
            'notes': 'Примечания',
        }
