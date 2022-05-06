from components.visitor.Ivisitor import IVisitor


class Component:

    def __init__(self, header=None, title=None, time=None, desc=None):
        self.header = header
        self.title = title
        self.time = time
        self.desc = desc
    
    def setHeader(self, header):
        self.header = header

    def setTitle(self):
        self.title = input(f"{self.header} - Título\n- ")
    
    def setTime(self):
        self.time = input(f"{self.header} - Intervalo de tempo\n- ")
    
    def setDesc(self):
        self.desc = input(f"{self.header} - Resumo\n- ")
    
    def _getClassAttributes(self):
        print(self.header)
        print(self.title)
        print(self.time)
        print(self.desc)
    
    def accept(self, v:IVisitor):
        visit_func = eval(f"v.visit{self.__class__.__name__}(self)")
        visit_func()
    