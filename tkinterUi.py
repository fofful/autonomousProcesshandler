import tkinter as tk


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

        self.label = tk.Label(self, text='execution rule\n"kpi01 and kpi02"')
        self.label.pack()
        self.entryExecrule = tk.Entry(self)
        self.entryExecrule.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'create'
        self.button['command'] = self.storeApo
        self.button.pack()

        self.quit = tk.Button(self, text='close', fg='red', command=self.master.destroy)
        self.quit.pack(side='right')

    def storeApo(self):
        print('work in progress..')


class UiInitKpis(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='name')
        self.label.pack()
        
        self.entryName = tk.Entry(self)
        self.entryName.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'create'
        self.button['command'] = self.storeApo
        self.button.pack()

        self.quit = tk.Button(self, text='close', fg='red', command=self.master.destroy)
        self.quit.pack(side='right')

    def storeApo(self):
        print('work in progress..')


class UiMainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text='Main window')
        self.label.pack()
        
        self.button = tk.Button(self)
        self.button['text'] = 'create autonomous process'
        self.button['command'] = self.createApo
        self.button.pack()

        self.button = tk.Button(self)
        self.button['text'] = 'initialize kpi values'
        self.button['command'] = self.initKpis
        self.button.pack()

        self.quit = tk.Button(self, text='close', fg='red', command=self.master.destroy)
        self.quit.pack(side='right')

    def createApo(self):
        root = tk.Tk()
        app = UiCreateApos(master=root)
        app.mainloop()

    def initKpis(self):
        root = tk.Tk()
        app = UiInitKpis(master=root)
        app.mainloop()

root = tk.Tk()
app = UiMainWindow(master=root)
app.mainloop()
app.mainloop()