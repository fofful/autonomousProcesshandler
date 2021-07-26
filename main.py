from sqlite3.dbapi2 import Error
from tkinterUi import UiMainWindow
import tkinter as tk
from sqliteFunctions import create_db_connection
from sqliteFunctions import create_ram_db_connection

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
        create_ram_db_connection()
        root = tk.Tk()
        app = UiMainWindow(master=root)
        app.mainloop()
    except Error as err:
        print(err)
    finally:
        print('app closed')

if __name__ == '__main__':
    main()