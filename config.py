def apoTable():
    return 'apoTable'

def KpiTable():
    return 'kpiTable'

def databaseAddress():
    return './databases/test.db'

def createKpiTable():
    return 'name text NOT NULL, value text NOT NULL'

def createApoTable():
    return 'name text NOT NULL, id text NOT NULL, kpis text NOT NULL, conditions text NOT NULL, executionRule text NOT NULL'