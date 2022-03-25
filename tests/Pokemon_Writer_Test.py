import unittest
import json
from src.pokemon_writer import PokemonWriter


class Pokemon_Downloader_Test(unittest.TestCase):
    
    def test_create_tables(self):
        pokemon_writer = PokemonWriter()

        columns = [("pokemon_name", "varchar"),("id", "int"),  ("height", "varchar"),("weight", "int"),("ability", "varchar"),\
                  ("species", "varchar"),("stats", "varchar"),("primary_type", "varchar"),("secondary_type", "varchar")]
        pokemon_sql = pokemon_writer.create_table("Pokemon", columns)

        expected_result = "CREATE TABLE Pokemon (\tpokemon_name varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tstats varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar\n);\n"
        self.assertEquals(expected_result, pokemon_sql)
    
    def test_create_primary_keys(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Pokemon","pokemon_name"),("Moves", "name")]
        pokemon_sql = pokemon_writer.create_primary_keys(primary_keys,"")

        expected_result = "ALTER TABLE Pokemon ADD PRIMARY KEY (pokemon_name);\nALTER TABLE Moves ADD PRIMARY KEY (name);\n"
        self.assertEquals(expected_result, pokemon_sql)

    def test_create_relationships(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Moves", "pokemon_name","Pokemon","pokemon_name"),("Moves", "name","Types", "name")]
        pokemon_sql = pokemon_writer.create_relationships(primary_keys,"")

        expected_result = "ALTER TABLE Moves ADD FOREIGN KEY (pokemon_name) REFERENCES Pokemon (pokemon_name);\nALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Types (name);\n"

        self.assertEquals(expected_result, pokemon_sql)

    def test_populate_table(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Moves", "pokemon_name","Pokemon","pokemon_name"),("Moves", "name","Types", "name")]
        pokemon_sql = pokemon_writer.create_relationships(primary_keys,"")

        expected_result = "ALTER TABLE Moves ADD FOREIGN KEY (pokemon_name) REFERENCES Pokemon (pokemon_name);\nALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Types (name);\n"

        self.assertEquals(expected_result, pokemon_sql)
    
    def test_convert_pokemon_json_to_sql(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Moves", "pokemon_name","Pokemon","pokemon_name"),("Moves", "name","Types", "name")]
        pokemon_sql = pokemon_writer.create_relationships(primary_keys,"")

        expected_result = "ALTER TABLE Moves ADD FOREIGN KEY (pokemon_name) REFERENCES Pokemon (pokemon_name);\nALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Types (name);\n"

        self.assertEquals(expected_result, pokemon_sql)
     
