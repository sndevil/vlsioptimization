from VLSI import *
       
#input the string to pass to VLSI object list
input_command=input("Please Enter One Of This : \n 1.Test_Case1 \n 2.Test_Case2 \n 3.Test_Case3 \n Any Other : Manual Input \n")
if int(input_command)==1:
    file=open("Test_Case1.txt","r")
    file_name=file.name
    inputstring=file.read()
    file.close()
elif int(input_command)==2:
    file=open("Test_Case2.txt","r")
    file_name=file.name
    inputstring=file.read()
    file.close()
elif int(input_command)==3:
    file=open("Test_Case3.txt","r")
    file_name=file.name
    inputstring=file.read()
    file.close()
else:
    inputstring=input("Please Enter Function : ")
    file_name="Manual Function"
input_var_num=input_num(inputstring)
    

timer_1=time.perf_counter()   # Start Time Of Analysis  
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
timer_2=time.perf_counter() # End Of Time Performance Counter
today_date=datetime.datetime.today() # Today Date And Local Time For Saving In Performance Text File
perf_time=str(timer_2-timer_1)+" Sec"
print("Performance Time: "+perf_time) # Print Time Performance
result_file=open("Perf_Result.txt","a") # Open Result File
result_file.write(file_name+" : ,"+"Input Var Number: "+str(input_var_num)+"Elapsed Time: "+perf_time+"  "+str(today_date)+"\n") # Write Result In File
result_file.close() # Close File

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
                        


       
