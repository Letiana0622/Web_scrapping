
import bs4
import requests
import re

from fake_useragent import UserAgent

def web_scrapping():
    for n in range(1,8):
        # ua = UserAgent()
        # print(ua.chrome)
        # header = {'User-Agent': str(ua.chrome)}
        # print(header)
        # url = 'https://habr.com/ru/all/'
        KEY_WORDS = ['IT-команда','Agile']
        # url = 'https://tproger.ru/'
        url = f'https://tproger.ru/page/{n}/'
        response = requests.get(url)
        # print(type(response))
        text = response.text
        # print(text)
        soup = bs4.BeautifulSoup(text, features='html.parser')
        articles = soup.find_all('article')
        for article in articles:
            hubs = article.find_all(class_='article__container-title')
            # print(hubs)
            # hubs = article.find_all(class_='tm-article-snippet__hubs-item')
            hubs = [hub.text.strip() for hub in hubs]
            # print(hubs)
            # print(href)
            for hub in hubs:
                result = re.split('\s', hub)
                # print(result)
                for word in result:
                    if word in KEY_WORDS:
                        # print('!!!!!!!!!!!!!!!!!!!!')
                        print(f'Title of news  - {hub}')
                        href = article.find(class_='article__link').attrs['href']
                        print(f'Link to news {href}')
                        views = article.find(class_='meta__views article__container-views').find('span').text
                        print(f'Number of views {views}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    web_scrapping()
