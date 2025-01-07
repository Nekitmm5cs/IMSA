from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imsa_main.urls')),  # Главная страница
    path('news/', include('imsa_news.urls')),  # Новости
    path('users/', include('imsa_users.urls')),  # Пользователи
 ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
