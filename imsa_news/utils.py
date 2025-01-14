# import requests
# from bs4 import BeautifulSoup as BS

# url = 'https://sportscar365.com/'

# # Заголовки для подражания браузеру
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# # Функция для парсинга новостей
# def parse_news(start=0, limit=5):
#     response = requests.get(url, headers=headers)
#     news_data = []

#     if response.status_code == 200:
#         html = BS(response.content, 'html.parser')
#         blog_section = html.select('ul.mvp-main-blog-wrap.left.relative.infinite-content')

#         if blog_section:
#             for el in blog_section[0].find_all('li')[start:start+limit]:  # Считываем новости с позиции start
#                 title = el.select('a')
#                 image = el.select('img')
#                 heading2 = el.select('h2')
#                 heading3 = el.select('h3')
#                 paragraph = el.select('p')
#                 author_span = el.select('span.mvp-blog-story-author a')

#                 if title and image:
#                     news_item = {
#                         'title': title[0].text.strip(),
#                         'link': title[0]['href'],
#                         'image': image[0]['src'],
#                         'heading2': heading2[0].text.strip() if heading2 else '',
#                         'heading3': heading3[0].text.strip() if heading3 else '',
#                         'pading': paragraph[0].text.strip() if paragraph else '',
#                         'author': author_span[0].text.strip() if author_span else '',
#                         'author_link': author_span[0]['href'] if author_span else ''
#                     }
#                     news_data.append(news_item)
#         return news_data
#     else:
#         return []