import os
import sys
from termcolor import colored
import subprocess
sys.path.append('.')

class RunnableApp(object):

    
    def __init__(self,AppCompletePath):
        self.isapp = True

        if("\\" in AppCompletePath):
            print(colored('Incorrect / form:   Try replacing \\ to /','red'))
            self.isapp = False
            if(AppCompletePath.endswith("/")):
                print(colored('Path should not end with /:     Try to remove ending /','red'))

        name = os.path.basename(AppCompletePath)

        if('.' not in name):
            print(colored('Path should include extension:    Try to write the ".ext" at the end','red'))
            self.isapp = False
        if(self.isapp):   
            self.PATH = AppCompletePath 
            self.NAME = name
#
            #os.path.basename(self.PATH)
            #command = f'REG QUERY "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /t "REG_SZ" /v {name.replace(".exe","")}'
            #res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            #print(colored(res.stdout.readline(),'magenta'))
            #Makes reference to the autorun propertie of each program

        else:
            print(colored('INSTANCE SKIPPED DUE TO PREV FAIL', 'red'))

        cmd_path = 'HKEY_USERS\S-1-5-21-4108893222-2288396013-2005981722-1001\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run'
        cmd_in = f'REG QUERY "{cmd_path}" /t REG_BINARY /v {self.NAME.replace(".exe","")}'
        cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        cmd_out_string = str(cmd_out.stdout.read())
        cmd_out_string = cmd_out_string.replace("\\","/").replace("//","/")
        cmd_out_string = cmd_out_string.replace(cmd_path.replace('\\','/'),'')
        cmd_out_string = cmd_out_string.replace("b'",'').replace('/r/n','').replace('   ','#').replace('Fin','#')#.replace('###','')
        values = cmd_out_string.split('#')
        state_value = values[3]
        state_value =state_value.replace(' ', '')
        #print(colored(cmd_path.replace("\\","\\"), 'magenta'))
        #print(colored(f'CMD_IN: {cmd_in}', 'cyan'))
        #print(colored(f'CMD_OUT: {cmd_out}', 'cyan'))
        #print(colored(f'CMD_OUT_STRING: {cmd_out_string}', 'cyan'))
        print(colored(f'STATE_VALUE: {state_value}', 'magenta'))
        
        
        if(state_value.startswith('00')):
            #print(colored('ENABLED', 'magenta'))
            self.STATE = 'enabled'
        elif (state_value.startswith('01')):
            #print(colored('DISABLED ', 'magenta'))
            self.STATE = 'disabled'
        elif (state_value.startswith('02')):
            #print(colored('DISABLED ', 'magenta'))
            self.STATE = 'disabled'
        elif (state_value.startswith('03')):
            #print(colored('DISABLED ', 'magenta'))
            self.STATE = 'disabled'
        else:
            print(colored(f'Could not recognize appState: {cmd_out_string}', 'red'))
            self.STATE = 'none'

    def toString(self):
        print(colored(f'NAME: {self.NAME}\nPATH: {self.PATH}\nSTATE: {self.STATE}', 'green'))

