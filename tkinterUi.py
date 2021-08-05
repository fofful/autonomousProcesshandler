from sqlite3.dbapi2 import Error
import tkinter as tk
from apoClass import autonomousProcessObject
from sqliteFunctions import get_table_values, write_apo_to_db, write_kpi_to_db
from config import apoTable, KpiTable

class UiCreateApos(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='name')
        self.label.pack()
        
        self.entryName = tk.Entry(self)
        self.entryName.pack()

        self.label = tk.Label(self, text='kpis (comma separated)\n"kpi01,kpi02, ..."')
        self.label.pack()
        self.entryKpis = tk.Entry(self)
        self.entryKpis.pack()

        self.label = tk.Label(self, text='conditions (comma separated)\n"==1.33,>=7, ..."')
        self.label.pack()
        self.entryConditions = tk.Entry(self)
        self.entryConditions.pack()

        self.label = tk.Label(self, text='execution rule\n"kpi01,and,kpi02"')
        self.label.pack()
        self.entryExecRule = tk.Entry(self)
        self.entryExecRule.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'create'
        self.button['command'] = self.storeApo
        self.button.pack()

        self.quit = tk.Button(self, text='close', fg='red', command=self.master.destroy)
        self.quit.pack(side='right')

    def storeApo(self):
        try:
            name = self.entryName.get()
            kpis = self.entryKpis.get()
            conds = self.entryConditions.get()
            execRule = self.entryExecRule.get()
            apo = autonomousProcessObject(name, kpis, conds, execRule)
            write_apo_to_db(apoTable(), apo.name, apo.id, apo.kpis, apo.conditions, apo.executionRule)
            
        except Error as err:
            print('apo_db error: ', err)


class UiSetKpiValues(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='kpi name')
        self.label.pack()
        self.entryName = tk.Entry(self)
        self.entryName.pack()

        self.label = tk.Label(self, text='value')
        self.label.pack()
        self.entryValue = tk.Entry(self)
        self.entryValue.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'create'
        self.button['command'] = self.setKpiValue
        self.button.pack()

        self.quit = tk.Button(self, text='close', fg='red', command=self.master.destroy)
        self.quit.pack(side='right')

    def setKpiValue(self):
        try:
            kpi_db = KpiTable()
            name = self.entryName.get()
            value = self.entryValue.get()
            write_kpi_to_db(kpi_db, name, value)
        except Error as err:
            print('kpi_db error: ', err)
        

class MonitorKpis(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='Main window')
        self.label.pack()
        
        self.quit = tk.Button(self, text='close', fg='red', command=self.master.destroy)
        self.quit.pack(side='right')


class UiMainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='--------- Main window ---------\n')
        self.label.pack()
        
        self.button = tk.Button(self)
        self.button['text'] = 'create autonomous process'
        self.button['command'] = self.createApo
        self.button.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'initialize KPI values'
        self.button['command'] = self.setKpiValues
        self.button.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'monitor KPI\'s'
        self.button['command'] = self.monitorKpis
        self.button.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'print apo db'
        self.button['command'] = self.printApoTable
        self.button.pack()

        self.quit = tk.Button(self, text='close', fg='red', command=self.master.destroy)
        self.quit.pack(side='right')

    def createApo(self):
        root = tk.Tk()
        app = UiCreateApos(master=root)
        app.mainloop()

    def setKpiValues(self):
        root = tk.Tk()
        app = UiSetKpiValues(master=root)
        app.mainloop()

    def monitorKpis(self):
        root = tk.Tk()
        app = MonitorKpis(master=root)
        app.mainloop()
    
    def printApoTable(self):
        rows = get_table_values(apoTable())
        for row in rows:
            print(row)

    def printKpiTable(self):
        rows = get_table_values(apoTable())
        for row in rows:
            print(row)