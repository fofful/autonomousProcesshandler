import random
from sre_constants import FAILURE
import time

random.seed(None)

class autonomousProcessObject:
    
    def __init__(self, name_, kpis_, conditions_, executionRule_):
        
        self.name = name_
        self.id = createId()
        self.kpis = kpis_
        self.conditions = conditions_
        self.executionRule = validateExecCondition(kpis_, executionRule_)


def createId():
    
    id = ""
    charArray = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(5):
        id += charArray[random.randint(0, len(charArray)-1)]
    id +=  '-' + str(time.time())
    return id


def validateExecCondition(kpis_, executionRule_):

    tempExecutionRule = executionRule_
    booleanArray = ['and', 'or' ,';']
    charArray = ['(', ')']

    for kpi in kpis_:
        tempExecutionRule = tempExecutionRule.replace(kpi, '')
    for booleanTerm in booleanArray:
        tempExecutionRule = tempExecutionRule.replace(booleanTerm, '')
    for char in charArray:
        tempExecutionRule = tempExecutionRule.replace(char, '')
    if len(tempExecutionRule) == 0:
        print('validation success')
        return executionRule_
    else:
        print('validation failure')
        return FAILURE