"""
Parses JSON file from PokeAPI
"""


class PokemonParser:
    """
    Parses JSON file from PokeAPI Pokemon endpoint
    """

    def parse(self, pokemon_json, species_json, moveset_dictionary, pokemon_stats):

        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """

        self.remove_unnecessary_properties(pokemon_json)
        self.use_first_ability_only(pokemon_json)
        self.seperate_data_from_pokemon_data(pokemon_json, moveset_dictionary, "moves")
        self.add_offical_artwork_property(pokemon_json)
        self.english_species_property(species_json, pokemon_json)
        self.types(pokemon_json)
        stats = self.extract_stats(pokemon_json,pokemon_stats)

        return stats

    @classmethod
    def add_offical_artwork_property(cls, pokemon_data):

        """
        Removes properties not necessary to download from the JSON file
        """

        sprites = pokemon_data["sprites"]
        official_artwork= ""

        if "other" in sprites and "official-artwork" in sprites["other"]:
            list_offical_artwork = pokemon_data["sprites"]["other"]["official-artwork"]
            if "front_default" in list_offical_artwork:
                official_artwork = list_offical_artwork["front_default"]
        elif "front_default" in sprites:
            official_artwork = sprites["front_default"]
        else:
            official_artwork = "none"
        pokemon_data["official_artwork"] = official_artwork
        del pokemon_data["sprites"]

    @classmethod
    def remove_unnecessary_properties(cls, pokemon_data):

        """
        Removes properties not necessary to download from the JSON file
        """

        unnecessary_properties = ["base_experience", "is_default", "order","game_indices",
                                 "held_items", "location_area_encounters", "past_types", "forms"]

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

    @classmethod
    def english_species_property(cls, pokemon_species, pokemon_data):
        """
        Replace species with English species property
        """

        english = "en"
        genera_data = pokemon_species["genera"]
        genus = "none"
        for element in genera_data:
            if element["language"]["name"] == english:
                genus = element["genus"]
                break

        pokemon_data["species"] = genus

    @classmethod
    def types(cls, pokemon_data):
        """
        Replace types with two properties
        """

        types = pokemon_data["types"]
        pokemon_data["primary_type"] = types[0]["type"]["name"]

        if len(types) == 2:
            pokemon_data["secondary_type"] = types[1]["type"]["name"]
        else:
            pokemon_data["secondary_type"] = "none"

        del pokemon_data["types"]

    @classmethod
    def extract_stats(cls, pokemon_data, pokemon_stats):
        """
        Replace types with two properties
        """
        cls.seperate_data_from_pokemon_data(pokemon_data,pokemon_stats,"stats")
        pokemon_current_stats = pokemon_stats[pokemon_data["name"]]
        pokemon_new_stats = {}
        pokemon_new_stats["name"] = pokemon_data["name"]
        for stat in pokemon_current_stats:
            stat_name = stat["stat"]["name"]
            pokemon_new_stats[stat_name] = stat["base_stat"]

        return pokemon_new_stats
