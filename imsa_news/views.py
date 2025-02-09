from django.http import JsonResponse
from .models import News

def load_more_news(request):
    start = int(request.GET.get('start', 0))
    news = News.objects.all()[start:start+5]  # Получаем новости начиная с позиции 'start'

    news_data = []
    for item in news:
        news_data.append({
            'title': item.title,
            'link': item.link,
            'image': item.image.url,  # Путь к изображению
            'heading3': item.heading3,
            'heading2': item.heading2,
            'pading': item.pading,
            'author': item.author,
            'author_link': item.author_link
        })
    
    # Определяем, есть ли еще новости для подгрузки
    more_news = len(news) == 5
    
    return JsonResponse({
        'news': news_data,
        'more_news': more_news  # Если новостей больше нет, возвращаем False
    })

