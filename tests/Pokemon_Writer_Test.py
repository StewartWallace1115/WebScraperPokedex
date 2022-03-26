import unittest
import json

from aiohttp import JsonPayload
from src.pokemon_writer import PokemonWriter

Parsed_pokemon_data ="""{ "id": 35,  "name":  "clefairy",  "height": 6,  "weight": 75,  "species":  "Fairy Pokémon",  "ability":  "friend-guard",  "primary_type":  "fairy",  "secondary_type":  "none"}"""
Parsed_pokemon_stat  = """{ "name": "clefairy","hp": 75, "attack":45 , "defense":45, "special-attack":60, "special-defense":45, "speed":35}"""

class Pokemon_Downloader_Test(unittest.TestCase):
    
    
    def test_create_tables(self):
        pokemon_writer = PokemonWriter()

        columns = [("name", "varchar"),("id", "int"),  ("height", "varchar"),("weight", "int"),("ability", "varchar"),\
                  ("species", "varchar"),("primary_type", "varchar"),("secondary_type", "varchar")]
        pokemon_sql = pokemon_writer.create_table("Pokemon", columns)

        expected_result = "CREATE TABLE Pokemon (\tname varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar\n);\n"
        self.assertEquals(expected_result, pokemon_sql)
    
    def test_create_primary_keys(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Pokemon","name"),("Moves", "name")]
        pokemon_sql = pokemon_writer.create_primary_keys(primary_keys,"")

        expected_result = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\nALTER TABLE Moves ADD PRIMARY KEY (name);\n"
        self.assertEquals(expected_result, pokemon_sql)
    
    def test_create_primary_key(self):
        pokemon_writer = PokemonWriter()
        pokemon_sql = pokemon_writer.create_primary_key("name", "Pokemon","")

        expected_result = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\n"
        self.assertEquals(expected_result, pokemon_sql)

    def test_create_relationships(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Moves", "name","Pokemon","name"),("Moves", "name","Types", "name")]
        pokemon_sql = pokemon_writer.create_relationships(primary_keys,"")

        expected_result = "ALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Pokemon (name);\nALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Types (name);\n"

        self.assertEquals(expected_result, pokemon_sql)

    def test_populate_table_pokemon(self):
        pokemon_writer = PokemonWriter()
        pokemon_data_json = json.loads(Parsed_pokemon_data)
        pokemon_columns = ["name", "id","height", "weight", "ability", "species",  \
                          "primary_type", "secondary_type"]
        pokemon_sql = pokemon_writer.populate_table(pokemon_data_json,"Pokemon", "", pokemon_columns)

        expected_result = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'friend-guard\', \'Fairy Pokémon\', \'fairy\', \'none\');\n"

        self.assertEquals(expected_result, pokemon_sql)
    
    def test_convert_pokemon_json_to_sql(self):
        pokemon_writer = PokemonWriter()

        pokemon_data_json = json.loads(Parsed_pokemon_data)
        stat_data_json = json.loads(Parsed_pokemon_stat)
        pokemon_sql = pokemon_writer.convert_pokemon_json_to_sql(pokemon_data_json, stat_data_json)
        expected_creation = "CREATE TABLE Pokemon (\tname varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar\n);\n"
        expected_alter = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\n"
        expected_populate = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'friend-guard\', \'Fairy Pokémon\', \'fairy\', \'none\');\n"
        expected_moves = """CREATE TABLE Stats (\tname varchar,\n\thp int,\n\tattack int,\n\tdefense int,\n\tspecial-attack int,\n\tspecial-defense int,\n\tspeed int\n);\nALTER TABLE Stats ADD PRIMARY KEY (name);\nINSERT INTO Stats VALUES ('clefairy', 75, 45, 45, 60, 45, 35);\n"""
        expected_result =expected_creation + expected_alter + expected_populate + expected_moves

        self.assertEquals(expected_result, pokemon_sql)

        self.assertEquals(expected_result, pokemon_sql)
     
     
