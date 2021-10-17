import os
import sys
import subprocess
from termcolor import colored
from threading import Thread
import random
#Customized class imports
sys.path.append(".")
from HTML import HTML
from WindowsInteractuable import WindowsInteractuable
from JavaScript import JavaScript


js = JavaScript('web/index.js')

js.append(js.js_function('salute','console.log("button clicked")'))

print(colored(js.read(), 'magenta'))


#notes
    #command = f'REG QUERY "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /t "REG_SZ" /v {app_name}'
    #res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL) 

    # class RunnableApp:
    #     def __init__(self,path):
    #         #name = ONLY APP NAME
    #         #path = ONLY DIRECTORY WITH / side
    #         #ext = EXT WITH .
    #         #self.values = values
    #         self.isapp = True
    #         if("\\" in path):
    #             print(colored('Incorrect / form:   Try replacing \\ to /','red'))
    #             self.isapp = False
    #             if(path.endswith("/")):
    #                 print(colored('Path should not end with /:     Try to remove ending /','red'))
    #                 #self.isapp = False~  Removed beacuse it s suppose to be false yet
    #         name = os.path.basename(path)
    #         if('.' not in name):
    #             print(colored('Path should include extension:    Try to write the ".ext" at the end','red'))
    #             self.isapp = False

    #         if(self.isapp):   
    #             self.PATH = path 
    #             self.NAME = name#os.path.basename(self.PATH)
    #         else:
    #             print(colored('INSTANCE SKIPPED DUE TO PREV FAIL', 'red'))

    #     def run(self):
    #         if(self.NAME.endswith( '.py' or '.pyw')):
    #             cmd_in = f'python {self.PATH}'
    #             print(colored(f'COMMAND RUNNED:     {cmd_in}','yellow'))
    #             cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    #             return cmd_out
    #         elif(self.NAME.endswith('.exe')):
    #             cmd_in = f"cd \\ && cd {self.PATH.replace(self.NAME,'')} && {self.NAME}"
    #             print(colored(f'COMMAND RUNNED:     {cmd_in}','yellow'))
    #             #only_path = self.PATH.replace(self.NAME,'')
    #             os.system(cmd_in)
                
        
    #         else:
    #             print(colored(f'We couldn´t recognize extension; We don´t know how to run program','red'))

    #     def toString(self):
    #         print('Comming Soon')

    # class WindowsInteractuable:
    #     def __init__(self):
    #         print('Object instanced')


    #     #NON SELF METHODS

    #     def RunOnStartApps(): 
    #         cmd_in = 'REG QUERY HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
    #         cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    #         return cmd_out 

    #     def stdoutTOarray(cmd_out):
    #         cmd_out_converted = []
    #         for line in cmd_out.stdout.readlines():
    #             if(line != ''):
    #                 line = str(line).replace("b'",'').replace("\\r\\n'",'')
    #                 line = line.replace('    ', '#').replace('\\','/').replace('//','/')
    #                 line = line.replace('" ','#').replace('"','')
    #                 line = line.replace(' -','#-')
    #                 if(line != ''):
    #                     cmd_out_converted.append(line)
    #                 else:
    #                     print('Skipping due to being a null line')
    #         return cmd_out_converted  

    #     def getproperties(object):
    #         object_props = str(object).split('#')
    #         return object_props

    #     def toRunnableApp(appsarray):      
    #         # NEEDS A stdoutTOarray ArrayType                                                                             # Make runnableApp object from spectial arrat from stdoutTOarray
    #         runnableApps = []
    #         for app in appsarray:
    #             app_properties = WindowsInteractuable.getproperties(app)
    #             if(app != ''):
    #                 if(len(app_properties) > 2):
    #                     print(colored(WindowsInteractuable.getproperties(app),'green'))
    #                     print(colored(WindowsInteractuable.getproperties(app)[3],'magenta'))
    #                     runnableApps.append(RunnableApp(app_properties[3]))
    #                 else:
    #                     print(colored('Skipping due to app properties is too short','yellow'))
    #             else:
    #                 print(colored('Skipping due to app is null','yellow'))
    #         return runnableApps

    #     def awesomeArray(array,values):
    #             for element in array:
    #                 app_properties = str(element).split('#')
    #                 if(len(app_properties) > 2):
    #                     print(colored(f'{values[0]}: {app_properties[1]}\r\n'
    #                     + f'{values[1]}: {app_properties[2]}\r\n'
    #                     + f'{values[2]}: {app_properties[3]}\r\n','green'))
    #                 else:
    #                     print(colored(f'app_properties is probably null for value {element}','red'))
        
    #     def new():
    #         print('new')
        
    # class HTML:
    #     htmlContent = ''
    #     def __init__(self):
    #         print('HTML Object created')
    #         self.htmlContent = ''

    #     def loadHTML(htmlfilename):
    #         HTMLNAME = htmlfilename

    #         #Solved
    #                 #It looks like you can not do this with files ONLY with directories
    #                 #I should better use a htt.server library in order to control the host on runtime
    #         #Solved 
    #         PATH = f'C:/Users/Jaime/3D Objects\ProyectoFinDeCiclo\web\{HTMLNAME}'
    #         PORT = '8055'
    #         LOCALIP = '127.0.0.1'
    #         URL = LOCALIP + ':' + PORT +'/' + HTMLNAME
    #         print ('-------COMMAND-------')
    #         print(f'cd {PATH} && python -m http.server {PORT} && chrome.exe -incognito --new-window {URL}')
    #         try:
    #             os.system(f'start chrome.exe --new-window --window-size=300,1080 {LOCALIP}:{PORT}/{HTMLNAME}')
    #             os.system('cd {} && python -m http.server {}'.format(PATH.replace('\index.html', ''),PORT))

    #             print('Command executed successfully')
    #         except:
    #             print('Command excecute failed')

    #     def read():
    #         global htmlContent
    #         with open('web/index.html', 'r') as html:
    #             htmlContent = html.read()
    #         #print(colored(htmlContent, 'green'))
    #         return htmlContent

    #     def divup(inside,classname):
    #         htmlContent = HTML.read()
    #         with open('web/index.html', 'w') as html:
    #             html.write(htmlContent)
    #             html.write(f'<div class="{classname}">\n'
    #             + f'{inside}')
    #     def divdown():
    #         htmlContent = HTML.read()
    #         with open('web/index.html', 'w') as html:
    #             html.write(htmlContent)
    #             html.write('</div>\n')


    #     def buttonup(inside,action,idname,classname):
    #         #with open('web/index.html', 'w') as html:
    #         #    html.write(htmlContent)
    #         #    html.write(f'<button class="{classname}">\n'
    #         #    + '{inside}')
    #         return f'<button onclick="{action}" id="{idname}" class="{classname}">\n{inside}\n'
                
    #     def buttondown():
    #         htmlContent = HTML.read()
    #         #with open('web/index.html', 'w') as html:
    #         #    html.write(htmlContent)
    #         #    html.write('</button>\n')
    #         return ('</button>\n')

    #     def headerUp():
    #         header_up = '''
    #         <!DOCTYPE html>
    #         <html lang="en">
    #         <head>
    #             <link rel="stylesheet" href="index.css">
    #             <meta charset="UTF-8">
    #             <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #             <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #             <title>Document</title>
    #             <script src="index.js"></script>
    #         </head>
    #         <body>
    #         '''
    #         with open('web/index.html', 'w') as html:
    #             html.write(header_up)

    #     def headerDown():
    #         #htmlContent = HTML.read()
    #         header_down = '''
    #         </body>
    #         </html>
    #         '''
    #         with open('web/index.html', 'w') as html:
    #             html.write(htmlContent + header_down)
            

    #     def append(inside):
    #         htmlContent = HTML.read()
    #         with open('web/index.html', 'w') as html:
    #             html.write(htmlContent)
    #             html.write(f'{inside}\n')
    # def notes():
    # windows = WindowsInteractuable
    # object = WindowsInteractuable.RunOnStartApps()#Non self method
    # array = WindowsInteractuable.stdoutTOarray(object)#Non self method
    # runnableApps = WindowsInteractuable.toRunnableApp(array)#Non self method


