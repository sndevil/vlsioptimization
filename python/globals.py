class Variables:
    varlist = []
    strlist = []
    def __init__(self):
        pass

class inputVars:
    ptrlist = []
    strlist = []
    def __init__(self):
        pass

class Details:
    area = []
    power = []
    timing = []
    leakage = []

def init():
    global varlist, inputs, VLSIlist,table,feedback
    varlist = Variables()
    inputs = inputVars()
    VLSIlist = []
    table = []
    feedback = Details()
