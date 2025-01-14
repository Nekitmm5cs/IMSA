from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news, name='news'),
    path('load-more-news/', views.load_more_news, name='load_more_news'),  # URL для подгрузки новостей
]
