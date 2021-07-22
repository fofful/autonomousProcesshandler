import sqlite3
from sqlite3 import Error

def create_db_connection(db_file, create_table_cmd):
    """ create a database connection and table if it doesn't exixt to an SQLite database """
    try:
        apo_db = sqlite3.connect(db_file)
        create_table(apo_db, create_table_cmd)
    except Error as err:
        print(err)
    finally:
        if apo_db:
            apo_db.close()

def write_apo_to_db(table, name, id, kpis, conds, execRule):
    try:
        apo_db = sqlite3.connect('./databases/apodatabase.db')
        params = (name, id, kpis, conds, execRule)
        sql = 'INSERT INTO {table}(name,id,kpis,conditions,executionRule) VALUES (?, ?, ?, ?, ?)'.format(table=table)
        cur = apo_db.cursor()
        cur.execute(sql, params)
        apo_db.commit()
        print('autonomous process ', id, ' committed to table: ', table)

    except Error as err:
        print(err)
    finally:
        if apo_db:
            apo_db.close()

def close_db_connection(db_file):
    try:
        db_file.close()
    except Error as err:
        print(err)

def create_ram_db_connection():
    """ create a database connection to a KPI value database"""
    try:
        ram_db = sqlite3.connect(':memory:')
    except Error as err:
        print(err)
    finally:
        if ram_db:
            ram_db.close()

def close_ram_connection(db_file):
    try:
        db_file.close()
    except Error as err:
        print(err)

def create_table(apo_db, create_table_sql):
    try:
        cur = apo_db.cursor()
        cur.execute(create_table_sql)
    except Error as err:
        print(err)