import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render

from bs4 import BeautifulSoup
import requests

def parse_sportscar365_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    base_url = 'https://sportscar365.com'
    url = f'{base_url}/category/imsa/'
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all('li', class_='mvp-blog-story-wrap')[:10]  # Ограничиваем 10 новостями
        
        news_list = []
        
        for item in news_items:
            try:
                # Основные данные с главной страницы
                title = item.find('h2').get_text(strip=True)
                relative_url = item.find('h2').a['href']
                full_url = f"{base_url}{relative_url}" if relative_url.startswith('/') else relative_url
                
                # Получаем полный текст статьи
                article_content = get_article_content(full_url, headers)
                
                # Продолжаем парсинг основной информации
                category = item.find('h3').get_text(strip=True) if item.find('h3') else ''
                date = item.find('span', class_='mvp-post-info-date').get_text(strip=True) if item.find('span', class_='mvp-post-info-date') else ''
                
                img = item.find('img', class_='mvp-reg-img')
                img_url = img['src'] if img else ''
                
                author = item.find('span', class_='mvp-blog-story-author').get_text(strip=True) if item.find('span', class_='mvp-blog-story-author') else ''
                
                news_list.append({
                    'title': title,
                    'url': full_url,
                    'category': category,
                    'date': date,
                    'image': img_url,
                    'excerpt': article_content.get('excerpt', ''),
                    'content': article_content.get('content', ''),
                    'author': author
                })
                
            except Exception as e:
                print(f"Ошибка парсинга элемента: {e}")
                continue
                
        return news_list
        
    except Exception as e:
        print(f"Ошибка при запросе к сайту: {e}")
        return []

def get_article_content(article_url, headers):
    """Получает полный текст статьи"""
    try:
        response = requests.get(article_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Извлекаем первый абзац (excerpt)
        excerpt = soup.find('div', class_='entry-content').find('p').get_text(strip=True) if soup.find('div', class_='entry-content') else ''
        
        # Извлекаем все абзацы содержания
        content_paragraphs = []
        entry_content = soup.find('div', class_='entry-content')
        if entry_content:
            for p in entry_content.find_all('p'):
                text = p.get_text(strip=True)
                if text:  # Игнорируем пустые абзацы
                    content_paragraphs.append(f"<p>{text}</p>")
        
        return {
            'excerpt': excerpt,
            'content': ' '.join(content_paragraphs) if content_paragraphs else ''
        }
        
    except Exception as e:
        print(f"Ошибка при парсинге статьи {article_url}: {e}")
        return {'excerpt': '', 'content': ''}

# Пример использования в Django View
def news_list(request):
    news = parse_sportscar365_news()
    return render(request, 'news/index.html', {'news': news})