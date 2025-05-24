from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GalleryImage
from .forms import GalleryImageForm
 
 # Функция для отображения галереи
def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'imsa_gallery/gallery.html', {'images': images})
 
 # Функция для загрузки изображений
@login_required
def upload_image(request):
    if request.user.username != "root":
        return redirect('gallery')  # Перенаправляем на галерею, если это не root
 
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'imsa_gallery/upload_image.html', {'form': form})