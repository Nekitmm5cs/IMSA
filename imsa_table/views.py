from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Participant
from .forms import ParticipantForm

def table(request):
    if request.method == 'POST' and request.user.username == "root":
        name = request.POST.get('name')
        car = request.POST.get('car')
        daytona = float(request.POST.get('daytona', 0))
        sebring = float(request.POST.get('sebring', 0))
        weathertech = float(request.POST.get('weathertech', 0))
        virginia = float(request.POST.get('virginia', 0))
        atlanta = float(request.POST.get('atlanta', 0))
        
        Participant.objects.create(
            name=name,
            car=car,
            daytona=daytona,
            sebring=sebring,
            weathertech=weathertech,
            virginia=virginia,
            atlanta=atlanta
        )
        return redirect('table')
    
    participants = Participant.objects.all()
    return render(request, 'imsa_table/table.html', {'participants': participants})

@login_required
def edit_participant(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    if not request.user.is_staff and request.user.username != "root":
        return redirect('table')

    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'imsa_table/edit_participant.html', {'form': form})

@login_required
def delete_participant(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    if not request.user.is_staff and request.user.username != "root":
        return redirect('table')

    participant.delete()
    return redirect('table')