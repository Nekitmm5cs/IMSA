from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imsa_main.urls')),   
    path('test/', include('imsa_test.urls')),   
<<<<<<< HEAD
    path('table/', include('imsa_table.urls')),   
    # path('news/', include('imsa_news.urls')),  
    path('users/', include('imsa_users.urls')),  
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    # path('news/', include('imsa_news.urls')),  
    path('users/', include('imsa_users.urls')),  
 ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 7f248e54c694e3d81703bac3bd833786ee3589b0
