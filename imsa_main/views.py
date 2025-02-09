from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import json

# Главная страница
def main(request):
    if request.user.is_authenticated:
        return render(request, 'imsa_main/main.html', {'user_authenticated': True})
    return render(request, 'imsa_main/main.html', {'user_authenticated': False})

def map(request):
    return render(request, 'imsa_main/imsa_map.html')

@csrf_exempt
@login_required
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        user = request.user
        ChatMessage.objects.create(user=user, message=message)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def get_messages(request):
    messages = ChatMessage.objects.all().order_by('timestamp')[:50]
    messages_data = [{'username': msg.user.username, 'message': msg.message} for msg in messages]
    return JsonResponse({'messages': messages_data})

