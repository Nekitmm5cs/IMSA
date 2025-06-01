from django.contrib import admin
from .models import MediaItem  # Измените GalleryImage на MediaItem

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_at')
    list_filter = ('media_type',)
    search_fields = ('title', 'description')