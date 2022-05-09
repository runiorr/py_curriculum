from components.component import Component

class Skills(Component):

    def __init__(self):
        super().__init__("Habilidades")
    
    def setDesc(self):
        self.desc = input(f"{self.header} - Liste elas separadas por ',' (ex: Python, Java)\n- ")
        self.desc = self.desc.split(',')