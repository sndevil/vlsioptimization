import string
def input_num(obj):
    '''
    (VLSI_Object)-> (Input_list,Numer Of Inputs)
'''
    try:
        input_list=[]
        for i in obj.input:
            if (i in string.ascii_letters) and (i not in input_list):
                input_list.append(i)
        return (input_list,len(input_list))
    except:
        print("Please Pass VLSI Object To Function")
        return None
def check_valid(input_string):
    '''
    (Str)->Boolean
'''
    try:
        for i in input_string:
            if i not in string.ascii_letters+ string.digits +"'+^.()#":
                return False
        return True
    except:
        print("Problem In Input")
        return None
def table_maker(obj):
    pass
def func_creator(obj):
    pass

def And(a,b):
    return a and b

def Or(a,b):
    return a or b

def Xor(a,b):
    if (a == b):
        return false
    else:
        return true
def Not(a):
    return not(a)
    
def Nand(a,b):
    
    return not(a and b)

def Nor(a,b):
    return not(a or b)

def Xnor(a,b):
    return not(Xor(a,b))
