from django.db import models
from django.utils import timezone

class NewsArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    url = models.URLField(verbose_name="Ссылка на статью")
    excerpt = models.TextField(blank=True, verbose_name="Краткое содержание")
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    image_url = models.URLField(blank=True, verbose_name="Ссылка на изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")

    class Meta:
        verbose_name = "Новость IMSA"
        verbose_name_plural = "Новости IMSA"
        ordering = ['-date']

    def __str__(self):
        return self.title