from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def schedule(request):
    return render(request, 'imsa_schedule/schedule.html')

