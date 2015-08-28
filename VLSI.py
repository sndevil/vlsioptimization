from functions import * # Outside Of The Class Functions
from logic import *
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
            self.inputnum=input_num(self) # Add Input Number As Attribute

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
        
    
    
           
#input the string to pass to VLSI object list
inputstring = input("enter the logic function string:\n")

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
    elif (i == len(temp) -1):
        start = 0
        end = len(temp) - 1
        indexcounter += 1
        packname = ('#%d#' % indexcounter)
        tempobject = VLSI(temp,packname)
        VLSIlist.append(tempobject)
        break
        
    if (start >= 0):
        indexcounter+=1
        temp1 = temp[start+1:end]
        packname = ('#%d#' % indexcounter) #    (a+b) -> #indexcounter# and is saved as a var 
        tempobject = VLSI(temp1,packname)
        VLSIlist.append(tempobject)
        temp = temp[:start]+('#%d#' % (indexcounter)) + temp[end+1:]
        start = -2
        end = -1
        i = 0

 
    i+=1

outstr = ''
for i in inputs.strlist:
    outstr += i

print (outstr+ '   Out') 

for counter in range(0,2**(len(inputs.strlist))):
    temp = counter
    outstr = ''
    for i in range(0,len(inputs.strlist)):
        #inputstr = input(inputs.strlist[i] + " = ")
        outstr += str(temp%2)
        varlist.varlist[inputs.ptrlist[i]] = int(temp%2)
        temp =int(temp/ 2)

    outstr += '   ' + calculate_result()
    counter+=1
    print(outstr)

#
#print('Variables used:')
#for k in range(0,len(varlist.varlist)):
#        print(str(k))
#        print('value:' + str(varlist.varlist[k]))
#        print('string token:' + varlist.strlist[k])
#        print()

#for k in range(0,len(inputs.strlist)):
#        print(str(k))
#        print('value:' + str(inputs.ptrlist[k]))
#        print('string token:' + inputs.strlist[k])
#        print()

#print ('gates used:')
#for i in range(0,indexcounter):
#    print("input variables" + str(i) + ": " + str(VLSIlist[i].firstvar) + " , " + str(VLSIlist[i].secondvar) )
#    print("output variable: " + str(VLSIlist[i].outputvar))
#    if VLSIlist[i].funcindex == 0:
#        print('func: or')
#    if VLSIlist[i].funcindex == 1:
#        print('func: and')
#    if VLSIlist[i].funcindex == 2:
#        print('func: xor')
#    if VLSIlist[i].funcindex == 3:
#        print('func: not')
#    print ()
                        


       
        
    
    
