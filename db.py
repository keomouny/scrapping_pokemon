import mysql.connector
from setup_logger import logger
from pokemon import pprint
import time
import os
from dotenv import load_dotenv


class DB:
    logger.info('instance of db class')

    def __init__(self):
        time.sleep(1)
        load_dotenv()
        logger.info('connect to database')
        self.db_name = os.environ.get('MSQL_DBNAME')
        self.myconn = mysql.connector.connect(
            host=os.environ.get('MSQL_HOST'),
            user=os.environ.get('MSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            port=3306,
            auth_plugin="mysql_native_password",
            database=self.db_name
        )
        self.query_specify = None
        self.dict_query = {
            'header_articles': {
                'create_table': 'CREATE TABLE IF NOT EXISTS header_articles (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, title VARCHAR(100), image VARCHAR(500));',
                'insert_into': 'INSERT INTO header_articles (title, image) VALUES (%s, %s)'
            },
            'all_news': {
                'create_table': 'CREATE TABLE IF NOT EXISTS all_news (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, title VARCHAR(100), description TEXT, nb_commentary int, author TEXT, image VARCHAR(500));',
                'insert_into': 'INSERT INTO all_news (title, description, nb_commentary, author, image) VALUES (%s, %s, %s, %s, %s)'},
            'all_posts': {
                'create_table': 'CREATE TABLE IF NOT EXISTS all_posts (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, title VARCHAR(100), nb_commentary int, image VARCHAR(500));',
                'insert_into': 'INSERT INTO all_posts (title, nb_commentary, image) VALUES (%s, %s, %s)'}
        }

    def create_db(self):
        logger.info(f'create database {self.db_name}')
        self.query_specify = f'CREATE DATABASE IF NOT EXISTS {self.db_name} CHARACTER SET utf8;'

    def create_table(self, query):
        logger.info(f'create table {query}')
        self.query_specify = self.dict_query[query]['create_table']

    def delete_table(self, query):
        logger.info(f'delete table {query}')
        self.query_specify = f'DROP table {query};'

    def delete_data(self, query):
        logger.info(f'delete data from table {query}')
        self.query_specify = f'DELETE from {query};'

    def insert_data(self, query, query_plus):
        logger.info(f'insert data from table {query}')
        self.query_specify = self.dict_query[query]['insert_into']
        try:
            self.mycursor = self.myconn.cursor()
            self.mycursor.executemany(self.query_specify, query_plus)
        except mysql.connector.Error as err:
            logger.error(err)
            exit()

    def select_from_db(self, tablename):
        logger.info(f'select all data from {tablename}')
        self.mycursor = self.myconn.cursor(dictionary=True)
        self.query_specify = f'SELECT * FROM {tablename};'
        self.mycursor.execute(self.query_specify)
        result = self.mycursor.fetchall()
        return result

    def __disconnect__(self):
        logger.info('disconnect from database')
        self.myconn.commit()
        self.myconn.close()

    def execute_query(self, callback_func, query):
        logger.info(f'execute query {callback_func}')
        try:
            self.mycursor = self.myconn.cursor()
            callback_func(query)
            self.mycursor.execute(self.query_specify)
        except mysql.connector.Error as err:
            logger.error(err)
            exit()
