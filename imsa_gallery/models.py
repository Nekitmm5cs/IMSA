from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MediaItem(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Изображение'),
        ('video', 'Видео'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    file = models.FileField(upload_to='gallery/', verbose_name="Файл")
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        verbose_name="Тип медиа"
    )
    uploaded_at = models.DateTimeField(default=timezone.now, verbose_name="Дата загрузки")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Загрузил")

    def __str__(self):
        return self.title

    def is_image(self):
        return self.media_type == 'image'