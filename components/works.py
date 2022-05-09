from components.component import Component

class Works(Component):

    items = []

    def __init__(self):
        super().__init__("EXPERIÊNCIA")
    
    def setTitle(self):
        if self.title == None:
            self.title = []

        self.title.append(input(f"{self.header} - Título\n- "))
    
    def setTime(self):
        if self.time == None:
            self.time = []

        self.time.append(input(f"{self.header} - Intervalo de tempo\n- "))
    
    def setDesc(self, parte=None):
        if self.desc == None:
            self.desc = []
        
        if parte is None:
            text = input(f"{self.header} - Resumo \n- ")
        else:
            text = input(f"{self.header} - Resumo {parte} (Enter para finalizar)\n- ")
            
        if text and text[0] == "-":
            self.items.append(text)
            self.setDesc(len(self.items)+1)

        if not(self.items == []):
            self.desc.append(self.items)
            self.items=[]
        
        line_wrapped = self.breakLines(text)
        if not(line_wrapped is None):
            self.desc.append(line_wrapped)