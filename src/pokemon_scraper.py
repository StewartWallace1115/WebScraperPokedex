"""
Downloads file from Poke API and saves it to the computer
"""
import json
import os
from src.pokemon_downloader import PokemonDownloader
from src.pokemon_writer import PokemonWriter

class PokemonScraper:
    """
    Downloads JSON file from Poke API endpoint and saves the data
    """
    @classmethod
    def json_to_local_sql_one_pokemon(cls, sql_file_location, sql_file_name, number):
        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """

        sql_data = cls.json_to_sql_only_one(number)
        file_path = os.path.join(sql_file_location, sql_file_name)

        with open(file_path, "w+") as sql_file:
            sql_file.write(sql_data)

    @classmethod
    def json_to_sql_only_one(cls, number):

        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """
        pokemon_url = "https://pokeapi.co/api/v2/pokemon"
        species_url = "https://pokeapi.co/api/v2/pokemon-species"

        only_pokemon_data = 0
        only_stat_data = 2
        pokemon_tuple = PokemonDownloader.download_pokemon(pokemon_url, species_url, number)
        pokemon_json = pokemon_tuple[only_pokemon_data]
        pokemon_stats_json = pokemon_tuple[only_stat_data]

        sql_data = PokemonWriter.convert_pokemon_json_to_sql(pokemon_json,pokemon_stats_json)
        return sql_data

    @classmethod
    def json_to_local_files_one_pokemon(cls, file_location, sql_file_name, nosql_file_name,number):
        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """
        only_pokemon_data = 0
        moveset_data = 1
        only_stat_data = 2
        pokemon_data = cls.json_data_only_one(number)
        sql_data = PokemonWriter.convert_pokemon_json_to_sql(pokemon_data[only_pokemon_data],pokemon_data[only_stat_data])
        moveset_json = PokemonWriter.convert_moveset_to_nosql(pokemon_data[only_pokemon_data],pokemon_data[moveset_data])

        sql_file_path = os.path.join(file_location, sql_file_name)

        with open(sql_file_path, "w+") as sql_file:
            sql_file.write(sql_data)
        
        nosql_file_path = os.path.join(file_location, nosql_file_name)

        with open(nosql_file_path, "w+") as nosql_file:
            nosql_file.write(json.dumps(moveset_json))

    @classmethod
    def json_to_local_files_first_gen(cls, file_location, sql_file_name, nosql_file_name):
        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """
        only_pokemon_data = 0
        moveset_data = 1
        only_stat_data = 2
        first_gen_pokemon = []
        number_of_first_gen = 151
        number_of_first_gen_offset = 1 + number_of_first_gen
        for id  in range(1,number_of_first_gen_offset):
             first_gen_pokemon.append(cls.json_data_only_one(id))
        
        first_pokemon = first_gen_pokemon.pop(0)

        sql_data = PokemonWriter.convert_pokemon_json_to_sql(first_pokemon[only_pokemon_data],first_pokemon[only_stat_data])
        moveset_json = PokemonWriter.convert_moveset_to_nosql(first_pokemon[only_pokemon_data],first_pokemon[moveset_data])

        # Move to constant file
        pokemon_columns = ["name", "id","height", "weight", "ability", "species",  \
                          "primary_type", "secondary_type", "official_artwork"]
        stats_columns = ["name", "hp","attack", "defense", "special-attack", "special-defense","speed"]

        for pokemon  in first_gen_pokemon:
            pokemon_name = pokemon[only_pokemon_data]["name"]
            sql_data = sql_data + PokemonWriter.populate_table(pokemon[only_pokemon_data],"Pokemon",sql_data,pokemon_columns)
            sql_data = sql_data + PokemonWriter.populate_table(pokemon[only_stat_data],"Stats",sql_data,stats_columns)
            moveset_json_temp = PokemonWriter.convert_moveset_to_nosql(pokemon[only_pokemon_data],pokemon[moveset_data])
            moveset_json[pokemon_name] = moveset_json_temp[pokemon_name]
            
        sql_file_path = os.path.join(file_location, sql_file_name)

        with open(sql_file_path, "w+") as sql_file:
             sql_file.write(sql_data)
        
        nosql_file_path = os.path.join(file_location, nosql_file_name)

        with open(nosql_file_path, "w+") as nosql_file:
            nosql_file.write(json.dumps(moveset_json))

    @classmethod
    def json_data_only_one(cls, number):

        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """
        pokemon_url = "https://pokeapi.co/api/v2/pokemon"
        species_url = "https://pokeapi.co/api/v2/pokemon-species"

        return PokemonDownloader.download_pokemon(pokemon_url, species_url, number)

