from jdg import JDG
from pprint import pprint
from dbconnection import *


def main():

    # List actuality :
    entry_item_article = JDG().soup.find_all(
        'div', {'class': 'entry__item'})
    list_actuality = JDG().get_data(entry_item_article)

    # List article à la une
    entry_item_une = JDG().soup.find('div', {
        'class': 'entry__grid-container'}).findChildren('div', {'class': 'entry__item'})
    list_Une = JDG().get_data(entry_item_une)

    all_data = list_actuality + list_Une

    data_query = JDG().convert_data_for_query(all_data, '')

    test_db = DBConnection()
    test_db.create_db()
    test_db.insert_db(data_query)
    test_db.select_from_db()
    test_db.close_db()


if __name__ == '__main__':
    main()
