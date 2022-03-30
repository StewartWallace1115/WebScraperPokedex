"""
Downloads file from Poke API
"""

class PokemonWriter:
    """
    Downloads JSON file from Poke API endpoint
    """

    @classmethod
    def convert_moveset_to_nosql(cls,pokemon_json, moveset):
        """
        Convert moveset to nosql (json)
        """

        name = pokemon_json['name']
        pokemon = moveset[name]
        array_moveset = []
        simplified_moveset = {}
        for element in pokemon:
            array_moveset.append(element['move']['name'])

        simplified_moveset[name] = array_moveset
        return simplified_moveset

    @classmethod
    def populate_pokemon_tables(cls,stat_json, pokemon_json):
        """
        Create SQL file from pokemon data
        """

        pokemon_columns = ["name", "id","height", "weight", "ability", "species",  \
                          "primary_type", "secondary_type", "official_artwork"]
        stats_columns = ["name", "hp","attack", "defense", "special-attack", "special-defense",\
                        "speed"]

        table_name_pokemon = "Pokemon"
        table_name_stats= "Stats"

        sql_pokemon_creation = cls.populate_table(pokemon_json, table_name_pokemon, \
                                pokemon_columns)
        sql_stats_creation = cls.populate_table(stat_json, table_name_stats, stats_columns)

        return sql_pokemon_creation + sql_stats_creation

    @classmethod
    def create_pokemon_tables(cls):
        """
        Create SQL file from pokemon data
        """

        pokemon_columns_types = [("name", "varchar"),("id", "int"),  ("height", "varchar"),\
                        ("weight", "int"),("ability", "varchar"),("species", "varchar"),\
                        ("primary_type", "varchar"),\
                        ("secondary_type", "varchar"), ("official_artwork", "varchar")]

        stats_columns_types = [("name", "varchar"),("hp", "int"), ("attack", "int"),\
                             ("defense", "int"), ("special-attack", "int"), \
                             ("special-defense", "int"),("speed", "int")]

        table_name_stats= "Stats"
        primary_key_stats = "name"
        table_name_pokemon = "Pokemon"
        primary_key_pokemon = "name"

        sql_pokemon_creation = cls.init_table(table_name_pokemon, primary_key_pokemon, \
                                pokemon_columns_types)
        sql_stats_creation = cls.init_table(table_name_stats, primary_key_stats, \
                            stats_columns_types)

        return sql_pokemon_creation + sql_stats_creation

    @classmethod
    def init_table(cls, table_name, primary_key, column_types):
        """
        Create tables and primary key for table
        """

        sql_pokemon_creation = cls.create_table(table_name, column_types)
        sql_primary_key_creation = cls.create_primary_key(table_name, primary_key)
        return sql_pokemon_creation + sql_primary_key_creation

    @classmethod
    def create_table(cls, table_name, columns):
        """
        Create SQL table using table and columns
        """

        column_name = 0
        column_datatype = 1
        sql_creation = "CREATE TABLE " + table_name + " ("

        for column in columns:
            sql_creation = sql_creation + "\t" + column[column_name] + \
            " " + column[column_datatype] + ",\n"

        sql_creation = cls.remove_last_comma(sql_creation, False)

        sql_creation = sql_creation + ");\n"
        return sql_creation

    @classmethod
    def create_primary_key(cls, table_name, primary_key):
        """
        Create set of SQL primary keys using Alter table method.
        """

        sql_creation_string = "ALTER TABLE " + table_name +" ADD PRIMARY KEY "\
                                "(" + primary_key + ");\n"

        return sql_creation_string


    @classmethod
    def create_relationships(cls, keys_tables, sql_creation_string):
        """
        Create SQL relationships using alter table method.
        """

        for key_table in keys_tables:
            sql_creation_string = sql_creation_string + "ALTER TABLE " + key_table[0] + \
            " ADD FOREIGN KEY (" +key_table[1] + ") REFERENCES " + key_table[2] + \
            " (" +key_table[3] + ");\n"

        return sql_creation_string

    @classmethod
    def populate_table(cls, pokemon_json, table_name, columns):
        """
        Populate SQL table using values and keys
        """

        value_string = "("

        for element in columns:
            value = pokemon_json[element]

            if not isinstance(value, str):
                value = str(value)
            else:
                value = "\'" + value + "\'"

            value_string = value_string + value +", "

        value_string = cls.remove_last_comma(value_string, True)
        sql_creation_string =  "INSERT INTO "+ table_name + " VALUES " + value_string + ");\n"
        return sql_creation_string

    @classmethod
    def remove_last_comma(cls, sql_creation, with_extra_space):
        """
        Remove the last comma in a string with or without spaces around comma.
        """

        only_comma = 1
        comma_and_space = 2
        amount_characters_skipped = only_comma

        if with_extra_space:
            amount_characters_skipped = comma_and_space

        last_comma_index = sql_creation.rfind(',')
        beginning_substring = sql_creation[0 : last_comma_index : ]
        ending_substring = sql_creation[last_comma_index + amount_characters_skipped : :]
        sql_creation = beginning_substring + ending_substring

        return sql_creation
