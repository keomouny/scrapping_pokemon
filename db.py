import sqlite3
from setup_logger import logger


def create_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    SQL_DELETE = """DROP TABLE IF EXISTS articles;"""
    SQL_STATEMENT = """CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT, image text, title text NOT NULL, categorie text, description text);"""

    c.execute(SQL_DELETE)
    c.execute(SQL_STATEMENT)

    conn.commit()
    conn.close()


# Insert some users into our database
def insert_db(query):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(query)
    # c.execute(
    #     """INSERT INTO articles (image, title, categorie, description ) VALUES ('jdg/hello.png', 'Le soleil brille', 'meteo', 'description du soleil'),('jdg/hello.png', 'La lune brille', 'meteo', 'description de lune') ;""")
    conn.commit()
    conn.close()


# Fetch the data
def select_from_db(query):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # c.execute("SELECT * FROM articles;")
    c.execute(query)
    # Store + print the fetched data
    result = c.fetchall()
    for i in result:
        print(i)

    # Remember to save + close
    conn.commit()
    conn.close()


create_db()
# insert_db()
# select_from_db()
