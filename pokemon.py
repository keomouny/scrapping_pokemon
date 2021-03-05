from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import os
from pprint import pprint
from setup_logger import logger


class pokemon:

    def __init__(self):
        logger.info('instanciation class pokemon')
        self.url_site = 'https://www.pokemontrash.com'
        self.request_data_site2 = Request(
            self.url_site, headers={'User-Agent': 'Mozilla/5.0'})
        self.request_data_site1 = urlopen(self.request_data_site2).read()
        self.soup = BeautifulSoup(self.request_data_site1, 'html.parser')
        self.scrap_type = self.scrap_element()

    message = 'hello world'

    def scrap_element(self):
        dict_query = {
            "header_articles": ['a', 'header-article', self.get_article_header, 'header_articles.html'],
            "all_news": ['li', 'post', self.get_all_news, 'all_news.html'],
            "all_posts": ['div', 'mur-item', self.get_all_post_aside, 'all_posts.html']
        }
        return dict_query

    def get_scrap_data(self, callback_func, query):
        return callback_func(query)

    def scrap_data(self, query):
        data = self.soup.find_all(self.scrap_type[query][0], {
            'class': self.scrap_type[query][1]})
        return self.get_scrap_data(self.scrap_type[query][2], data)

    def get_article_header(self, listData):
        logger.info('create data articles header')
        list_articles = []
        for key, value in enumerate(listData):
            article = []
            try:
                article.append(listData[key].find('span').get_text())
                article.append(listData[key]['style'].replace(
                    'background-image:url(//www.pokemontrash.com', self.url_site).replace(')', ''))
                list_articles.append(tuple(article))
            except:
                pass
        print(list_articles)
        return list_articles

    def get_all_news(self, listData):
        logger.info('create data news')
        list_news = []
        for key, value in enumerate(listData):
            news = []
            try:
                news.append(listData[key].find('h3').get_text())
                news.append(listData[key].find(
                    'p').get_text(strip=True).split(' @')[0])
                news.append(listData[key].find(
                    'div', {'class': 'post-count'}).get_text())
                news.append(listData[key].find(
                    'p').get_text(strip=True).split('@')[1])
                news.append(listData[key].find('div', {'class': 'post-thumb'})[
                            'style'].replace('background-image:url(', self.url_site).replace(');', ''))
                list_news.append(tuple(news))
            except:
                pass
        return list_news

    def get_all_post_aside(self, listData):
        logger.info('create data post aside')
        list_posts = []
        for key, value in enumerate(listData):
            post = []
            try:
                post.append(listData[key].find(
                    'span', {'class': 'mur-title'}).get_text())
                post.append(listData[key].find(
                    'div', {'class': 'mur-top'}).get_text())
                post.append(self.url_site + listData[key].find(
                    'span', {'class': 'mur-thumb'})['style'].split('(')[1].split(')')[0])
                list_posts.append(tuple(post))
            except:
                pass
        return list_posts
