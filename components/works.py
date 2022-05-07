from components.component import Component

class Works(Component):

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
    
    def setDesc(self):
        if self.desc == None:
            self.desc = []

        text = input(f"{self.header} - Resumo\n- ")

        self.desc.append(self.breakLines(text))