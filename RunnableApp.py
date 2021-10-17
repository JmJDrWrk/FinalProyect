import os
import sys
from termcolor import colored
import subprocess
sys.path.append('.')

class RunnableApp:
    def __init__(self,path):
        #name = ONLY APP NAME
        #path = ONLY DIRECTORY WITH / side
        #ext = EXT WITH .
        #self.values = values
        self.isapp = True
        if("\\" in path):
            print(colored('Incorrect / form:   Try replacing \\ to /','red'))
            self.isapp = False
            if(path.endswith("/")):
                print(colored('Path should not end with /:     Try to remove ending /','red'))
                #self.isapp = False~  Removed beacuse it s suppose to be false yet
        name = os.path.basename(path)
        if('.' not in name):
            print(colored('Path should include extension:    Try to write the ".ext" at the end','red'))
            self.isapp = False

        
        #res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL) 
        if(self.isapp):   
            self.PATH = path 
            self.NAME = name#os.path.basename(self.PATH)
            command = f'REG QUERY "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /t "REG_SZ" /v {name.replace(".exe","")}'
            res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            print(colored(res.stdout.readline(),'magenta'))
            self.STATE = 'enabled'
        else:
            print(colored('INSTANCE SKIPPED DUE TO PREV FAIL', 'red'))

    def run(self):
        if(self.NAME.endswith( '.py' or '.pyw')):
            cmd_in = f'python {self.PATH}'
            print(colored(f'COMMAND RUNNED:     {cmd_in}','yellow'))
            cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            return cmd_out
        elif(self.NAME.endswith('.exe')):
            cmd_in = f"cd \\ && cd {self.PATH.replace(self.NAME,'')} && {self.NAME}"
            print(colored(f'COMMAND RUNNED:     {cmd_in}','yellow'))
            #only_path = self.PATH.replace(self.NAME,'')
            os.system(cmd_in)
            
    
        else:
            print(colored(f'We couldn´t recognize extension; We don´t know how to run program','red'))


    def disableRunOnStart():
        print('Comming soon')
        #Equipo\HKEY_USERS\S-1-5-21-4108893222-2288396013-2005981722-1001\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run
        #REG QUERY "HKEY_USERS\S-1-5-21-4108893222-2288396013-2005981722-1001\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run" /t REG_BINARY
    def toString(self):
        print('Comming Soon')