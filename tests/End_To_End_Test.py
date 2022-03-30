from argparse import ArgumentParser
import filecmp
import subprocess
import unittest
import program

from src.pokemon_scraper import PokemonScraper

class End_To_End_Test(unittest.TestCase):

    @unittest.skip("Run locally")
    def test_json_to_local_files_one_pokemon(self):
        #Depending on file system encoding, dev might have to generate test case first then test code.

        args = ['--path', 'tests/', '--sql-name', 'pokemon.sql', '--no-sql-name', 'pokemon.json', '--number', '35']
        program.setup_cmd_line(args)

        sql_compare = filecmp.cmp("tests/pokemon.sql", "tests/test.sql", False)
        nosql_compare = filecmp.cmp("tests/pokemon.json", "tests/test.json", False)
        
        self.assertTrue(sql_compare)
        self.assertTrue(nosql_compare)
    
    @unittest.skip("Run locally")
    def test_json_to_local_files_first_gen(self):
        args = ['--path', 'tests/', '--sql-name', 'pokemon.sql', '--no-sql-name', 'pokemon.json']
        program.setup_cmd_line(args)

        sql_compare = filecmp.cmp("tests/pokemon.sql", "tests/test.sql", False)
        nosql_compare = filecmp.cmp("tests/pokemon.json", "tests/test.json", False)
        
        self.assertTrue(sql_compare)
        self.assertTrue(nosql_compare)

        self.assertTrue(True)
            