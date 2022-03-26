import unittest

from src.pokemon_scraper import PokemonScraper

class Pokemon_Scraper_Test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


        
    def test_jsonToSQL(self):
        sql_data = PokemonScraper.json_to_sql_only_one(35)

        expected_creation = "CREATE TABLE Pokemon (\tname varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar\n);\n"
        expected_alter = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\n"
        expected_populate = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'cute-charm\', \'Fairy Pokémon\', \'fairy\', \'none\');"

        expected_result = expected_creation + expected_alter + expected_populate
        
        self.assertEqual(sql_data, expected_result)