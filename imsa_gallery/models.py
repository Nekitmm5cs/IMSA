# imsa_gallery/models.py
from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to='gallery/', verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"