# imsa_gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('upload/', views.upload_image, name='upload_image'),
]