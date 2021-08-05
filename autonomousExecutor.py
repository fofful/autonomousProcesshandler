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
                kpiNames = apo[2].split(',')
                kpiConditions = apo[3].split(',')            
                kpiAndRuleArray = list(map(lambda kpi, rule: kpi + rule, kpiNames, kpiConditions))
                execRule = apo[4]

                for kpiAndRule in kpiAndRuleArray:
                    for kpiValueTuple in kpisTable:
                        if kpiValueTuple[0] in kpiAndRule:
                            execRule = execRule.replace(kpiValueTuple[0], kpiAndRule)
                            execRule = execRule.replace(kpiValueTuple[0], kpiValueTuple[1])
                execRule = execRule.replace(',', ' ')  
                print('kpiandrule: ', kpiAndRuleArray)
                print('execRule: ', execRule)
                print(apo[0], 'evaluates: ', eval(execRule))

                

            #print(kpisTable)
            #print(aposTable)
            time.sleep(2)



