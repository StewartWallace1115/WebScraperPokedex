"""
Downloads file from Poke API
"""


class PokemonWriter:
    """
    Downloads JSON file from Poke API endpoint
    """

    @classmethod
    def convert_pokemon_json_to_sql(cls, pokemon_json):

        """
        Parse pokemon json to remove unnecessary data and extract moves set
        """
        return pokemon_json
    

    @classmethod
    def create_table(cls, table_name, columns):

        column_name = 0
        column_datatype = 1
        sql_creation_string = "CREATE TABLE " + table_name + " ("

        for column in columns:
            sql_creation_string = sql_creation_string + "\t" + column[column_name] + \
            " " + column[column_datatype] + ",\n"

        # Remove the last comma. Not needed for last column
        last_comma_index = sql_creation_string.rfind(',')
        sql_creation_string = sql_creation_string[0 : last_comma_index : ] + sql_creation_string[last_comma_index + 1 : :]
        
        sql_creation_string = sql_creation_string + ");\n"

        return sql_creation_string
    
    @classmethod
    def create_primary_keys(cls,keys_tables, sql_creation_string):
        for key_table in keys_tables:
            sql_creation_string = sql_creation_string + "ALTER TABLE " + key_table[0] +\
                             " ADD PRIMARY KEY (" + key_table[1] + ");\n"
        
        return sql_creation_string

    @classmethod
    def create_relationships(cls, keys_tables, sql_creation_string):

        for key_table in keys_tables:
            sql_creation_string = sql_creation_string + "ALTER TABLE " + key_table[0] + \
            " ADD FOREIGN KEY (" +key_table[1] + ") REFERENCES " + key_table[2] + " (" +key_table[3] + ");\n"
 
        return sql_creation_string

    @classmethod
    def populate_table(cls, values, table_name, sql_creation_string):

        value_string = "("
        for value in values:
            value_string = value_string + value +", "

        # Remove the last comma. Not needed for last column
        last_comma_index = value_string.rfind(',')
        value_string = value_string[0 : last_comma_index : ] + value_string[last_comma_index + 1 : :]

        value_string = ")"
        sql_creation_string = "INSERT INTO "+ table_name + " VALUES " + value_string 
 
        return sql_creation_string

        
