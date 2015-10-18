from VLSI import *
from parser2 import *
import platform
import globals
import os       
#input the string to pass to VLSI object list
current_dir=os.getcwd()
test_dir=current_dir+"\\Test"
test_files=os.listdir(test_dir)
for i in range(len(test_files)):
    test_file=open(test_dir+"\\"+test_files[i],"r")
    inputstring=test_file.read()
    input_var_num=input_num(inputstring)
    input_op_num=input_op(inputstring)
    test_file.close()
    print(i+1,test_files[i],input_var_num,input_op_num)
input_command=input("Please Enter One Of This Files Number : (*Any Other = Manual Input) \n")
if int(input_command)<=len(test_files):
    file=open(test_dir+"\\"+test_files[int(input_command)-1],"r")
    print(test_dir+"\\"+test_files[int(input_command)-1])
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
timer_2=time.perf_counter()
make_table()
timer_3=time.perf_counter()
 # End Of Time Performance Counter
today_date=datetime.datetime.today() # Today Date And Local Time For Saving In Performance Text File
parser_perf_time=str(timer_2-timer_1)+" Sec"
table_perf_time=str(timer_3-timer_2)+" Sec"
print("Parser Performance Time: "+parser_perf_time) # Print Time Performance
print("Table Maker Performance Time: "+table_perf_time) # Print Time Performance

###      while (1):

make_script_files()

###     run the scripts
print_result() ## this should be commented

read_results()


### do the proccessing


###      while end


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


result_file=open("Parser_Perf_Result.txt","a") # Open Result File
result_file_2=open("Table_Perf_Result.txt","a")
result_file.write(file_name+" : ,"+"Input Var Number: "+str(input_var_num)+" Input Operation Number: "+str(sum(input_op_num))+" Elapsed Time: "+parser_perf_time+"  "+str(today_date)+" CPU: "+platform.processor()+"\n") # Write Result In File
result_file_2.write(file_name+" : ,"+"Input Var Number: "+str(input_var_num)+" Input Operation Number: "+str(sum(input_op_num))+" Elapsed Time: "+table_perf_time+"  "+str(today_date)+" CPU: "+platform.processor()+"\n") # Write Result In File
result_file.close() # Close Parser Text File
result_file_2.close() # Close Table Maker File


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

                        


       
