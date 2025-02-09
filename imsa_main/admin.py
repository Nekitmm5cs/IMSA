from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('message',)
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        queryset.delete()
    delete_selected.short_description = "Delete selected messages"