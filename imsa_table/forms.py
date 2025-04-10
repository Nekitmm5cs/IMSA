from django import forms
from .models import RaceParticipant

class RaceParticipantForm(forms.ModelForm):
    class Meta:
        model = RaceParticipant
        fields = ['name', 'daytona', 'sebring', 'weathertech', 'virginia', 'atlanta']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя участника'}),
            'daytona': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Daytona'}),
            'sebring': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Sebring'}),
            'weathertech': forms.NumberInput(attrs={'placeholder': 'Введите баллы для WeatherTech'}),
            'virginia': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Virginia'}),
            'atlanta': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Atlanta'}),
        }