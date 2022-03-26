import argparse
from email.policy import default

from src.pokemon_scraper import PokemonScraper

def setup_cmd_line():

    my_parser = argparse.ArgumentParser(prog='Pokemon_Scraper')
    my_parser.add_argument('--path', help='path to sql file output. Default sqlScripts', default="sqlScripts/")
    my_parser.add_argument('--name', help='name of sql file that will be outputted. Default pokemon.sql', default="pokemon.sql")
    my_parser.add_argument('--number', help='Pokemon number retrieve from api. Default is 1, Bulbasaur.', default='1')
    return my_parser.parse_args()


def start():
    args = setup_cmd_line()
    print("done")
    PokemonScraper.json_to_local_sql_one_pokemon(args.path, args.name, args.number)

if __name__ == "__main__":
    start()