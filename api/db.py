'''
Setup SQLite DB

Executing this file will bootstrap the DB.
'''

import sqlite3

DB_NAME = 'movies.db'
SCHEMA = 'schema.sql'


def get_conn():
    '''
    Retrieives a DB connection.
    '''

    return sqlite3.connect(DB_NAME, )


def init_db():
    '''
    Initializes the DB with schema.
    '''

    db = get_conn()

    with db:
        schema_file = open(SCHEMA)
        db.executescript(schema_file.read())


if __name__ == '__main__':
    init_db()
    print('>>> Initialized DB ...')
