import sqlite3


def create_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Create the table, read the article below if you
    # are unsure of what they mean
    # https://www.w3schools.com/sql/sql_datatypes.asp

    SQL_DELETE = """DROP TABLE IF EXISTS articles;"""
    SQL_STATEMENT = """CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT, image text, title text NOT NULL, categorie text, description text);"""

    c.execute(SQL_DELETE)
    c.execute(SQL_STATEMENT)
    # Remember to save + close
    conn.commit()
    conn.close()


# Insert some users into our database
def insert_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    # c.execute(query)
    c.execute(
        """INSERT INTO articles (image, title, categorie, description ) VALUES ('jdg/hello.png', 'Le soleil brille', 'meteo', 'description du soleil'),('jdg/hello.png', 'La lune brille', 'meteo', 'description de lune') ;""")
    # Remember to save + close
    conn.commit()
    conn.close()


# Fetch the data
def select_from_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM articles;")
    # Store + print the fetched data
    result = c.fetchall()
    for i in result:
        print(i)

    # Remember to save + close
    conn.commit()
    conn.close()


create_db()
insert_db()
select_from_db()
