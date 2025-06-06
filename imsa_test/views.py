from django.shortcuts import render

def test(request):
    return render(request, 'imsa_test/test.html')

