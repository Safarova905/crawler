import os
from bs4 import BeautifulSoup   # для разбора html     # pip install bs4
import requests                 # для доступа к сайту  # pip install import requests


class Content:
    def __init__(self, url, title, body):
        self.url   = url
        self.title = title
        self.body  = body


def get_page(url):
    req = requests.get(url)

    if req.status_code == 200:
        return BeautifulSoup(req.text, 'html.parser')
    return None

def news_form_lenta(url):
    bs = get_page(url)
    if bs is None:
        return bs
    titleBs = bs.find("title")
    if titleBs:
        title = titleBs.text
    else: title = ' '
    lines = bs.find_all("p")
    body  = '\n'.join([line.text.strip() for line in lines])
    return Content(url, title, body)


#content = news_form_lenta('https://lenta.ru/news/2019/10/17/competition/')
# или
for i in range(1,101):

    content = news_form_lenta('https://libcat.ru/knigi/fantastika-i-fjentezi/boevaya-fantastika/392345-%i-oleg-danilchenko-imperskij-voyazh-1-4.html#text' %i)
    if content is None:
        print("Ошибка!")
    else:
        with open('fileOutput%i.txt' %i, 'w', encoding='utf-8') as f:
            print("Заголовок: {}".format(content.title), file=f)
            print("\nАдрес    : {}\n".format(content.url), file=f)
            print(content.body, file=f)
    print('fileOutput%i.txt' %i, '-', 'https://libcat.ru/knigi/fantastika-i-fjentezi/boevaya-fantastika/392345-%i-oleg-danilchenko-imperskij-voyazh-1-4.html#text' %i)

