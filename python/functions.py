import string
import globals
import shlex
import subprocess as sub
from multiprocessing import Process,Queue,Pool
valid_input=[1,0,True,False] # Valid Input For Boolean Functions
def input_num(input_str):
    '''
    (VLSI_Object)-> (Input_list,Numer Of Inputs)
'''
    try:
        input_list=[]
        for i in input_str:
            if (i in string.ascii_letters) and (i not in input_list):
                input_list.append(i)
        return len(input_list)
    except:
        print("Please Pass VLSI Object To Function")
        return None
# This Function Count Boolean Operation In Input String Separately
def input_op(input_str):


    try:
        counter=[0,0,0,0]
        input_list=[]
        for i in input_str:
            if i==".":
                counter[0]=counter[0]+1
            elif i=="+":
                counter[1]=counter[1]+1
            elif i=="^":
                counter[2]=counter[2]+1
            elif i=="'":
                counter[3]=counter[3]+1
        return counter   # Return List
    except:
        print("Error In Input")
        return None
                
            
def check_valid(input_string):
    '''
    (Str)->Boolean
'''
    try:
        for i in input_string:
            if i not in string.ascii_letters+ string.digits +"'+^.() #!":
                return False
        return True
    except:
        print("Problem In Input")
        return None
def table_maker(obj):
    pass
def func_creator(obj):
    pass

def script_func(t):
    file_name = 'S' + t.packname.replace("#",'')
    verilog_name = 'F'+ t.packname.replace('#','')
    script_file=open('../scripts/' + file_name +'.scr',"w")
    script_file.write('set power_preserve_rtl_hier_names "true"\n')
    script_file.write('analyze -format verilog { source/Verilogs/' + verilog_name + '.v' +'}\n')
    script_file.write('elaborate ' + verilog_name+'\n')
    script_file.write('link\n')
    script_file.write('uniquify -force\n')
    script_file.write('compile -map_effort medium\n')
    script_file.write('change_names -rules verilog -hierarchy\n')
    script_file.write('write -format verilog -hierarchy -output '+ 'netlist/' + verilog_name + '.v\n')
    script_file.write('uplevel #0 { report_power -analysis_effort low } > Power/' + verilog_name +'.txt\n')
    script_file.write('uplevel #0 { report_area -nosplit } > Area/'+ verilog_name +'.txt\n')
    script_file.close()
    #source_file.write('source scripts/'+ file_name+'.scr\n')
def make_script_files():
    source_file = open('../Source.scr','w')
    source_file.write('set_app_var link_library "/ICIC/180/TSMC/LIB/synopsys/slow.db"\n')
    source_file.write('set_app_var target_library "/ICIC/180/TSMC/LIB/synopsys/slow.db"\n')
    source_file.write('set_app_var target_library "/ICIC/180/TSMC/LIB/synopsys/slow.db"\n')
    writerQueue = Queue()
    #manager=mu.Manager()
    #q=manager.Queue()
    #p=Pool(2)
    #p.map(script_func,globals.VLSIlist)
    #writerQueue=Queue()
    #write_process=Process(target=script_func,args=(writerQueue,globals.VLSIlist))
    #write_process.start()
    for t in globals.VLSIlist:
        file_name = 'S' + t.packname.replace("#",'')
        verilog_name = 'F'+ t.packname.replace('#','')
        with open('../scripts/' + file_name +'.scr',"w") as script_file:
            script_file.write('set power_preserve_rtl_hier_names "true"\n')
            script_file.write('analyze -format verilog { source/Verilogs/' + verilog_name + '.v' +'}\n')
            script_file.write('elaborate ' + verilog_name+'\n')
            script_file.write('link\n')
            script_file.write('uniquify -force\n')
            script_file.write('compile -map_effort medium\n')
            script_file.write('change_names -rules verilog -hierarchy\n')
            script_file.write('write -format verilog -hierarchy -output '+ 'netlist/' + verilog_name + '.v\n')
            script_file.write('uplevel #0 { report_power -analysis_effort low } > Power/' + verilog_name +'.txt\n')
            script_file.write('uplevel #0 { report_area -nosplit } > Area/'+ verilog_name +'.txt\n')
            source_file.write('source scripts/'+ file_name+'.scr\n')
    source_file.write('exit')
    source_file.close()

def read_results():
    for t in globals.VLSIlist:
        name = 'F' + t.packname.replace("#",'')
        area_file=open('../Area/' + name +'.txt',"r")
        power_file=open('../Power/' + name + '.txt',"r")
        report_file=open('../Timing/' + name + '.txt',"r")

        t = ''
        while ('Total cell area:' not in t):
            t = area_file.readline()
        t = t[16:len(t)-2]
        for i in range(0,len(t)):
            if t[i] != ' ':
                break
        t = t[i:]
        area = float(t)
        globals.feedback.area.append(area)

        t = ''
        while ('Total Dynamic Power' not in t):
            t = power_file.readline()
        t = t[20:len(t)-12]
        for i in range(0,len(t)):
            if t[i] != ' ' and t[i] != '=':
                break
        t = t[i:]
        power = float(t)
        globals.feedback.power.append(power)
        power_file.readline()
        t = power_file.readline()
        for i in range(19,len(t)):
            if t[i] != ' ' and t[i] != '=':
                break
        t = t[i:len(t)-3]
        leak = float(t)
        globals.feedback.leakage.append(leak)

        area_file.close()
        power_file.close()
        report_file.close()        
def run_scripts():
    print('running scripts')
    process = sub.Popen('cd ..; dc_shell-xg-t -x "source Source.scr"; rm [F]*;',stdin=sub.PIPE,stdout=sub.PIPE,stderr=sub.PIPE , shell=True)
    result=list(process.communicate())
    command_out=result[0]
    command_error=result[1]
    if len(command_error)!=0:
        print("**Error In DC_SHELL**")
