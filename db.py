import mysql.connector
from setup_logger import logger
from jdg import pprint


class DB:
    def __init__(self):
        self.myconn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            auth_plugin="mysql_native_password",
            database="db_simplon_test"
        )
        self.db_name = 'db_simplon_test'
        self.query_specify = None

    def create_db(self):
        self.query_specify = f'CREATE DATABASE IF NOT EXISTS {self.db_name};'

    def create_table(self):
        self.query_specify = f'use {self.db_name}; CREATE TABLE IF NOT EXISTS articles (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, image VARCHAR(100), title VARCHAR(100), categorie VARCHAR(100));'

    def insert_data(self, query_plus):
        try:
            self.mycursor = self.myconn.cursor()
            self.query_specify = 'INSERT INTO articles (image, title, categorie) VALUES (%s, %s, %s)'
            self.mycursor.executemany(self.query_specify, query_plus)
            self.myconn.commit()
        except mysql.connector.Error as err:
            print(err)
            exit()

    def select_from_db(self):
        self.mycursor = self.myconn.cursor()
        self.query_specify = 'SELECT * FROM departement'
        self.mycursor.execute(self.query_specify)
        result = self.mycursor.fetchall()
        for i in result:
            print(i)

    def __disconnect__(self):
        self.myconn.close()

    def execute_query(self, callback_func):
        try:
            self.mycursor = self.myconn.cursor()
            callback_func()
            self.mycursor.execute(self.query_specify, multi=True)
            self.myconn.commit()
        except mysql.connector.Error as err:
            print(err)
            exit()
