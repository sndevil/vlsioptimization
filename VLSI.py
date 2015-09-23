from functions import * # Outside Of The Class Functions
from logic import *

import globals
import time # Import Time Module For Counter Performance
import datetime # Import Date And Time For Saving Result

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

        if (self.func == Not):
            toprint = "Not"
        print('gate: ' + toprint)             
        
        
    
    

class VLSI:

    variables = []
    func = []

    packname = ''
    firstvar = -1
    secondvar = -1
    outputvar = -1

    
    def __init__(self,string,output,index):
        if check_valid(string):

            self.input=string # Input String
            self.inputnum=input_num(string) # Add Input Number As Attribute
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


            ## !a + !(c+a.d)

            ## detecting and replacing NOTs with variables 
            while (1):
                symbolcounter = 0
                for i in range(0,len(clone)):
                    if clone[i] in "+.^!":
                        symbolcounter +=1
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
                    self.packname = ('#%d' % index)+('#%d#' % self.varcounter)
                    self.varcounter += 1
                    if (symbolcounter == 1):
                        self.outputvar = self.handle_variable(output)
                        out = self.outputvar
                        self.packname = output
                    else:
                        out = self.handle_variable(self.packname)
                    tempfuncobject = funcObject(firstvar = tonot,outputvar = out)
                    self.func.append(tempfuncobject)
                    clone = clone[0:start-1] + self.packname + clone[end:]
                cursor += 1

            cursor = 0
            start = 0
            while (1):
                symbolcounter = 0
                for i in range(0,len(clone)):
                    if clone[i] in "+.^":
                        symbolcounter +=1
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
                    self.packname = ('#%d' % index)+('#%d#' % self.varcounter)
                    self.varcounter+=1
                    if symbolcounter == 1:
                        self.outputvar = self.handle_variable(output)
                        out = self.outputvar
                        self.packname = output
                    else:
                        out = self.handle_variable(self.packname)
                    
                    first = self.handle_variable(temp1)
                    second = self.handle_variable(temp2)
                    
                    tempfuncobject = funcObject(first,out,second,tempfunc)
                    self.func.append(tempfuncobject)
                    clone = clone[0:start] + self.packname + clone[tempcursor:]                       

                    cursor = 0

                cursor += 1
                                
                    
            
           
        ##else:
##            print("Please Enter Valid String")
    def handle_variable(self,string):
        for i in range(0,len(globals.varlist.strlist)):
            if (string == globals.varlist.strlist[i]):
                self.variables.append(i)
                return len(self.variables)-1
        if (string[0] != '#'):
            globals.inputs.ptrlist.append(len(globals.varlist.strlist))
            globals.inputs.strlist.append(string)
        globals.varlist.strlist.append(string)
        globals.varlist.varlist.append(0)
        self.variables.append(len(globals.varlist.varlist) - 1)

        return len(self.variables)-1
    
    def __str__(self):
        #This Function Is For Show Object In Print Format
        return "VLSI("+self.input+")"
    def __repr__(self):
        # Representing VLSI Object
        return "VLSI_Object(Input_String="+self.input+")"

    def function(self):
        result = 0
        self.make_verilog()
        for i in range(0,len(self.func)):
            temp = self.func[i]
            in1 = self.variables[temp.firstvarptr]
            out = self.variables[temp.output]
            if (temp.func != Not):
                globals.varlist.varlist[out] = temp.function(globals.varlist.varlist[in1],globals.varlist.varlist[self.variables[temp.secondvarptr]])
            else:
                globals.varlist.varlist[out] = temp.Notfunction(globals.varlist.varlist[in1])
        return 1

    def make_verilog(self):
        file_name = 'V' + self.packname.replace("#",'')
        verilog_file=open('verilogs/' + file_name +'.v',"w")
        verilog_file.write('module ' + file_name + ' (')
        for v in range(0,len(self.variables)):
            if (v != 0):
                 verilog_file.write(' , ')
            varname = globals.varlist.strlist[self.variables[v]]
            if  (varname[0] == '#'):
                varname = 'V'+varname
            verilog_file.write(varname)
        verilog_file.write('); \n')
        
        #for (f in self.func):
#            f.
        
        verilog_file.close()

        
    
    
