import unittest
import json
from src.pokemon_writer import PokemonWriter

Parsed_pokemon_data ="""{ "id": 35,  "name":  "clefairy",  "height": 6,  "weight": 75,  "species":  "Fairy Pokémon",  "ability":  "friend-guard",  "primary_type":  "fairy",  "secondary_type":  "none"}"""
 

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

    def test_populate_table(self):
        pokemon_writer = PokemonWriter()
        pokemon_data_json = json.loads(Parsed_pokemon_data)
        pokemon_columns = ["name", "id","height", "weight", "ability", "species",  \
                          "primary_type", "secondary_type"]
        pokemon_sql = pokemon_writer.populate_table(pokemon_data_json,"Pokemon", "", pokemon_columns)

        expected_result = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'friend-guard\', \'Fairy Pokémon\', \'fairy\', \'none\');"

        self.assertEquals(expected_result, pokemon_sql)
    
    def test_convert_pokemon_json_to_sql(self):
        pokemon_writer = PokemonWriter()
        pokemon_data_json = json.loads(Parsed_pokemon_data)

        pokemon_sql = pokemon_writer.convert_pokemon_json_to_sql(pokemon_data_json)
        expected_creation = "CREATE TABLE Pokemon (\tname varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar\n);\n"
        expected_alter = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\n"
        expected_populate = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'friend-guard\', \'Fairy Pokémon\', \'fairy\', \'none\');"

        expected_result =expected_creation + expected_alter + expected_populate

        self.assertEquals(expected_result, pokemon_sql)
     
