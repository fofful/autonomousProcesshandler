import sqlite3
from sqlite3 import Error
from config import databaseAddress


def create_db_connection(db_file, create_table_cmd):
    '''create database connection and table if it doesn't exist'''
    try:
        db = sqlite3.connect(db_file)
        cur = db.cursor()
        cur.execute(create_table_cmd)
    except Error as err:
        print(err)
    finally:
        if db:
            db.close()

def write_apo_to_db(table, name, id, kpis, conds, execRule):
    try:
        db = sqlite3.connect(databaseAddress())
        params = (name, id, kpis, conds, execRule)
        sql = 'INSERT INTO {table}(name,id,kpis,conditions,executionRule) VALUES (?, ?, ?, ?, ?)'.format(table=table)
        cur = db.cursor()
        cur.execute(sql, params)
        db.commit()
        print('autonomous process name: ', name,'\nid: ',id , '\ncommitted to table: ', table)
    except Error as err:
        print(err)
    finally:
        if db:
            db.close()

def write_kpi_to_db(table, name, value):
    try:
        db = sqlite3.connect(databaseAddress())
        params = (name, value)
        sql = 'INSERT INTO {table}(name,value) VALUES (?, ?)'.format(table=table)
        cur = db.cursor()
        cur.execute(sql, params)
        db.commit()
        print('KPI: ', name, '\nvalue: ', value, '\ncommitted to table: ', table)
    except Error as err:
        print(err)
    finally:
        if db:
            db.close()

def create_table_if_not_exist(table, variables):
    return '''CREATE TABLE IF NOT EXISTS {table} (
                                        {variables}
                                    );'''.format(table=table, variables=variables)

def printTable(table):
    try:
        db = sqlite3.connect(databaseAddress())
        cur = db.cursor()
        cur.execute('SELECT * FROM {table}'.format(table=table))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as err:
        print(err)
    finally:
        if db:
            db.close()