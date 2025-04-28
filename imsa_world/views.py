from django.shortcuts import render

def world(request):
    return render(request, 'imsa_world/world.html')