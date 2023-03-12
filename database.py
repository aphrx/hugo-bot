import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def setup_db():
    conn = create_connection('data.db')
    if conn is not None:
        sql = """ CREATE TABLE IF NOT EXISTS tokens (
                    id integer PRIMARY KEY,
                    user text NOT NULL,
                    category text NOT NULL,
                    token text NOT NULL
                ); """
        create_table(conn, sql)
    return conn
   