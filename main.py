from jdg import JDG
from pprint import pprint


def main():

    # List actuality :
    entry_item_article = JDG().soup.find_all(
        'div', {'class': 'entry__item'})
    list_actuality = JDG().get_data(entry_item_article)

    # List article à la une
    entry_item_une = JDG().soup.find('div', {
        'class': 'entry__grid-container'}).findChildren('div', {'class': 'entry__item'})
    list_Une = JDG().get_data(entry_item_une)
    pprint(list_Une)


if __name__ == '__main__':
    main()
