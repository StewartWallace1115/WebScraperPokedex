"""
Parses JSON file from PokeAPI
"""
class PokemonParser:
    """
    Parses JSON file from PokeAPI Pokemon endpoint
    """

    def parse(self, pokemon_json, moveset_dictionary):

        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """

        self.remove_unnecessary_properties(pokemon_json)
        self.use_first_ability_only(pokemon_json)
        self.seperate_moveset_from_pokemon_data(pokemon_json, moveset_dictionary)

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
    def seperate_moveset_from_pokemon_data(cls,pokemon_data, moveset_dictionary):

        """
        Append moveset of a pokemon to moveset dictionary. Remove moves from the pokemon data
        """

        moveset_dictionary[pokemon_data["name"]] = pokemon_data["moves"]

        # Remove abilites property since there is only one ability
        del pokemon_data["moves"]
       