#
    # def isAutoRunnable(self):
    #     cmd_path = 'HKEY_USERS\S-1-5-21-4108893222-2288396013-2005981722-1001\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run'
    #     cmd_in = f'REG QUERY "{cmd_path}" /t REG_BINARY /v {self.NAME.replace(".exe","")}'
    #     cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    #     cmd_out_string = str(cmd_out.stdout.read())
    #     cmd_out_string = cmd_out_string.replace("\\","/").replace("//","/")
    #     cmd_out_string = cmd_out_string.replace(cmd_path.replace('\\','/'),'')
    #     cmd_out_string = cmd_out_string.replace("b'",'').replace('/r/n','').replace('   ','#').replace('Fin','#')#.replace('###','')
    #     values = cmd_out_string.split('#')
    #     state_value = values[3]
    #     state_value =state_value.replace(' ', '')
    #     #print(colored(cmd_path.replace("\\","\\"), 'magenta'))
    #     #print(colored(f'CMD_IN: {cmd_in}', 'cyan'))
    #     #print(colored(f'CMD_OUT: {cmd_out}', 'cyan'))
    #     #print(colored(f'CMD_OUT_STRING: {cmd_out_string}', 'cyan'))
    #     print(colored(f'STATE_VALUE: {state_value}', 'magenta'))
        
    #     if(state_value.startswith('00')):
    #         #print(colored('ENABLED', 'magenta'))
    #         self.STATE = 'enabled'
    #     elif (state_value.startswith('01')):
    #         #print(colored('DISABLED ', 'magenta'))
    #         self.STATE = 'disabled'
    #     elif (state_value.startswith('02')):
    #         #print(colored('DISABLED ', 'magenta'))
    #         self.STATE = 'disabled'
    #     elif (state_value.startswith('03')):
    #         #print(colored('DISABLED ', 'magenta'))
    #         self.STATE = 'disabled'
    #     else:
    #         print(colored(f'Could not recognize appState: {cmd_out_string}', 'red'))
    #         self.STATE = 'none'

class WindowsInteractuable(object):
    def __init__(self,name):
        self.name = name 
        print('Object instanced')
    #NON SELF METHODS

    def RunOnStartApps(self): 
        cmd_in = 'REG QUERY HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
        cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        return cmd_out 

    def stdoutTOarray(self,cmd_out):
        cmd_out_converted = []
        for line in cmd_out.stdout.readlines():
            if(line != ''):
                line = str(line).replace("b'",'').replace("\\r\\n'",'')
                line = line.replace('    ', '#').replace('\\','/').replace('//','/')
                line = line.replace('" ','#').replace('"','')
                line = line.replace(' -','#-')
                if(line != ''):
                    cmd_out_converted.append(line)
                else:
                    print('Skipping due to being a null line')
        return cmd_out_converted  

    def getproperties(self,object):
        object_props = str(object).split('#')
        return object_props

    def toRunnableApp(self,appsarray):      
        # NEEDS A stdoutTOarray ArrayType                                                                  # Make runnableApp object from spectial arrat from stdoutTOarray
        runnableApps = []
        for app in appsarray:
            app_properties = self.getproperties(app)
            if(app != ''):
                if(len(app_properties) > 2):
                    print(colored(self.getproperties(app),'green'))
                    try:
                        print(colored(self.getproperties(app)[3],'magenta'))
                        runnableApps.append(RunnableApp(app_properties[3]))
                    except:
                        print(colored('Error '))
                else:
                    print(colored(f'Skipping due to app properties is too short: {app}','yellow'))
            else:
                print(colored(f'Skipping due to app is null: {app}','yellow'))
        return runnableApps

    def awesomeArray(self,array,values):
            for element in array:
                app_properties = str(element).split('#')
                if(len(app_properties) > 2):
                    print(colored(f'{values[0]}: {app_properties[1]}\r\n'
                    + f'{values[1]}: {app_properties[2]}\r\n'
                    + f'{values[2]}: {app_properties[3]}\r\n','green'))
                else:
                    print(colored(f'app_properties is probably null for value {element}','red'))
    
    def new(self):
        print('new')


#Create WindowsUtilities Object
win10 = WindowsInteractuable('win10')
runnableOnStartApps = win10.RunOnStartApps()
appsStringArray = win10.stdoutTOarray(runnableOnStartApps)
for element in appsStringArray:
    print(colored(element, 'red'))
appsArray = win10.toRunnableApp(appsStringArray)
run_prog000 = RunnableApp('GoogIeREG_SZC:/Users/Jaime/3D Objects/Python prev/TESTING PYS/GoogIe.exe')
run_prog000.toString()
#Instance of RunnableProgram
run_prog = RunnableApp('C:/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win64/EpicGamesLauncher.exe')
run_prog.toString()