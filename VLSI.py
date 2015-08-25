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
            if i not in string.ascii_letters+"'+^.":
                return False
        return True
    except:
        print("Problem In Input")
        return None
def table_maker(obj):
    pass
def func_creator(obj):
    pass


class VLSI:
    def __init__(self,string):
        if check_valid(string):
             self.input=string # Input String
             self.func=None   # Converted Boolean Function
             self.inputnum=None # Number Of Inputs
        else:
            print("Please Enter Valid String")
    def __str__(self):
        #This Function Is For Show Object In Print Format
        return "VLSI("+self.input+")"
    def __repr__(self):
        # Representing VLSI Object
        return "VLSI_Object(Input_String="+self.input+")"
        
            
       
        
    
    
