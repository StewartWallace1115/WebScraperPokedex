import unittest
import json
from src.pokemon_downloader import PokemonDownloader


class Pokemon_Downloader_Test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_download_parse_pokemon(self):
        url = "https://pokeapi.co/api/v2/pokemon"
        number = 1
        pokemon_downloader = PokemonDownloader()
        pokemon_json,moveset_dicionary = pokemon_downloader.download_pokemon(url,number)
        move = moveset_dicionary["bulbasaur"][0]['move']['name']

        self.assertFalse( "moves" in pokemon_json)
        self.assertEquals( pokemon_json["name"], "bulbasaur")
        self.assertEquals(move, "razor-wind")
        self.assertFalse( "abilities" in pokemon_json)
        self.assertTrue( "ability" in pokemon_json)
        self.assertEquals(pokemon_json["ability"], "overgrow")
        self.assertFalse( "base_experience" in pokemon_json)
        self.assertFalse( "is_default" in pokemon_json)
        self.assertFalse( "order" in pokemon_json)
        self.assertFalse( "game_indices" in pokemon_json)
        self.assertFalse( "held_items" in pokemon_json)
        self.assertFalse( "location_area_encounters" in pokemon_json)
        self.assertFalse( "past_types" in pokemon_json)