"""
Downloads file from Poke API and saves it to the computer
"""
import json
import os
import sys
from src.pokemon_downloader import PokemonDownloader
from src.pokemon_writer import PokemonWriter

class PokemonScraper:
    """
    Downloads JSON file from Poke API endpoint and saves the data
    """

    @classmethod
    def json_to_local_files_one_pokemon(cls, file_location, sql_file_name, nosql_file_name,number):
        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """

        pokemon_sql = PokemonWriter.create_pokemon_tables()
        pokemon_data, moveset_data, stat_data = cls.json_data_only_one(number)

        pokemon_sql = pokemon_sql + PokemonWriter.populate_pokemon_tables(stat_data, pokemon_data)
        moveset_json = PokemonWriter.convert_moveset_to_nosql(pokemon_data, moveset_data)

        cls.write_to_file(pokemon_sql, file_location, sql_file_name)
        cls.write_to_file(json.dumps(moveset_json), file_location, nosql_file_name)

    @classmethod
    def json_to_local_files_first_gen(cls, file_location, sql_file_name, nosql_file_name):
        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """

        first_gen_pokemon = []
        number_of_first_gen = 151
        number_of_first_gen_offset = 1 + number_of_first_gen
        moveset_json = {}

        sql_data = PokemonWriter.create_pokemon_tables()

        for pokemon_id  in range(1,number_of_first_gen_offset):
            first_gen_pokemon.append(cls.json_data_only_one(pokemon_id))

        for pokemon_data, moveset_data, stat_data   in first_gen_pokemon:
            pokemon_name = pokemon_data["name"]
            sql_data = sql_data + PokemonWriter.populate_pokemon_tables(stat_data, pokemon_data)
            moveset_json_temp = PokemonWriter.convert_moveset_to_nosql(pokemon_data,moveset_data)
            moveset_json[pokemon_name] = moveset_json_temp[pokemon_name]

        cls.write_to_file(sql_data, file_location, sql_file_name)
        cls.write_to_file(json.dumps(moveset_json), file_location, nosql_file_name)

    @classmethod
    def json_data_only_one(cls, number):
        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """

        pokemon_url = "https://pokeapi.co/api/v2/pokemon"
        species_url = "https://pokeapi.co/api/v2/pokemon-species"

        return PokemonDownloader.download_pokemon(pokemon_url, species_url, number)

    @classmethod
    def write_to_file(cls, data, file_location, file_name):
        '''
        Write data to a file.
        '''

        system_encoding = sys.getdefaultencoding()

        file_name_path = os.path.join(file_location, file_name)

        with open(file_name_path, "w+", encoding=system_encoding) as data_file:
            data_file.write(data)
