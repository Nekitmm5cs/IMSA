from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'daytona', 'sebring', 'weathertech', 'virginia', 'atlanta', 'total')
    list_filter = ('car',)
    search_fields = ('name',)
    ordering = ('-total',)

admin.site.register(Participant, ParticipantAdmin)