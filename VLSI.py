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

class funcObject:
    def __init__(self,firstvar,outputvar,secondvar=-1,funct=Not):
        self.func = funct
        self.firstvarptr = firstvar
        self.secondvarptr = secondvar
        self.output = outputvar
        
    def function(self,c,d):
        if (self.func != Not):
            return self.func(c,d)
    def Notfunction(self,ar):
        if (self.func == Not):
            return self.func(ar)
    def printobj(self):
        toprint = ''
        if (self.func == And):
            toprint = "And"
        elif (self.func == Or):
            toprint = "Or"
        elif (self.func == Xor):
            toprint = "Xor"
        elif (self.func == Not):
            toprint = "Not"
        print('gate: ' + toprint)             
        
        
    

varlist = Variables()
inputs = inputVars()
    

class VLSI:

    variables = []
    func = []

    firstvar = -1
    secondvar = -1
    outputvar = -1

    
    def __init__(self,string,output,index):
        if check_valid(string):

            self.input=string # Input String
            self.inputnum=input_num(string) # Add Input Number As Attribute
            self.outputvar = self.handle_variable(output)
            #print(str(self.outputvar))
            #checking for variables and functions in the passed string

            
            self.varcounter = 0

            start = 0
            end = -1
            #start and end of each section
            
            cursor = 0
            clone = string
            clone.replace(" ","")
            #cloning input string

            #inputs should look like this:   (((a+b)+c)+d)
            #not supported yet:    (a+b+c+d)

            ## !a + !(c+a.d)

            ## detecting and replacing NOTs with variables 
            while (1):
                if cursor == len(clone)-1:
                    break
                elif (clone[cursor] == "!"):
                    start = cursor+1
                    tempcursor = cursor +1
                    while (1):
                        if (tempcursor < len(clone)):
                            if clone[tempcursor] in "+.^":
                                break
                            tempcursor += 1
                        if (tempcursor == len(clone)):
                            break

                    end = tempcursor
                    tonot = self.handle_variable(clone[start:end])
                    packname = ('#%d' % index)+('#%d#' % self.varcounter)
                    self.varcounter += 1
                    output = self.handle_variable(packname)
                    tempfuncobject = funcObject(firstvar = tonot,outputvar = output)
                    self.func.append(tempfuncobject)
                    clone = clone[0:start-1] + packname + clone[end:]
                cursor += 1

            cursor = 0
            start = 0
            while (1):
                if cursor == len(clone) - 1:
                    break
                elif clone[cursor] in "+.^":
                    if (clone[cursor] == '+'):
                        tempfunc = Or
                    elif (clone[cursor] == '.'):
                        tempfunc = And
                    elif (clone[cursor] == '^'):
                        tempfunc = Xor
                    else:
                        tempfunc = And
                    
                    end = cursor
                    #detect variable
                    temp1 = clone[start:end]
                    tempcursor = cursor + 1
                    while (clone[tempcursor] not in "+.^" and tempcursor != len(clone)-1):
                        tempcursor += 1
                    if (tempcursor == len(clone) -1):
                        tempcursor += 1
                    temp2 = clone[end+1:tempcursor]
                    packname = ('#%d' % index)+('#%d#' % self.varcounter)
                    self.varcounter+=1
                    output = self.handle_variable(packname)
                    first = self.handle_variable(temp1)
                    second = self.handle_variable(temp2)
                    tempfuncobject = funcObject(first,output,second,tempfunc)
                    self.func.append(tempfuncobject)
                    clone = clone[0:start] + packname + clone[tempcursor:]                       

                    cursor = 0

 
                cursor += 1

            self.func[len(self.func)-1].output = self.outputvar
        
                    
            
           
        ##else:
##            print("Please Enter Valid String")
    def handle_variable(self,string):
        for i in range(0,len(varlist.strlist)):
            if (string == varlist.strlist[i]):
                self.variables.append(i)
                return i
        if (string[0] != '#'):
            inputs.ptrlist.append(len(varlist.strlist))
            inputs.strlist.append(string)
        varlist.strlist.append(string)
        varlist.varlist.append(0)
        self.variables.append(len(varlist.varlist) - 1)

        return len(self.variables)-1
    
    def __str__(self):
        #This Function Is For Show Object In Print Format
        return "VLSI("+self.input+")"
    def __repr__(self):
        # Representing VLSI Object
        return "VLSI_Object(Input_String="+self.input+")"

    def function(self):
        result = 0
        for i in range(0,len(self.func)):
            temp = self.func[i]
            in1 = self.variables[temp.firstvarptr]
            out = self.variables[temp.output]
            if (temp.func != Not):
                varlist.varlist[out] = temp.function(varlist.varlist[in1],varlist.varlist[self.variables[temp.secondvarptr]])
            else:
                varlist.varlist[out] = temp.Notfunction(varlist.varlist[in1])
        return 1
            

VLSIlist = []


def calculate_result():
    for temp in VLSIlist:
        while (not temp.function()):
            pass

    return str(varlist.varlist[VLSIlist[len(VLSIlist)-1].outputvar])
        
    
    

        
    
    
