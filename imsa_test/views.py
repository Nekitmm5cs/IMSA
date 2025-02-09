from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def test(request):
    return render(request, 'imsa_test/test.html')

def test2(request):
    return render(request, 'imsa_test/test2.html')

def test3(request):
    return render(request, 'imsa_test/test3.html')

def test4(request):
    return render(request, 'imsa_test/test4.html')

def test5(request):
    return render(request, 'imsa_test/test5.html')
