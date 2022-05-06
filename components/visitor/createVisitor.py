from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills

class CreateVisitor:

    def visitInformations(self, information: Informations):
        pass

    def visitProjects(self, project: Projects):
        pass

    def visitWorks(self, work: Works):
        pass

    def visitEducations(self, education: Educations):
        pass

    def visitSkills(self, skill: Skills):
        pass
    