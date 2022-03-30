'''
Entry point to the  PokemonScraper program. Handles CMD line args.
'''

import argparse
import sys

from src.pokemon_scraper import PokemonScraper

def setup_cmd_line(args):
    '''
    Setup CMD parser with arguments.
    '''

    help_first_gen = 'Creates sql/nosql file for the 151st Pokemon. Mutual exclusive of number.'
    help_number = 'Create sql/nosql file for the number given.'\
                 'Default is 1, Bulbasaur. Mutual exclusive of first gen.'
    help_nosql_name ='Name of nosql file that will be outputted. Default pokemon.json'
    help_sql_name ='Name of sql file that will be outputted. Default pokemon.sql'
    help_path = 'Path to directory output. Default sqlScripts'

    my_parser = argparse.ArgumentParser(prog='Pokemon_Scraper')
    my_parser.add_argument('--path', help=help_path, default="sqlScripts/")
    my_parser.add_argument('--sql-name',help=help_sql_name, default="pokemon.sql")
    my_parser.add_argument('--no-sql-name', help=help_nosql_name, default="pokemon.json")
    # my_parser.add_mutually_exclusive_group(required=True) https://bugs.python.org/issue26952
    my_parser.add_argument('--number', help=help_number)
    my_parser.add_argument('--first-gen',action='store_true', help=help_first_gen)

    return my_parser.parse_args(args)

def start(main_args):
    '''
    Handle input from CMD line
    '''
    args = setup_cmd_line(main_args)

    if args.number is not None and args.first_gen:
        print("Use either number or first-gen flags, but not both.")
        sys.exit()
    elif args.first_gen:
        PokemonScraper.json_to_local_files_first_gen(args.path, args.sql_name, args.no_sql_name)
    elif args.number is not None:
        PokemonScraper.json_to_local_files_one_pokemon(args.path, args.sql_name, args.no_sql_name,
                                                    args.number)

if __name__ == "__main__":
    start(sys.argv[1:])
