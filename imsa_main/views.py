from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Главная страница
def main(request):
    if request.user.is_authenticated:
        return render(request, 'imsa_main/main.html', {'user_authenticated': True})
    return render(request, 'imsa_main/main.html', {'user_authenticated': False})
