from jdg import JDG
from jdg import pprint
from db import *


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

    # print(all_data)

    # print(list_Une)
    # print(list_actuality)

    # data_query = JDG().convert_data_for_query(all_data, '')

    # print(data_query)

    db_test = DB()
    db_test.select_from_db()
    # db_test.execute_query(db_test.create_db)
    # db_test.execute_query(db_test.create_table)
    # db_test.insert_data(all_data)
    # db_test.execute_query(db_test.select_from_db)
    db_test.__disconnect__()


if __name__ == '__main__':
    main()
