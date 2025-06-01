from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MediaItem
from .forms import MediaItemForm



def gallery(request):
    media_items = MediaItem.objects.all().order_by('-uploaded_at')
    return render(request, 'imsa_gallery/gallery.html', {'media_items': media_items})

@login_required
def upload_media(request):  # Обратите внимание на имя функции - upload_media
    if not request.user.username == "root":
        return redirect('gallery')
    
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = MediaItemForm(user=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'imsa_gallery/upload_media.html', context)