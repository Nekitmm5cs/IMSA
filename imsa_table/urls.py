from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.table, name='table'),
    path('edit/<int:participant_id>/', views.edit_participant, name='edit_participant'),
    path('delete/<int:participant_id>/', views.delete_participant, name='delete_participant'),
]