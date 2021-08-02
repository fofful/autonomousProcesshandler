import threading
import time
from config import databaseAddress, KpiTable
from sqliteFunctions import create_db_connection

class autonomousExecutorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def terminate(self):
        self.running = False

    def run(self):
        while self.running:
            print('kieno')
            time.sleep(2)



