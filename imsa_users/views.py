from django.shortcuts import render

def login(request):
    return render(request, "imsa_users/login.html")

def register(request):
    return render(request, "imsa_users/register.html")
