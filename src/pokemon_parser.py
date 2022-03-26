"""
Parses JSON file from PokeAPI
"""
class PokemonParser:
    """
    Parses JSON file from PokeAPI Pokemon endpoint
    """

    def parse(self, pokemon_json, moveset_dictionary, spirites_dictionary):

        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """

        self.remove_unnecessary_properties(pokemon_json)
        self.use_first_ability_only(pokemon_json)
        self.seperate_data_from_pokemon_data(pokemon_json, moveset_dictionary, "moves")
        self.seperate_data_from_pokemon_data(pokemon_json, spirites_dictionary, "sprites")


    @classmethod
    def remove_unnecessary_properties(cls, pokemon_data):

        """
        Removes properties not necessary to download from the JSON file
        """

        unnecessary_properties = ["base_experience", "is_default", "order","game_indices",
                                 "held_items", "location_area_encounters", "past_types"]

        for element in unnecessary_properties:
            del pokemon_data[element]

    @classmethod
    def use_first_ability_only(cls, pokemon_data):

        """
        Only use the first ability
        """

        only_first_ability = 0

        ability_data = pokemon_data["abilities"][only_first_ability]
        pokemon_data["ability"] = ability_data["ability"]["name"]

        # Remove abilites property since there is only one ability
        del pokemon_data["abilities"]

    @classmethod
    def seperate_data_from_pokemon_data(cls,pokemon_data, data_dictionary, data_property):

        """
        Append data property of a pokemon to data dictionary. Data is used to create seperate tables
        """

        data_dictionary[pokemon_data["name"]] = pokemon_data[data_property]

        del pokemon_data[data_property]

       