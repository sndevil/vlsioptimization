import string
valid_input=[1,0,True,False] # Valid Input For Boolean Functions
def input_num(input_str):
    '''
    (VLSI_Object)-> (Input_list,Numer Of Inputs)
'''
    try:
        input_list=[]
        for i in input_str:
            if (i in string.ascii_letters) and (i not in input_list):
                input_list.append(i)
        return len(input_list)
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
