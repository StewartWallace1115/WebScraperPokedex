import filecmp
from operator import truediv
import unittest

from src.pokemon_scraper import PokemonScraper

class Pokemon_Scraper_Test(unittest.TestCase):

    @unittest.skip("Run locally")
    def test_json_to_local_files_one_pokemon(self):
        #Depending on file system encoding, dev might have to generate test case first then test code.
        
        PokemonScraper.json_to_local_files_one_pokemon("tests/","pokemon.sql","pokemon.json",35)
        sql_compare = filecmp.cmp("tests/pokemon.sql", "tests/test.sql", False)
        nosql_compare = filecmp.cmp("tests/pokemon.json", "tests/test.json", False)
        
        self.assertTrue(sql_compare)
        self.assertTrue(nosql_compare)
    
    @unittest.skip("Run locally")
    def test_json_to_local_files_first_gen_pokemon(self):
        #Depending on file system encoding, dev might have to generate test case first then test code.
        
        PokemonScraper.json_to_local_files_first_gen("tests/","pokemonFirstGenTest.sql","pokemonFirstGenTest.json")
        sql_compare = filecmp.cmp("tests/pokemonFirstGenTest.sql", "tests/pokemonFirstGenTest.sql", False)
        nosql_compare = filecmp.cmp("tests/pokemonFirstGenTest.json", "tests/pokemonFirstGenTest.json", False)
        
        self.assertTrue(sql_compare)
        self.assertTrue(nosql_compare)