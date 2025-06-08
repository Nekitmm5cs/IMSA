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

@csrf_exempt
@login_required
def get_messages(request):
    messages = ChatMessage.objects.order_by('-timestamp')[:50]
    messages_data = [{
        'user_id': msg.user.id,
        'username': msg.user.username,
        'message': msg.message
    } for msg in messages]
    return JsonResponse({'messages': messages_data[::-1]})  # Reverse to show oldest first

def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        message = data.get('message')
        
        if user.is_authenticated and message:
            ChatMessage.objects.create(user=user, message=message)
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)



