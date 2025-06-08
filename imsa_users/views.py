from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from .forms import TeamForm, TeamVacancyForm, TeamApplicationForm, TournamentRegistrationForm
from .models import Team, TeamMember, TeamVacancy, TeamApplication
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
            send_mail(subject='Регистрация',message='Вы успешно зарагестрированы!',from_email='imsa02657@gmail.com', recipient_list=[email], fail_silently=False)
            return redirect('login')  # Перенаправление на страницу логина
    return render(request, 'imsa_users/register.html')

# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('main')  # Перенаправление на главную страницу после выхода

@login_required
def profile(request):
    return render(request, 'imsa_users/profile.html')

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    is_owner = team.owner == request.user
    is_member = TeamMember.objects.filter(team=team, user=request.user, is_confirmed=True).exists()
    
    if not (is_owner or is_member or request.user.is_staff):
        messages.error(request, 'У вас нет доступа к этой команде')
        return redirect('my_teams')
    
    context = {
        'team': team,
        'members': team.members.filter(is_confirmed=True),
        'vacancies': team.vacancies.filter(is_active=True),
        'applications': team.applications.filter(status='PENDING'),
        'registrations': team.registrations.all(),
        'is_owner': is_owner,
    }
    return render(request, 'imsa_users/team_detail.html', context)


@login_required
def create_vacancy(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    
    if team.owner != request.user:
        messages.error(request, 'Только владелец команды может создавать вакансии')
        return redirect('team_detail', team_id=team.id)
    
    if request.method == 'POST':
        form = TeamVacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.team = team
            vacancy.save()
            messages.success(request, 'Вакансия успешно создана!')
            return redirect('team_detail', team_id=team.id)
    else:
        form = TeamVacancyForm()
    return render(request, 'imsa_users/create_vacancy.html', {'form': form, 'team': team})


@login_required
def apply_for_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(TeamVacancy, id=vacancy_id, is_active=True)
    
    if TeamMember.objects.filter(team=vacancy.team, user=request.user).exists():
        messages.error(request, 'Вы уже состоите в этой команде')
        return redirect('team_detail', team_id=vacancy.team.id)
    
    if TeamApplication.objects.filter(vacancy=vacancy, user=request.user).exists():
        messages.error(request, 'Вы уже подавали заявку на эту вакансию')
        return redirect('team_detail', team_id=vacancy.team.id)
    
    if request.method == 'POST':
        form = TeamApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.team = vacancy.team
            application.user = request.user
            application.vacancy = vacancy
            application.save()
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('team_detail', team_id=vacancy.team.id)
    else:
        form = TeamApplicationForm()
    return render(request, 'imsa_users/apply_for_vacancy.html', {'form': form, 'vacancy': vacancy})


@login_required
def process_application(request, application_id, action):
    application = get_object_or_404(TeamApplication, id=application_id)
    
    if application.team.owner != request.user:
        messages.error(request, 'Только владелец команды может обрабатывать заявки')
        return redirect('team_detail', team_id=application.team.id)
    
    if application.status != 'PENDING':
        messages.error(request, 'Эта заявка уже была обработана')
        return redirect('team_detail', team_id=application.team.id)
    
    if action == 'approve':
        application.status = 'APPROVED'
        TeamMember.objects.create(
            team=application.team,
            user=application.user,
            role=application.vacancy.role,
            is_confirmed=True
        )
        messages.success(request, 'Заявка одобрена, участник добавлен в команду')
    elif action == 'reject':
        application.status = 'REJECTED'
        messages.success(request, 'Заявка отклонена')
    
    application.processed_at = timezone.now()
    application.save()
    return redirect('team_detail', team_id=application.team.id)


@login_required
def register_for_tournament(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    
    if team.owner != request.user:
        messages.error(request, 'Только владелец команды может регистрировать команду на турнир')
        return redirect('team_detail', team_id=team.id)
    
    if not team.is_approved:
        messages.error(request, 'Ваша команда еще не подтверждена администрацией')
        return redirect('team_detail', team_id=team.id)
    
    if request.method == 'POST':
        form = TournamentRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.team = team
            registration.save()
            messages.success(request, 'Заявка на участие в турнире отправлена!')
            return redirect('team_detail', team_id=team.id)
    else:
        form = TournamentRegistrationForm()
    return render(request, 'imsa_users/register_for_tournament.html', {'form': form, 'team': team})


@login_required
def my_teams(request):
    context = {
        'owned_teams': Team.objects.filter(owner=request.user),
        'member_teams': Team.objects.filter(members__user=request.user, members__is_confirmed=True),
    }
    return render(request, 'imsa_users/my_teams.html', context)


@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save(commit=False)
            team.owner = request.user
            team.save()
            
            TeamMember.objects.create(
                team=team,
                user=request.user,
                role='MANAGER',
                is_confirmed=True
            )
            
            messages.success(request, 'Команда успешно создана! Ожидайте подтверждения администрацией.')
            return redirect('team_detail', team_id=team.id)
    else:
        form = TeamForm()
    return render(request, 'imsa_users/create_team.html', {'form': form})