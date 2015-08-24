import string
def input_num(obj):
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
    for i in input_string:
        if i not in string.ascii_letters+"'+^.":
            return False
    return True

class VLSI:
    def __init__(self,string):
        if check_valid(string):
             self.input=string
             self.func=None
        else:
            print("Please Enter Valid String")
    def __str__(self):
        return "VLSI("+self.input+")"
    def __repr__(self):
        return "VLSI_Object(Input_String="+self.input+")"
        
            
       
        
    
    
