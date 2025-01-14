import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Парсит новости с сайта IMSA'

    def handle(self, *args, **kwargs):
        # Ссылка на новости
        url = 'https://www.imsa.com/weathertech/latestnews/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Парсим все новости
        news_items = soup.select('.card-news-content')  # Этот CSS-класс соответствует карточкам новостей
        news_data = []

        for item in news_items:
            title = item.select_one('.card-news-title').text.strip() if item.select_one('.card-news-title') else ''
            description = item.select_one('.card-news-excerpt').text.strip() if item.select_one('.card-news-excerpt') else ''
            published_at = item.select_one('.card-news-date').text.strip() if item.select_one('.card-news-date') else ''
            url = item.select_one('a')['href'] if item.select_one('a') else ''

            # Добавляем новость в список
            news_data.append({
                'title': title,
                'description': description,
                'published_at': published_at,
                'url': url
            })

        # Выводим данные в консоль
        for news in news_data:
            self.stdout.write(f"Title: {news['title']}, Published at: {news['published_at']}")

        # Возвращаем список новостей
        return news_data
