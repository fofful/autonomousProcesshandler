from sqlite3.dbapi2 import Error
from tkinterUi import UiMainWindow
import tkinter as tk
from sqliteFunctions import create_db_connection
from sqliteFunctions import create_table_if_not_exist
from autonomousExecutor import autonomousExecutorThread
from config import apoTable, KpiTable, databaseAddress, createKpiTable, createApoTable

def main():

    try:
        create_db_connection(databaseAddress(), create_table_if_not_exist(apoTable(), createApoTable()))
        create_db_connection(databaseAddress(), create_table_if_not_exist(KpiTable(), createKpiTable()))
        apoExecThread = autonomousExecutorThread()
        apoExecThread.start()
        
        root = tk.Tk()
        uitask = UiMainWindow(master=root)
        uitask.mainloop()
        
    except Error as err:
        print(err)

    finally:
        apoExecThread.terminate()
        apoExecThread.join()
        print('app closed')

if __name__ == '__main__':
    main()