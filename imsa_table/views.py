from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RaceParticipant
from .forms import RaceParticipantForm

def table(request):
    if request.method == 'POST' and request.user.username == "root":
        form = RaceParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = RaceParticipantForm()

    participants = RaceParticipant.objects.all().order_by('-total')
    return render(request, 'imsa_table/table.html', {'participants': participants, 'user': request.user, 'form': form})

@login_required
def edit_participant(request, participant_id):
    participant = get_object_or_404(RaceParticipant, id=participant_id)
    if not request.user.is_staff and request.user.username != "root":
        return redirect('table')

    if request.method == 'POST':
        form = RaceParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = RaceParticipantForm(instance=participant)
    return render(request, 'imsa_table/edit_participant.html', {'form': form})

@login_required
def delete_participant(request, participant_id):
    participant = get_object_or_404(RaceParticipant, id=participant_id)
    if not request.user.is_staff and request.user.username != "root":
        return redirect('table')

    participant.delete()
    return redirect('table')