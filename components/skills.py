from components.component import Component

class Skills(Component):

    def __init__(self, title=None, time=None, desc=None):
        super().__init__("Habilidades", title, time, desc)
    
    def setDesc(self):
        self.desc = input(f"{self.header} - Liste elas separadas por ',' e espaço (ex: Python, Java)\n- ")
        self.desc = self.desc.split(',')