from textwrap import wrap

class Component:

    def __init__(self, header=None, title=None, time=None, desc=None):
    # def __init__(self, header=[], title=[], time=[], desc=[]):

        self.header = header
        self.title = title
        self.time = time
        self.desc = desc
    
    def setHeader(self, header):
        self.header = header

    # def setTitle(self):
    #     self.title = input(f"{self.header} - Título\n- ")
    
    # def setTime(self):
    #     self.time = (input(f"{self.header} - Intervalo de tempo\n- "))
    
    # def setDesc(self):
    #     self.desc = (input(f"{self.header} - Resumo\n- "))
    
    def accept(self, visitor):
        visit_func = eval(f"visitor.visit{self.__class__.__name__}")
        visit_func(self)
    
    def getItems(self):
        print(self.__class__.__name__)
        print(self.header, type(self.header))
        print(self.title, type(self.title))
        print(self.time, type(self.time))
        print(self.desc, type(self.desc))
    
    def breakLines(self, text):
        if text:
            if(text[0]=="" or text[0] == "-"):
                return None
            else:
                return wrap(text,70)