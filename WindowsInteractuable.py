import sys
import subprocess
from termcolor import colored
sys.path.append(".")
from RunnableApp import RunnableApp

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
                    print(colored(self.getproperties(app)[3],'magenta'))
                    runnableApps.append(RunnableApp(app_properties[3]))
                else:
                    print(colored('Skipping due to app properties is too short','yellow'))
            else:
                print(colored('Skipping due to app is null','yellow'))
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