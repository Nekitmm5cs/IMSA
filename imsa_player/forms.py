from django import forms
from .models import Team, TeamVacancy, TeamApplication, TournamentRegistration

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'logo', 'description', 'car_class', 'sponsors']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'sponsors': forms.Textarea(attrs={'rows': 3}),
        }

class TeamVacancyForm(forms.ModelForm):
    class Meta:
        model = TeamVacancy
        fields = ['role', 'description', 'requirements']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 4}),
        }

class TeamApplicationForm(forms.ModelForm):
    class Meta:
        model = TeamApplication
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class TournamentRegistrationForm(forms.ModelForm):
    class Meta:
        model = TournamentRegistration
        fields = ['tournament_name', 'car_model', 'car_number', 'license_info']
        widgets = {
            'license_info': forms.Textarea(attrs={'rows': 4}),
        }