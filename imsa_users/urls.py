from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('create_team/', views.create_team, name='create_team'),  # Эта строка должна быть
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/<int:team_id>/vacancy/create/', views.create_vacancy, name='create_vacancy'),
    path('vacancy/<int:vacancy_id>/apply/', views.apply_for_vacancy, name='apply_for_vacancy'),
    path('application/<int:application_id>/<str:action>/', views.process_application, name='process_application'),
    path('teams/<int:team_id>/register/', views.register_for_tournament, name='register_for_tournament'),
    path('my-teams/', views.my_teams, name='my_teams'),
]