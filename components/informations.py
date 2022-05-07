from components.component import Component

class Informations(Component):

    def __init__(self):
        super().__init__()
    
    def setName(self):
        self.header = input("Qual o seu nome?\n- ").title()
    
    def setRole(self):
        self.title = input("Qual cargo deseja colocar?\n- ").title()

    def setContact(self):
        cellphone = input("Qual seu número de telefone?\n- ")
        email = input("Qual seu email?\n- ")
        self.time = f"{cellphone} {email}"

    def setSites(self):
        linkedin = input("Qual seu linkedin?\n- ")
        github = input("Qual seu github?\n- ")
        self.desc = f"{linkedin} {github}"