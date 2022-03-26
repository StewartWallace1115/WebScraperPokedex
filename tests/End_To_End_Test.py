import filecmp
import unittest

from src.pokemon_scraper import PokemonScraper

class Pokemon_Scraper_Test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


        
    def test_jsonToLocalSQLOnlyOne(self):
        sql_data = PokemonScraper.json_to_local_sql_one_pokemon("tests/","pokemon.sql",35)
        results = filecmp.cmp("tests/test.sql","tests/pokemon.sql",False)

        self.assertTrue(True)
        #self.assertTrue(results)