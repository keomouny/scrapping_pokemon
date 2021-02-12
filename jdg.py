from bs4 import BeautifulSoup
import requests
import os
from pprint import pprint
from setup_logger import logger


class JDG:

    def __init__(self):
        self.request_data_site = requests.get('https://www.journaldugeek.com')
        self.soup = BeautifulSoup(
            self.request_data_site.content, 'html.parser')

        # print(soup.prettify())

    def get_data(self, listData):
        logger.info(f'Create data {listData}')
        list_actuality = []
        for key, value in enumerate(listData):
            dict_article = {}
            dict_article['images'] = listData[key].find(
                'img', {'class': 'entry__img'})['data-srcset'].split(' ,')[0]
            dict_article['title'] = listData[key].find(
                'h3', {'class': 'entry__title'}).text.strip()
            try:
                dict_article['categories'] = listData[key].find(
                    'span', {'class': 'entry__category'}).get_text().replace('\t', '').replace('\n', '')
            except:
                dict_article['categories'] = None

            list_actuality.append(dict_article)
            dict_article = {}
        return list_actuality

    def convert_data_for_query(self, listData, str_query):
        if len(listData):
            my_list = listData[-1]
            # print(my_list, end='\r')
            new_list_data = listData[:-1]
            str_query = f"{str_query} ('{listData[-1]['images']}', '{listData[-1]['title']}', '{listData[-1]['categories']}')"
            str_query += ', ' if len(listData) != 1 else ';'
            return self.convert_data_for_query(new_list_data, str_query)
        return str_query
