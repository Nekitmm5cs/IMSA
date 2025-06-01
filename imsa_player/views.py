from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def player(request):
    return render(request, 'imsa_player/player.html')