print('\n')
windows = WindowsInteractuable('windows')
object = windows.RunOnStartApps()#
array = windows.stdoutTOarray(object)#
runnableApps = windows.toRunnableApp(array)#

print('\n')
for runnableApp in runnableApps:
    print(colored(runnableApp, 'cyan'))



# RANDOM CHOICE FOR CSS TESTING
list = ['enabled','disabled']


html = HTML('web/index.html')

html.headerUp()#Autowrite

#Requires manual writing
html.append(html.divup('','container'))
for element in runnableApps:
    htmlContent = html.buttonup(element.NAME,'salute()',element.STATE,'raise')
    htmlContent = htmlContent + html.buttondown()
    print(colored(htmlContent, 'cyan'))
    html.append(htmlContent)

html.append(html.divdown())


html.headerDown()#Autowrite



exit()

aaaaa = WindowsInteractuable.getproperties(array[2])
print(aaaaa)

windows.awesomeArray(windows,array,['NAME','TYPE','PATH'])













# for app in array:
#     if(app != ''):
#         app = app.replace('    ', '#').replace('\\','/').replace('//','/')
#         app_properties = str(app).split('#')
#         if(len(app_properties) > 2):
#             print(f'APP: {app_properties[1]}\r\n'
#             + f'TYPE: {app_properties[2]}\r\n'
#             + f'PATH: {app_properties[3]}\r\n')
#         else:
#             print(f'app_properties is probably null for value {app}' )