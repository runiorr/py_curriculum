from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills

class CreateVisitor:

    def validate_items(self, items):
        if items[0] == "": items[0]=1
        try:
            items[0] = int(items[0])
        except:
            print("Escolha um número válido!\n- ")
        if type(items[0]) != int: return False
        if items[0] <= 0: return False
        if items[0] >= 4: return False
        return True

    def visitInformations(self, information: Informations):
        information.setName()
        information.setRole()
        information.setContact()
        information.setSites()

    def visitProjects(self, project: Projects):
        items = [input("Quantos projetos irá adicionar? (Limite é 3 | 'Enter para 1)\n- ")]
        if self.validate_items(items):
            for item in range(items[0]):
                project.setTitle()
                project.setDesc()
        else: self.visitProjects(project) 

    def visitWorks(self, work: Works):
        items = [input("Quantas experiências irá adicionar? (Limite é 3 | 'Enter para 1)\n- ")]
        if self.validate_items(items):
            for item in range(items[0]):
                work.setTitle()
                work.setTime()
                work.setDesc()
        else: self.visitWorks(work)

    def visitEducations(self, education: Educations):
        items = [input("Quantas formações irá adicionar? (Limite é 3 | 'Enter para 1)\n- ")]
        if self.validate_items(items):
            for item in range(items[0]):
                education.setTitle()
                education.setTime()
        else: self.visitEducations(education)

    def visitSkills(self, skill: Skills):
        skill.setDesc()
