import os
import sys
class HTML(object):
    htmlContent = ''
    file = '?????'
    def __init__(self,file):
        print('HTML Object created')
        self.htmlContent = ''
        self.file = file
        
    def getFile(self):
        return(f'file {self.file}')

    def loadHTML(self,htmlfilename):
        HTMLNAME = htmlfilename

        #Solved
                #It looks like you can not do this with files ONLY with directories
                #I should better use a htt.server library in order to control the host on runtime
        #Solved 
        PATH = f'C:/Users/Jaime/3D Objects\ProyectoFinDeCiclo\web\{HTMLNAME}'
        PORT = '8055'
        LOCALIP = '127.0.0.1'
        URL = LOCALIP + ':' + PORT +'/' + HTMLNAME
        print ('-------COMMAND-------')
        print(f'cd {PATH} && python -m http.server {PORT} && chrome.exe -incognito --new-window {URL}')
        try:
            os.system(f'start chrome.exe --new-window --window-size=300,1080 {LOCALIP}:{PORT}/{HTMLNAME}')
            os.system('cd {} && python -m http.server {}'.format(PATH.replace('\index.html', ''),PORT))

            print('Command executed successfully')
        except:
            print('Command excecute failed')

    def read(self):
        global htmlContent
        with open('web/index.html', 'r') as html:
            htmlContent = html.read()
        #print(colored(htmlContent, 'green'))
        return htmlContent

    def divup(self,inside,classname):
        htmlContent = self.read()
        #with open('web/index.html', 'w') as html:
        #    html.write(htmlContent)
        #    html.write(f'<div class="{classname}">\n'
        #    + f'{inside}')
        return f'<div class="{classname}">\n{inside}'
        
    def divdown(self):
        htmlContent = self.read()
        #with open('web/index.html', 'w') as html:
        #    html.write(htmlContent)
        #    html.write('</div>\n')
        return '</div>\n'

    def buttonup(self,inside,action,idname,classname):
        #with open('web/index.html', 'w') as html:
        #    html.write(htmlContent)
        #    html.write(f'<button class="{classname}">\n'
        #    + '{inside}')
        return f'        <button onclick="{action}" id="{idname}" class="{classname}">\n        {inside}\n'
            
    def buttondown(self):
        htmlContent = self.read()
        #with open('web/index.html', 'w') as html:
        #    html.write(htmlContent)
        #    html.write('</button>\n')
        return ('        </button>\n')

    def headerUp(self):
        header_up = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="index.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="index.js"></script>
    <script>
        function mod(){
            if(document.getElementById("enabled").innerHTML = "New text!"){
                alert("Run On Start: disabled");
            }else{
               alert("enabled"); 
            }  
                
            }       
    </script>
</head>
    <body>
    
'''
        with open(self.file, 'w') as html:
            html.write(header_up)

    def headerDown(self):
        #htmlContent = HTML.read()
        header_down = '''
    </body>
</html>
'''     
        htmlContent = self.read()
        with open(self.file, 'w') as html:
            html.write(htmlContent + header_down)
        

    def append(self,inside):
        htmlContent = self.read()
        with open(self.file, 'w') as html:
            html.write(htmlContent)
            html.write(f'{inside}\n')

