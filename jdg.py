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
            list_article = []
            list_article.append(listData[key].find(
                'img', {'class': 'entry__img'})['data-srcset'].split(' ,')[0])
            list_article.append(listData[key].find(
                'h3', {'class': 'entry__title'}).get_text(strip=True, separator=',').replace('\xa0', ' '))
            try:
                list_article.append(listData[key].find(
                    'span', {'class': 'entry__category'}).get_text(strip=True, separator=','))
            except:
                list_article.append(None)

            list_actuality.append(tuple(list_article))
            list_article = []
        return list_actuality

    # def convert_data_for_query(self, listData, str_query):
    #     if len(listData):
    #         my_list = listData[0]
    #         new_list_data = listData[1:]
    #         str_query = f"{str_query} ('{listData[0]['images']}', '{listData[0]['title']}', '{listData[0]['categories']}')"
    #         str_query += ', ' if len(listData) != 1 else ';'
    #         return self.convert_data_for_query(new_list_data, str_query)
    #     return str_query
