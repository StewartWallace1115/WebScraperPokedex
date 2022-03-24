
class PokemonParser:

    # Removes properties not necessary to download from the JSON file
    def removeUnnecessaryProperties(PokemonData):        
        unnecessaryProperties = ["base_experience", "is_default", "order","game_indices",
                                 "held_items", "location_area_encounters", "past_types"]

            
        for element in unnecessaryProperties:
            del PokemonData[element]

    # Only use the first ability to simplify data. 
    def useFirstAbilityOnly(PokemonData):
        ONLY_FIRST_ABILITY = 0

        ability_data = PokemonData["abilities"][ONLY_FIRST_ABILITY]     
        PokemonData["ability"] = ability_data["ability"]["name"]
        
        # Remove abilites property since there is only one ability
        del PokemonData["abilities"]

    # Extract move set into a dictionary
