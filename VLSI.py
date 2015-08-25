#import LogicToken
from functions import * # Outside Of The Class Functions
from logic import *
class Variables:
    varlist = []
    strlist = []
    def __init__(self):
        pass

varlist = Variables()
    

class VLSI:
    
    def __init__(self,string):
        if check_valid(string):
            #  print(string)
            self.input=string # Input String
            self.inputnum=input_num(self) # Add Input Number As Attribute
            if string.find('+')!=-1:
                self.func = Or
                self.funcindex = 0
            elif string.find('.')!=-1:
                self.func = And
                self.funcindex = 1
            elif string.find('^')!=-1:
                self.func = Xor
                self.funcindex = 2
            elif string.find('!')!=-1:
                self.func = Not
                self.funcindex = 3
            else:
                self.func=None# Converted Boolean Function
                self.funcindex = -1
        else:
            print("Please Enter Valid String")
    def __str__(self):
        #This Function Is For Show Object In Print Format
        return "VLSI("+self.input+")"
    def __repr__(self):
        # Representing VLSI Object
        return "VLSI_Object(Input_String="+self.input+")"

            
#input the string to pass to VLSI object list
inputstring = input("enter the logic function string")

VLSIlist = []

start = -2
end = -1
indexcounter = 0
i = 0
j = 0

temp = inputstring
temp.replace(" ",'')

while (i < len(temp)):
    if (temp[i] == ')'):
        end = i
        j = i
        while (j >= 0):
            if (temp[j] == '('):
                start = j
                break
            else:
                j-=1
        
        if (start < 0):
            break

    if (start >= 0):
        indexcounter+=1
        temp1 = temp[start+1:end]
        tempobject = VLSI(temp1)
        VLSIlist.append(tempobject)
        print(tempobject.func)
        temp = temp[:start]+('#%d#' % (indexcounter)) + temp[end+1:]
        if not(i==0) and not(j==0):
            print('start: ' + str(start) + ' end: ' + str(end))
            print(temp)
        start = -2
        end = -1
        i = 0

    print('tempbefore:' + temp)
    #if not(end == len(temp)):
    #    end += 
 
    i+=1

for i in range(0,indexcounter):
    print(VLSIlist[i])
    if VLSIlist[i].funcindex == 0:
        print('func: or')
    if VLSIlist[i].funcindex == 1:
        print('func: and')
    if VLSIlist[i].funcindex == 2:
        print('func: xor')
    if VLSIlist[i].funcindex == 3:
        print('func: not')
                        


       
        
    
    
