import threading
import time
from config import KpiTable, apoTable
from sqliteFunctions import get_table_values

class autonomousExecutorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def terminate(self):
        self.running = False

    def run(self):
        while self.running:
            kpisTable = get_table_values(KpiTable())
            aposTable = get_table_values(apoTable())

            for apo in aposTable:
                print(apo[4])
                execRule = apo[4]
                execRule = execRule.replace(',', ' ')
                kpiNames = apo[2].split(',')
                for kpiName in kpiNames:
                    execRule = execRule.replace(kpiName, '{' + kpiName + '}')
                kpiConditions = apo[3].split(',')
                for kpi in kpisTable:
                    print('to be continued...')

                

            print(kpisTable)
            #print(aposTable)
            time.sleep(2)



