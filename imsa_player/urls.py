from django.urls import path
from . import views

urlpatterns = [
    path('', views.player, name='player'),
    path('create-team/', views.create_team, name='create_team'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('team/<int:team_id>/create-vacancy/', views.create_vacancy, name='create_vacancy'),
    path('vacancy/<int:vacancy_id>/apply/', views.apply_for_vacancy, name='apply_for_vacancy'),
    path('application/<int:application_id>/<str:action>/', views.process_application, name='process_application'),
    path('team/<int:team_id>/register/', views.register_for_tournament, name='register_for_tournament'),
    path('my-teams/', views.my_teams, name='my_teams'),
]