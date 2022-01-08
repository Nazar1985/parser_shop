import os
import sqlite3
from sqlite3 import Error


def create_schema_db(db_name, db_schema_filename):
    """ If file not exist then Create DB file"""
    with sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        if not os.path.exists(db_name):
            with open(db_schema_filename, 'rt') as f:
                schema = f.read()
            conn.executescript(schema)


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def set_data(conn):
    """ Create data """
    pass


def get_data(conn):
    """ Read data """
    pass


def update_data(conn):
    """ Update data """
    pass


def delete_data(conn):
    """ Delete data """
    pass


if __name__ == '__main__':
    create_schema_db('./temp_and_personal_data/parser.db', 'parser_schema.sql')
    create_connection('./temp_and_personal_data/parser.db')

