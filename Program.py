import argparse
from email.policy import default

from src.pokemon_scraper import PokemonScraper

def setup_cmd_line():

    my_parser = argparse.ArgumentParser(prog='Pokemon_Scraper')
    my_parser.add_argument('--path', help='path to file output. Default sqlScripts', default="sqlScripts/")
    my_parser.add_argument('--sql-name', help='name of sql file that will be outputted. Default pokemon.sql', default="pokemon.sql")
    my_parser.add_argument('--no-sql-name', help='name of nosql file that will be outputted. Default pokemon.sql', default="pokemon.json")
    my_parser.add_argument('--number', help='Pokemon number retrieve from API. Default is 1, Bulbasaur. Mutual exclusive of first gen.', default='1')
    my_parser.add_argument('--first-gen', help='Creates sql and nosql file for the first 151 Pokemon. Mutual exclusive of number.')

    return my_parser.parse_args()


def start():
    args = setup_cmd_line()
    print("done")
    if args.number is not None:
        PokemonScraper.json_to_local_files_one_pokemon(args.path, args.sql_name, args.no_sql_name, args.number)
    elif args.first_gen:
        PokemonScraper.json_to_local_files_first_gen(args.path, args.sql_name, args.no_sql_name)

if __name__ == "__main__":
    start()