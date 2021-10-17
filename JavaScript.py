class JavaScript(object):
    def __init__(self, file):
        print('JavaScript Class')
        self.file = file
        with open(self.file, 'w') as js:
            js.write('')

    def read(self):
        with open(self.file, 'r') as js:
            jsContent = js.read()
        return jsContent

    def append(self, inside):
        jsContent = self.read()
        with open(self.file, 'w') as js:
            js.write(jsContent + '\n')
            js.write(inside)

    def js_function(self,funcname,inside):
        return (f'function {funcname}()' + '{\n' + f'    {inside}' + '\n}')
        
    