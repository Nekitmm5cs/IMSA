from django.urls import path
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from . import views, consumers

urlpatterns = [
    path('', views.main, name='main'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'), 
]


