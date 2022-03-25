# """
# Downloads file from Poke API and saves it to the computer
# """
# class PokemonScraper:
#     """
#     Downloads JSON file from Poke API endpoint and saves the data
#     """

#     def scrap(self, pokemon_json, moveset_dictionary):

#         """
#         Parse pokemon json to remove unnecessary data and extract moves set
#         """

#         self.remove_unnecessary_properties(pokemon_json)
#         self.use_first_ability_only(pokemon_json)
#         self.seperate_moveset_from_pokemon_data(pokemon_json, moveset_dictionary)
