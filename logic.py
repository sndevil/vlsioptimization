def And(a,b):
    if (a in valid_input and b in valid_input):
        return a and b
    else:
        print("Input Is Not Boolean")
        return None

def Or(a,b):
    if (a in valid_input and b in valid_input):
        return a or b
    else:
        print("Input Is Not Boolean")
        return None

def Xor(a,b):
    if (a in valid_input and b in valid_input): 
        if (a == b):
            return False
        else:
            return True
    else:
        print("Input Is Not Boolean")
        return None
def Not(a):
    if a in valid_input:
        return not(a)
    else:
        print("Input Is Not Boolean")
        return None
    
def Nand(a,b):
    return Not(And(a,b))

def Nor(a,b):
    return Not(Or(a,b))

def Xnor(a,b):
    return not(Xor(a,b))

