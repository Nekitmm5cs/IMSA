from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Представление для логина
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)  # Логиним пользователя
            return redirect('main')  # Перенаправление на главную страницу
        else:
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'imsa_users/login.html')

# Представление для регистрации
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Аккаунт успешно создан')
            return redirect('login')  # Перенаправление на страницу логина
    return render(request, 'imsa_users/register.html')

# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('main')  # Перенаправление на главную страницу после выхода

@login_required
def profile(request):
    return render(request, 'imsa_users/profile.html')
