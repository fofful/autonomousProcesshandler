import sqlite3
from sqlite3 import Error

APODATABASEADDRESS = './databases/apodatabase.db'

def create_db_connection(db_file, create_table_cmd):
    '''create a database connection and table if it doesn't exist to an SQLite database'''
    try:
        apo_db = sqlite3.connect(db_file)
        cur = apo_db.cursor()
        cur.execute(create_table_cmd)
    except Error as err:
        print(err)
    finally:
        if apo_db:
            apo_db.close()

def write_apo_to_db(table, name, id, kpis, conds, execRule):
    try:
        apo_db = sqlite3.connect(APODATABASEADDRESS)
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

def create_ram_db_connection():
    try:
        ram_db = sqlite3.connect(':memory:')
    except Error as err:
        print(err)
    finally:
        return ram_db

def write_kpi_to_db(ram_db, kpiName, value):
    try:
        params = (kpiName, value)
        cur = ram_db.cursor()
        cur.execute('SELECT {kpiName} FROM')
    except Error as err:
        print(err)
    finally:
        if ram_db:
            ram_db.close()

def printApos():
    try:
        apo_db = sqlite3.connect(APODATABASEADDRESS)
        cur = apo_db.cursor()
        cur.execute('SELECT * FROM testtable')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as err:
        print(err)
    finally:
        if apo_db:
            apo_db.close()