import unittest
import json

from aiohttp import JsonPayload
from src.pokemon_writer import PokemonWriter

Parsed_pokemon_data ="""{ "id": 35,  "name":  "clefairy",  "height": 6,  "weight": 75,  "species":  "Fairy Pokémon",  "ability":  "friend-guard",  "primary_type":  "fairy",  "secondary_type":  "none", "official_artwork": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/35.png"}"""
Parsed_pokemon_stat  = """{ "name": "clefairy","hp": 75, "attack":45 , "defense":45, "special-attack":60, "special-defense":45, "speed":35}"""
Parsed_moveset_data ="""{ "clefairy": [
    {
      "move": {
        "name": "pound",
        "url": "https://pokeapi.co/api/v2/move/1/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "double-slap",
        "url": "https://pokeapi.co/api/v2/move/3/"
      },
      "version_group_details": [
        {
          "level_learned_at": 18,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 18,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 12,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "mega-punch",
        "url": "https://pokeapi.co/api/v2/move/5/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "fire-punch",
        "url": "https://pokeapi.co/api/v2/move/7/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "ice-punch",
        "url": "https://pokeapi.co/api/v2/move/8/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "thunder-punch",
        "url": "https://pokeapi.co/api/v2/move/9/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "mega-kick",
        "url": "https://pokeapi.co/api/v2/move/25/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "headbutt",
        "url": "https://pokeapi.co/api/v2/move/29/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "body-slam",
        "url": "https://pokeapi.co/api/v2/move/34/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 24,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "take-down",
        "url": "https://pokeapi.co/api/v2/move/36/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "double-edge",
        "url": "https://pokeapi.co/api/v2/move/38/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "growl",
        "url": "https://pokeapi.co/api/v2/move/45/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "sing",
        "url": "https://pokeapi.co/api/v2/move/47/"
      },
      "version_group_details": [
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 8,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 8,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 9,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 9,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 9,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 9,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 9,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 7,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 6,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "flamethrower",
        "url": "https://pokeapi.co/api/v2/move/53/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "water-gun",
        "url": "https://pokeapi.co/api/v2/move/55/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "ice-beam",
        "url": "https://pokeapi.co/api/v2/move/58/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "blizzard",
        "url": "https://pokeapi.co/api/v2/move/59/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "bubble-beam",
        "url": "https://pokeapi.co/api/v2/move/61/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "submission",
        "url": "https://pokeapi.co/api/v2/move/66/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "counter",
        "url": "https://pokeapi.co/api/v2/move/68/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "seismic-toss",
        "url": "https://pokeapi.co/api/v2/move/69/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "strength",
        "url": "https://pokeapi.co/api/v2/move/70/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "solar-beam",
        "url": "https://pokeapi.co/api/v2/move/76/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "thunderbolt",
        "url": "https://pokeapi.co/api/v2/move/85/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "thunder-wave",
        "url": "https://pokeapi.co/api/v2/move/86/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "thunder",
        "url": "https://pokeapi.co/api/v2/move/87/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "dig",
        "url": "https://pokeapi.co/api/v2/move/91/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "toxic",
        "url": "https://pokeapi.co/api/v2/move/92/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "psychic",
        "url": "https://pokeapi.co/api/v2/move/94/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "rage",
        "url": "https://pokeapi.co/api/v2/move/99/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "teleport",
        "url": "https://pokeapi.co/api/v2/move/100/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "mimic",
        "url": "https://pokeapi.co/api/v2/move/102/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "double-team",
        "url": "https://pokeapi.co/api/v2/move/104/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "minimize",
        "url": "https://pokeapi.co/api/v2/move/107/"
      },
      "version_group_details": [
        {
          "level_learned_at": 24,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 24,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 21,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 21,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 21,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 21,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 21,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 10,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 8,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "defense-curl",
        "url": "https://pokeapi.co/api/v2/move/111/"
      },
      "version_group_details": [
        {
          "level_learned_at": 39,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 39,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 26,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 26,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 13,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "light-screen",
        "url": "https://pokeapi.co/api/v2/move/113/"
      },
      "version_group_details": [
        {
          "level_learned_at": 48,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 48,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 53,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 53,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 41,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 41,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 41,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 41,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 41,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "reflect",
        "url": "https://pokeapi.co/api/v2/move/115/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "bide",
        "url": "https://pokeapi.co/api/v2/move/117/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "metronome",
        "url": "https://pokeapi.co/api/v2/move/118/"
      },
      "version_group_details": [
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 29,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 29,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 29,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 29,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 29,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 18,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 20,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "fire-blast",
        "url": "https://pokeapi.co/api/v2/move/126/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "skull-bash",
        "url": "https://pokeapi.co/api/v2/move/130/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "amnesia",
        "url": "https://pokeapi.co/api/v2/move/133/"
      },
      "version_group_details": [
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "soft-boiled",
        "url": "https://pokeapi.co/api/v2/move/135/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "dream-eater",
        "url": "https://pokeapi.co/api/v2/move/138/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "flash",
        "url": "https://pokeapi.co/api/v2/move/148/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "psywave",
        "url": "https://pokeapi.co/api/v2/move/149/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "splash",
        "url": "https://pokeapi.co/api/v2/move/150/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "rest",
        "url": "https://pokeapi.co/api/v2/move/156/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "tri-attack",
        "url": "https://pokeapi.co/api/v2/move/161/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "substitute",
        "url": "https://pokeapi.co/api/v2/move/164/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "yellow",
            "url": "https://pokeapi.co/api/v2/version-group/2/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "nightmare",
        "url": "https://pokeapi.co/api/v2/move/171/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "snore",
        "url": "https://pokeapi.co/api/v2/move/173/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "curse",
        "url": "https://pokeapi.co/api/v2/move/174/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "protect",
        "url": "https://pokeapi.co/api/v2/move/182/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "sweet-kiss",
        "url": "https://pokeapi.co/api/v2/move/186/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "mud-slap",
        "url": "https://pokeapi.co/api/v2/move/189/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "zap-cannon",
        "url": "https://pokeapi.co/api/v2/move/192/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "icy-wind",
        "url": "https://pokeapi.co/api/v2/move/196/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "detect",
        "url": "https://pokeapi.co/api/v2/move/197/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "endure",
        "url": "https://pokeapi.co/api/v2/move/203/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "charm",
        "url": "https://pokeapi.co/api/v2/move/204/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "rollout",
        "url": "https://pokeapi.co/api/v2/move/205/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "swagger",
        "url": "https://pokeapi.co/api/v2/move/207/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "attract",
        "url": "https://pokeapi.co/api/v2/move/213/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "sleep-talk",
        "url": "https://pokeapi.co/api/v2/move/214/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "heal-bell",
        "url": "https://pokeapi.co/api/v2/move/215/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "return",
        "url": "https://pokeapi.co/api/v2/move/216/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "frustration",
        "url": "https://pokeapi.co/api/v2/move/218/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "safeguard",
        "url": "https://pokeapi.co/api/v2/move/219/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "dynamic-punch",
        "url": "https://pokeapi.co/api/v2/move/223/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "baton-pass",
        "url": "https://pokeapi.co/api/v2/move/226/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "encore",
        "url": "https://pokeapi.co/api/v2/move/227/"
      },
      "version_group_details": [
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 5,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 5,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 5,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 5,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 5,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "iron-tail",
        "url": "https://pokeapi.co/api/v2/move/231/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "moonlight",
        "url": "https://pokeapi.co/api/v2/move/236/"
      },
      "version_group_details": [
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 24,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "hidden-power",
        "url": "https://pokeapi.co/api/v2/move/237/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "rain-dance",
        "url": "https://pokeapi.co/api/v2/move/240/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "sunny-day",
        "url": "https://pokeapi.co/api/v2/move/241/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "psych-up",
        "url": "https://pokeapi.co/api/v2/move/244/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "shadow-ball",
        "url": "https://pokeapi.co/api/v2/move/247/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "gold-silver",
            "url": "https://pokeapi.co/api/v2/version-group/3/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "crystal",
            "url": "https://pokeapi.co/api/v2/version-group/4/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "rock-smash",
        "url": "https://pokeapi.co/api/v2/move/249/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "uproar",
        "url": "https://pokeapi.co/api/v2/move/253/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "facade",
        "url": "https://pokeapi.co/api/v2/move/263/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "focus-punch",
        "url": "https://pokeapi.co/api/v2/move/264/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "follow-me",
        "url": "https://pokeapi.co/api/v2/move/266/"
      },
      "version_group_details": [
        {
          "level_learned_at": 17,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 17,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 17,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 17,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 17,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 36,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "helping-hand",
        "url": "https://pokeapi.co/api/v2/move/270/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "trick",
        "url": "https://pokeapi.co/api/v2/move/271/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "role-play",
        "url": "https://pokeapi.co/api/v2/move/272/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "magic-coat",
        "url": "https://pokeapi.co/api/v2/move/277/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "recycle",
        "url": "https://pokeapi.co/api/v2/move/278/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "brick-break",
        "url": "https://pokeapi.co/api/v2/move/280/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "knock-off",
        "url": "https://pokeapi.co/api/v2/move/282/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "endeavor",
        "url": "https://pokeapi.co/api/v2/move/283/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "imprison",
        "url": "https://pokeapi.co/api/v2/move/286/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "snatch",
        "url": "https://pokeapi.co/api/v2/move/289/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "secret-power",
        "url": "https://pokeapi.co/api/v2/move/290/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "hyper-voice",
        "url": "https://pokeapi.co/api/v2/move/304/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "meteor-mash",
        "url": "https://pokeapi.co/api/v2/move/309/"
      },
      "version_group_details": [
        {
          "level_learned_at": 45,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 45,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 45,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 55,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 45,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 45,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 52,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 50,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 50,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 50,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 50,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 32,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "fake-tears",
        "url": "https://pokeapi.co/api/v2/move/313/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "cosmic-power",
        "url": "https://pokeapi.co/api/v2/move/322/"
      },
      "version_group_details": [
        {
          "level_learned_at": 33,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 33,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 33,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 33,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 33,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 40,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "signal-beam",
        "url": "https://pokeapi.co/api/v2/move/324/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "bounce",
        "url": "https://pokeapi.co/api/v2/move/340/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "covet",
        "url": "https://pokeapi.co/api/v2/move/343/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "magical-leaf",
        "url": "https://pokeapi.co/api/v2/move/345/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "calm-mind",
        "url": "https://pokeapi.co/api/v2/move/347/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "shock-wave",
        "url": "https://pokeapi.co/api/v2/move/351/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "water-pulse",
        "url": "https://pokeapi.co/api/v2/move/352/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ruby-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/5/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "emerald",
            "url": "https://pokeapi.co/api/v2/version-group/6/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "firered-leafgreen",
            "url": "https://pokeapi.co/api/v2/version-group/7/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "colosseum",
            "url": "https://pokeapi.co/api/v2/version-group/12/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "xd",
            "url": "https://pokeapi.co/api/v2/version-group/13/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "gravity",
        "url": "https://pokeapi.co/api/v2/move/356/"
      },
      "version_group_details": [
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 34,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 49,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 49,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 49,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 49,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 49,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "wake-up-slap",
        "url": "https://pokeapi.co/api/v2/move/358/"
      },
      "version_group_details": [
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 22,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "healing-wish",
        "url": "https://pokeapi.co/api/v2/move/361/"
      },
      "version_group_details": [
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 49,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 55,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 55,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 55,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 55,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 55,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 48,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "natural-gift",
        "url": "https://pokeapi.co/api/v2/move/363/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "fling",
        "url": "https://pokeapi.co/api/v2/move/374/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "lucky-chant",
        "url": "https://pokeapi.co/api/v2/move/381/"
      },
      "version_group_details": [
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 31,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 37,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "copycat",
        "url": "https://pokeapi.co/api/v2/move/383/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "last-resort",
        "url": "https://pokeapi.co/api/v2/move/387/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "drain-punch",
        "url": "https://pokeapi.co/api/v2/move/409/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "zen-headbutt",
        "url": "https://pokeapi.co/api/v2/move/428/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "captivate",
        "url": "https://pokeapi.co/api/v2/move/445/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "stealth-rock",
        "url": "https://pokeapi.co/api/v2/move/446/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "grass-knot",
        "url": "https://pokeapi.co/api/v2/move/447/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "charge-beam",
        "url": "https://pokeapi.co/api/v2/move/451/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "diamond-pearl",
            "url": "https://pokeapi.co/api/v2/version-group/8/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version-group/9/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "heartgold-soulsilver",
            "url": "https://pokeapi.co/api/v2/version-group/10/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "wonder-room",
        "url": "https://pokeapi.co/api/v2/move/472/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "psyshock",
        "url": "https://pokeapi.co/api/v2/move/473/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "telekinesis",
        "url": "https://pokeapi.co/api/v2/move/477/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "after-you",
        "url": "https://pokeapi.co/api/v2/move/495/"
      },
      "version_group_details": [
        {
          "level_learned_at": 52,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 58,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 58,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 58,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 58,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 58,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 12,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "round",
        "url": "https://pokeapi.co/api/v2/move/496/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "echoed-voice",
        "url": "https://pokeapi.co/api/v2/move/497/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "stored-power",
        "url": "https://pokeapi.co/api/v2/move/500/"
      },
      "version_group_details": [
        {
          "level_learned_at": 43,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 4,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "ally-switch",
        "url": "https://pokeapi.co/api/v2/move/502/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "incinerate",
        "url": "https://pokeapi.co/api/v2/move/510/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "retaliate",
        "url": "https://pokeapi.co/api/v2/move/514/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "bestow",
        "url": "https://pokeapi.co/api/v2/move/516/"
      },
      "version_group_details": [
        {
          "level_learned_at": 25,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 19,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "work-up",
        "url": "https://pokeapi.co/api/v2/move/526/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-white",
            "url": "https://pokeapi.co/api/v2/version-group/11/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "black-2-white-2",
            "url": "https://pokeapi.co/api/v2/version-group/14/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "disarming-voice",
        "url": "https://pokeapi.co/api/v2/move/574/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "draining-kiss",
        "url": "https://pokeapi.co/api/v2/move/577/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "misty-terrain",
        "url": "https://pokeapi.co/api/v2/move/581/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "play-rough",
        "url": "https://pokeapi.co/api/v2/move/583/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "moonblast",
        "url": "https://pokeapi.co/api/v2/move/585/"
      },
      "version_group_details": [
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 46,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 28,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 44,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "confide",
        "url": "https://pokeapi.co/api/v2/move/590/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "mystical-fire",
        "url": "https://pokeapi.co/api/v2/move/595/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "dazzling-gleam",
        "url": "https://pokeapi.co/api/v2/move/605/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "lets-go-pikachu-lets-go-eevee",
            "url": "https://pokeapi.co/api/v2/version-group/19/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "power-up-punch",
        "url": "https://pokeapi.co/api/v2/move/612/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "x-y",
            "url": "https://pokeapi.co/api/v2/version-group/15/"
          }
        },
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "machine",
            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
          },
          "version_group": {
            "name": "omega-ruby-alpha-sapphire",
            "url": "https://pokeapi.co/api/v2/version-group/16/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "spotlight",
        "url": "https://pokeapi.co/api/v2/move/671/"
      },
      "version_group_details": [
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sun-moon",
            "url": "https://pokeapi.co/api/v2/version-group/17/"
          }
        },
        {
          "level_learned_at": 1,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "ultra-sun-ultra-moon",
            "url": "https://pokeapi.co/api/v2/version-group/18/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "life-dew",
        "url": "https://pokeapi.co/api/v2/move/791/"
      },
      "version_group_details": [
        {
          "level_learned_at": 16,
          "move_learn_method": {
            "name": "level-up",
            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "meteor-beam",
        "url": "https://pokeapi.co/api/v2/move/800/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "misty-explosion",
        "url": "https://pokeapi.co/api/v2/move/802/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    },
    {
      "move": {
        "name": "dual-wingbeat",
        "url": "https://pokeapi.co/api/v2/move/814/"
      },
      "version_group_details": [
        {
          "level_learned_at": 0,
          "move_learn_method": {
            "name": "tutor",
            "url": "https://pokeapi.co/api/v2/move-learn-method/3/"
          },
          "version_group": {
            "name": "sword-shield",
            "url": "https://pokeapi.co/api/v2/version-group/20/"
          }
        }
      ]
    }
  ]

}"""
class Pokemon_Downloader_Test(unittest.TestCase):
    
    
    def test_create_tables(self):
        pokemon_writer = PokemonWriter()

        columns = [("name", "varchar"),("id", "int"),  ("height", "varchar"),("weight", "int"),("ability", "varchar"),\
                  ("species", "varchar"),("primary_type", "varchar"),("secondary_type", "varchar"),("offical_artwork", "varchar")]
        pokemon_sql = pokemon_writer.create_table("Pokemon", columns)

        expected_result = "CREATE TABLE Pokemon (\tname varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar,\n\toffical_artwork varchar\n);\n"
        self.assertEquals(expected_result, pokemon_sql)
    
    def test_create_primary_keys(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Pokemon","name"),("Moves", "name")]
        pokemon_sql = pokemon_writer.create_primary_keys(primary_keys,"")

        expected_result = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\nALTER TABLE Moves ADD PRIMARY KEY (name);\n"
        self.assertEquals(expected_result, pokemon_sql)
    
    def test_create_primary_key(self):
        pokemon_writer = PokemonWriter()
        pokemon_sql = pokemon_writer.create_primary_key("name", "Pokemon","")

        expected_result = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\n"
        self.assertEquals(expected_result, pokemon_sql)

    def test_create_relationships(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Moves", "name","Pokemon","name"),("Moves", "name","Types", "name")]
        pokemon_sql = pokemon_writer.create_relationships(primary_keys,"")

        expected_result = "ALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Pokemon (name);\nALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Types (name);\n"

        self.assertEquals(expected_result, pokemon_sql)

    def test_populate_table_pokemon(self):
        pokemon_writer = PokemonWriter()
        pokemon_data_json = json.loads(Parsed_pokemon_data)
        pokemon_columns = ["name", "id","height", "weight", "ability", "species",  \
                          "primary_type", "secondary_type", "official_artwork"]
        pokemon_sql = pokemon_writer.populate_table(pokemon_data_json,"Pokemon", "", pokemon_columns)

        expected_result = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'friend-guard\', \'Fairy Pokémon\', \'fairy\', \'none\', \'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/35.png\');\n"

        self.assertEquals(expected_result, pokemon_sql)
    
    def test_convert_pokemon_json_to_sql(self):
        pokemon_writer = PokemonWriter()

        pokemon_data_json = json.loads(Parsed_pokemon_data)
        stat_data_json = json.loads(Parsed_pokemon_stat)
        pokemon_sql = pokemon_writer.convert_pokemon_json_to_sql(pokemon_data_json, stat_data_json)
        expected_creation = "CREATE TABLE Pokemon (\tname varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar,\n\tofficial_artwork varchar\n);\n" 
        expected_alter = "ALTER TABLE Pokemon ADD PRIMARY KEY (name);\n"
        expected_populate = "INSERT INTO Pokemon VALUES (\'clefairy\', 35, 6, 75, \'friend-guard\', \'Fairy Pokémon\', \'fairy\', \'none\', \'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/35.png\');\n"
        expected_moves = """CREATE TABLE Stats (\tname varchar,\n\thp int,\n\tattack int,\n\tdefense int,\n\tspecial-attack int,\n\tspecial-defense int,\n\tspeed int\n);\nALTER TABLE Stats ADD PRIMARY KEY (name);\nINSERT INTO Stats VALUES ('clefairy', 75, 45, 45, 60, 45, 35);\n"""
        expected_result =expected_creation + expected_alter + expected_populate + expected_moves

        self.assertEquals(expected_result, pokemon_sql)

        self.assertEquals(expected_result, pokemon_sql)

    def test_convert_pokemon_json_to_nosql(self):
        pokemon_writer = PokemonWriter()

        pokemon_data_json = json.loads(Parsed_pokemon_data)
        moveset = json.loads(Parsed_moveset_data)
        moveset_array = pokemon_writer.convert_moveset_to_nosql(pokemon_data_json, moveset)

        self.assertTrue("clefairy" in moveset_array)
        self.assertEquals(moveset_array['clefairy'][0], 'pound')
        self.assertEquals(moveset_array['clefairy'][145], 'dual-wingbeat')

     
     
