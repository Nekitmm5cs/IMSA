from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    search_fields = ('title', 'excerpt')
    list_filter = ('date',)