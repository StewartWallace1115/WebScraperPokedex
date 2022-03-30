"""
Downloads file from Poke API
"""

import requests
from src.pokemon_parser import PokemonParser

class PokemonDownloader:
    """
    Downloads JSON file from Poke API endpoint
    """

    @classmethod
    def download_pokemon(cls, pokemon_url, species_url, number):

        """
        Downloads and parses one pokemon
        """

        moveset_dicionary = {}
        stats_dictionary = {}
        pokemon_parser = PokemonParser()
        pokemon_json = requests.get(pokemon_url + "//" + str(number)).json()
        species_json = requests.get(species_url + "//" + str(number)).json()

        stats = pokemon_parser.parse(pokemon_json, species_json, moveset_dicionary,\
             stats_dictionary)

        return pokemon_json,moveset_dicionary,stats
