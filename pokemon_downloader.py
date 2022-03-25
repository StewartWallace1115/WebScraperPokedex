"""
Downloads file from Poke API
"""

import requests
from pokemon_parser import PokemonParser

class PokemonDownloader:
    """
    Downloads JSON file from Poke API endpoint
    """

    @classmethod
    def download_all_pokemon(cls, moveset_dictionary):

        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """
        return moveset_dictionary

    @classmethod
    def download_pokemon(cls, url, number):

        """
        Downloads and parses one pokemon
        """

        response = requests.get(url + "//" + str(number))
        moveset_dicionary = {}
        pokemon_json = response.json()
        pokemon_parser = PokemonParser()
        pokemon_parser.parse(pokemon_json, moveset_dicionary)

        return pokemon_json,moveset_dicionary
