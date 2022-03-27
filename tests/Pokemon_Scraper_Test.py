import unittest

from src.pokemon_scraper import PokemonScraper

class Pokemon_Scraper_Test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


        
    def test_jsonToSQL(self):
        sql_data = PokemonScraper.json_to_sql_only_one(35)

        expected_creation = "CREATE TABLE Pokemon (\tname varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar,\n\tofficial_artwork varchar\n);\n"
        expected_alter = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\n"
        expected_populate = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'cute-charm\', \'Fairy Pokémon\', \'fairy\', \'none\', \'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/35.png\');\n"
        expected_moves = """CREATE TABLE Stats (\tname varchar,\n\thp int,\n\tattack int,\n\tdefense int,\n\tspecial-attack int,\n\tspecial-defense int,\n\tspeed int\n);\nALTER TABLE Stats ADD PRIMARY KEY (name);\nINSERT INTO Stats VALUES ('clefairy', 70, 45, 48, 60, 65, 35);\n"""
        expected_result =expected_creation + expected_alter + expected_populate + expected_moves

        
        self.assertEqual(sql_data, expected_result)
            
