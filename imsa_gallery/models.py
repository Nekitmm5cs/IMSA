from django.db import models
from django.contrib.auth.models import User

class MediaItem(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Изображение'),
        ('video', 'Видео'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    file = models.FileField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def is_image(self):
        return self.media_type == 'image'
    
    def is_video(self):
        return self.media_type == 'video'