import os
import sqlite3
import settings


def create_db(db_name, db_schema_filename):
    """ If file not exist then Create DB file"""
    with sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        if not os.path.exists(db_name):
            with open(db_schema_filename, 'rt') as f:
                schema = f.read()
            conn.executescript(schema)


def set_data(db_name):
    """ Create data """
    if not os.path.exists(db_name):
        create_db(settings.DB_NAME, settings.DB_SCHEMA_FILENAME)
    else:
        with sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()


def get_data(db_name):
    """ Read data """
    if not os.path.exists(db_name):
        create_db(settings.DB_NAME, settings.DB_SCHEMA_FILENAME)
    else:
        with sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()


if __name__ == '__main__':
    pass
