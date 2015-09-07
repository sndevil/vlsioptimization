from VLSI import *
from parser import *
import platform
import globals
       
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
input_op_num=input_op(inputstring)

globals.init()

timer_1=time.perf_counter()   # Start Time Of Analysis

parse_string(inputstring)
make_table()

timer_2=time.perf_counter() # End Of Time Performance Counter
today_date=datetime.datetime.today() # Today Date And Local Time For Saving In Performance Text File
perf_time=str(timer_2-timer_1)+" Sec"
print("Performance Time: "+perf_time) # Print Time Performance

print_result()


#print('Variables used:')
#for k in range(0,len(globals.varlist.varlist)):
#        print(str(k))
#        print('value:' + str(globals.varlist.varlist[k]))
#        print('string token:' + globals.varlist.strlist[k])
#        print()

#print('VLSI objects:')
#for temp in globals.VLSIlist:
#    for funcs in temp.func:
#        print('first: ' + str(temp.variables[funcs.firstvarptr]))
#        print('second: ' + str(temp.variables[funcs.secondvarptr]))
#        print('out: ' + str(temp.variables[funcs.output]))
#        funcs.printobj()
#        print('\n')
#    print('next object\n')


#for k in range(0,len(globals.inputs.strlist)):
#        print(str(k))
#        print('value:' + str(globals.inputs.ptrlist[k]))
#        print('string token:' + globals.inputs.strlist[k])
#        print()


result_file=open("Perf_Result.txt","a") # Open Result File
result_file.write(file_name+" : ,"+"Input Var Number: "+str(input_var_num)+" Input Operation Number: "+str(sum(input_op_num))+" Elapsed Time: "+perf_time+"  "+str(today_date)+" CPU: "+platform.processor()+"\n") # Write Result In File
result_file.close() # Close File


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

                        


       
