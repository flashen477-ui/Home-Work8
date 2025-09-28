import requests
from bs4 import BeautifulSoup

class WebPageScraper:
    def __init__(self, url):
        self.url = url

    def scrape_tag(self, tag="title"):
        try:
            responce = requests.get(self.url)
            responce.raise_for_status()
            soup = BeautifulSoup(responce.text, 'html.parser')
            my_tags = soup.select(tag)
            return [my_tag.text for my_tag in my_tags]
        except Exception as e:
            print(f"Помилка: {e}")
            return []

    def scrape_class(self, class_name):
        try:
            responce = requests.get(self.url)
            responce.raise_for_status()
            soup = BeautifulSoup(responce.text, 'html.parser')
            my_tags = soup.find_all(class_=class_name)
            return [my_tag.text for my_tag in my_tags]
        except Exception as e:
            print(f"Помилка: {e}")
            return []

url = 'https://epicentrk.ua/ua/shop/smartfony-i-mobilnye-telefony/'
scraper = WebPageScraper(url)

title = scraper.scrape_tag('title')
print(f'Назва сторінки: {title}')

heading = scraper.scrape_tag('h1')
print(f'Головний заголовок сторінки: {heading}')

class_name = '_jFNyPKOC'
elements = scraper.scrape_class(class_name)
print(f'Елементи з класом {class_name}: {elements}')