import sqlite3
from sqlite3 import Error

def create_db_connection(db_file):
    """ create a database connection to a SQLite database """
    apo_db = None
    try:
        apo_db = sqlite3.connect(db_file)
    except Error as err:
        print(err)
    finally:
        if apo_db:
            apo_db.close()

def create_ram_db_connection():
    """ create a database connection to a KPI value database"""
    ram_db = None
    try:
        ram_db = sqlite3.connect(':memory:')
        return ram_db
    except Error as err:
        print(err)
    finally:
        if ram_db:
            ram_db.close()

def create_table(apo_db, create_table_sql):
    try:
        cur = apo_db.cursor()
        cur.execute(create_table_sql)
    except Error as err:
        print(err)