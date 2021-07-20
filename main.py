from sqlite3.dbapi2 import Error
from tkinterUi import UiMainWindow
import tkinter as tk


def main():
    try:
        root = tk.Tk()
        app = UiMainWindow(master=root)
        app.mainloop()
    except Error as err:
        print(err)

if __name__ == '__main__':
    main()