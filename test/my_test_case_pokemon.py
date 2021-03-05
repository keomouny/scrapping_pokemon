import unittest
from pokemon import pokemon
from bs4 import BeautifulSoup

pokemon = pokemon()


class MyTestCasePokemon(unittest.TestCase, pokemon):
    def test_class_init(self):
        pass
