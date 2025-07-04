from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imsa_main.urls')),   
    path('test/', include('imsa_test.urls')),   
    path('table/', include('imsa_table.urls')),  
    path('gallery/', include('imsa_gallery.urls')),
    path('schedule/', include('imsa_schedule.urls')),
    path('world/', include('imsa_world.urls')),
    path('player/', include('imsa_player.urls')),
    path('news/', include('imsa_news.urls')),  
    path('users/', include('imsa_users.urls')),  
]

# This is for development only - serves both static and media files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)