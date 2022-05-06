from Ivisitor import IVisitor
from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills

import matplotlib.pyplot as plt

class PrinterVisitor(IVisitor):

    def visitInformations(information: Informations):
        pass

    def visitProjects(project: Projects):
        pass

    def visitEducations(education: Educations):
        pass

    def visitSkills(skill: Skills):
        pass

    def visitWorks(work: Works):
        pass