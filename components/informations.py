from components.component import Component

class Information(Component):

    def __init__(self, name=None, title=None, contact=None, sites=None):
        super().__init__(name, title, contact, sites)
    
    def setName(self):
        self.header = input("Qual o seu nome?\n- ")
    
    def setRole(self):
        self.title = input("Qual cargo deseja colocar?\n- ")

    def setContact(self):
        self.time = input("Informações de contato (numero e email):\n- ")
    
    def setSites(self):
        self.desc = input("URL de seu Linkedin e/ou Github\:\n- ")