from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'car', 'daytona', 'sebring', 'weathertech', 'virginia', 'atlanta']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя участника'}),
            'car': forms.Select(attrs={'class': 'form-control'}),
            'daytona': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Daytona'}),
            'sebring': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Sebring'}),
            'weathertech': forms.NumberInput(attrs={'placeholder': 'Введите баллы для WeatherTech'}),
            'virginia': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Virginia'}),
            'atlanta': forms.NumberInput(attrs={'placeholder': 'Введите баллы для Atlanta'}),
        }