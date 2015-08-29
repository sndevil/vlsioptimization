from functions import * # Outside Of The Class Functions
from logic import *
import time # Import Time Module For Counter Performance
import datetime # Import Date And Time For Saving Result
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
    

varlist = Variables()
inputs = inputVars()
    

class VLSI:

    firstvar = -1
    secondvar = -1
    outputvar = -1

    
    def __init__(self,string,output):
        if check_valid(string):
            #  print(string)
            self.input=string # Input String
            self.inputnum=input_num(string) # Add Input Number As Attribute

            #checking for variables and functions in the passed string

            start = 0
            end = -1
            #start and end of each section
            
            cursor = 0
            clone = string
            #cloning input string

            #inputs should look like this:   (((a+b)+c)+d)
            #not supported yet:    (a+b+c+d)
            
            while (1):
                if clone[cursor] in "+.^":
                    end = cursor
                    #detect variable
                    temp1 = clone[start:end]
                    temp2 = clone[end+1:]
                    
                    for i in range(0,len(varlist.strlist)):
                        if (temp1 == varlist.strlist[i]): #first var exists
                            self.firstvar = i #link to existing
                        if (temp2 == varlist.strlist[i]):
                            self.secondvar = i
                        if (output == varlist.strlist[i]):
                            self.outputvar = i
                    if (self.firstvar == -1): #first var is a new var
                        if (temp1[0] != '#'):
                            inputs.ptrlist.append(len(varlist.strlist))
                            inputs.strlist.append(temp1)
                        varlist.strlist.append(temp1)
                        varlist.varlist.append(0)
                        self.firstvar = len(varlist.varlist) - 1
                    if (self.secondvar == -1): #second var is a new var
                        if (temp2[0] != '#'):
                            inputs.ptrlist.append(len(varlist.strlist))
                            inputs.strlist.append(temp2)
                        varlist.strlist.append(temp2)
                        varlist.varlist.append(0)
                        self.secondvar = len(varlist.varlist) - 1
                    if (self.outputvar == -1):
                        varlist.strlist.append(output)
                        varlist.varlist.append(0)
                        self.outputvar = len(varlist.varlist) - 1
    
                    break
                cursor += 1
        
                    
            
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

    def function(self):
        varlist.varlist[self.outputvar] = self.func(a = varlist.varlist[self.firstvar],b = varlist.varlist[self.secondvar])

VLSIlist = []


def calculate_result():
    for temp in VLSIlist:
        temp.function()

    return str(varlist.varlist[VLSIlist[len(VLSIlist)-1].outputvar])
        
    
    

        
    
    
