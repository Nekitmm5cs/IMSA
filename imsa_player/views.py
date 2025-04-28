from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team, TeamMember, TeamVacancy, TeamApplication, TournamentRegistration
from .forms import TeamForm, TeamVacancyForm, TeamApplicationForm, TournamentRegistrationForm

@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save(commit=False)
            team.owner = request.user
            team.save()
            
            # Автоматически добавляем владельца как участника команды
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
    
    return render(request, 'imsa_player/create_team.html', {'form': form})

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    is_owner = team.owner == request.user
    is_member = TeamMember.objects.filter(team=team, user=request.user, is_confirmed=True).exists()
    
    if not (is_owner or is_member or request.user.is_staff):
        messages.error(request, 'У вас нет доступа к этой команде')
        return redirect('my_teams')
    
    members = team.members.filter(is_confirmed=True)
    vacancies = team.vacancies.filter(is_active=True)
    applications = team.applications.filter(status='PENDING')
    registrations = team.registrations.all()
    
    context = {
        'team': team,
        'members': members,
        'vacancies': vacancies,
        'applications': applications,
        'registrations': registrations,
        'is_owner': is_owner,
    }
    
    return render(request, 'imsa_player/team_detail.html', context)

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
    
    return render(request, 'imsa_player/create_vacancy.html', {'form': form, 'team': team})

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
    
    return render(request, 'imsa_player/apply_for_vacancy.html', {'form': form, 'vacancy': vacancy})

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
    
    return render(request, 'imsa_player/register_for_tournament.html', {'form': form, 'team': team})

@login_required
def my_teams(request):
    owned_teams = Team.objects.filter(owner=request.user)
    member_teams = Team.objects.filter(members__user=request.user, members__is_confirmed=True)
    
    context = {
        'owned_teams': owned_teams,
        'member_teams': member_teams,
    }
    
    return render(request, 'imsa_player/my_teams.html', context)

@login_required
def player(request):
    return render(request, 'imsa_player/player.html')