from django.shortcuts import render, redirect
from .forms import MediaItemForm
from .models import MediaItem

def gallery(request):
    media_items = MediaItem.objects.all().order_by('-uploaded_at')
    return render(request, 'imsa_gallery/gallery.html', {'media_items': media_items})

def upload_media(request):
    if not request.user.is_authenticated or request.user.username != "root":
        return redirect('gallery')
    
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = MediaItemForm(user=request.user)
    
    return render(request, 'imsa_gallery/upload_media.html', {'form': form})