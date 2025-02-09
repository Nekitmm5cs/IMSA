from django.shortcuts import render
from .models import RaceParticipant

def table(request):
    participants = RaceParticipant.objects.all()
    return render(request, 'imsa_table/table.html', {'participants': participants, 'user': request.user})