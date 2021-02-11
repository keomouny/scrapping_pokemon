from bs4 import BeautifulSoup
import requests
import os
from pprint import pprint

url = 'https://www.journaldugeek.com'
request_data_site = requests.get(url)
soup = BeautifulSoup(request_data_site.content, 'html.parser')

# print(soup.prettify())


def get_data(listData):
    list_actuality = []
    for key, value in enumerate(listData):
        dict_article = {}
        # print(key, value)
        dict_article['images'] = listData[key].find(
            'img', {'class': 'entry__img'})['data-srcset'].split(' ,')[0]
        dict_article['title'] = listData[key].find(
            'h3', {'class': 'entry__title'}).text.strip()
        if listData[key].find('span', {'class': 'entry__category'}):
            dict_article['categories'] = listData[key].find(
                'span', {'class': 'entry__category'}).get_text().replace('\t', '').replace('\n', '')
        else:
            dict_article['categories'] = None
        list_actuality.append(dict_article)
        dict_article = {}
    return list_actuality


# List actuality :
entry_item_article = soup.find_all('div', {'class': 'entry__item'})
list_actuality = get_data(entry_item_article)


# List article à la une
entry_item_une = soup.find('div', {
                           'class': 'entry__grid-container'}).findChildren('div', {'class': 'entry__item'})
list_Une = get_data(entry_item_une)
# pprint(list_Une)
