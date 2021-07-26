from sqlite3.dbapi2 import Error
from tkinterUi import UiMainWindow
import tkinter as tk
from sqliteFunctions import create_db_connection, create_ram_db_connection
from autonomousExecutor import autonomousExecutorLoop
import threading

def main():

    database = './databases/apodatabase.db'
    tableName = 'testtable'
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS {table} (
                                        name text NOT NULL,
                                        id text NOT NULL,
                                        kpis text NOT NULL,
                                        conditions text NOT NULL,
                                        executionRule text NOT NULL
                                    ); """.format(table=tableName)

    try:
        create_db_connection(database, sql_create_projects_table)
        autonomousExecutorLoop()
        root = tk.Tk()
        task02 = UiMainWindow(master=root)
        task02.mainloop()
        

    except Error as err:
        print(err)
    finally:
        print('app closed')

if __name__ == '__main__':
    main()