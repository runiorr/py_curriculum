from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills
from generate.margins import left,right,paragraph,header_distance,title_distance,time_distance,desc_distance

import matplotlib.pyplot as plt

class AnnotateVisitor:
    last_project = 0
    last_work = 0

    def visitInformations(self, information: Informations):
        Header = '>>>Esse currículo foi feito 100% em Python. Para código fonte, leia o QR Code.'
        plt.annotate(Header, (left, .98), weight='regular', fontsize=8, alpha=.75)
        name_heigh = .93
        role_heigh = name_heigh - .026
        plt.annotate(information.header, (left, name_heigh), weight='bold', fontsize=20) # Name
        plt.annotate(information.title, (left, role_heigh), weight='regular', fontsize=14) # Role
        CONTATO_header = .97
        cellphone = CONTATO_header - desc_distance # contatos
        email = cellphone - desc_distance # contatos
        linkedin = email - desc_distance # sites
        github = linkedin - desc_distance # sites
        plt.annotate("Informações", (right, CONTATO_header), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(information.time.split()[0], (right, cellphone), weight='regular', fontsize=8, color='#ffffff') # Contact
        plt.annotate(information.time.split()[1], (right, email), weight='regular', fontsize=8, color='#ffffff') # Sites
        plt.annotate(information.desc.split()[0], (right, linkedin), weight='regular', fontsize=8, color='#ffffff')
        plt.annotate(information.desc.split()[1], (right, github), weight='regular', fontsize=8, color='#ffffff')

    def visitProjects(self, project: Projects):
        p_header = .86
        p_title = p_header - title_distance
        p_desc = p_title - desc_distance
        self.last_project = p_desc
        plt.annotate(project.header, (left, p_header), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(project.title, (left, p_title), weight='bold', fontsize=10)
        plt.annotate(project.desc, (paragraph, p_desc), weight='regular', fontsize=9)

    def visitWorks(self, work: Works):
        w_header = self.last_project - header_distance
        w_title = w_header - title_distance
        w_time = w_title - time_distance
        w_desc = w_time - desc_distance
        self.last_work = w_desc
        plt.annotate(work.header, (left, w_header), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(work.title, (left, w_title), weight='bold', fontsize=10)
        plt.annotate(work.time, (left, w_time), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(work.desc, (paragraph, w_desc), weight='regular', fontsize=9)

    def visitEducations(self, education: Educations):
        e_header = self.last_work - header_distance
        e_title = e_header - title_distance
        e_time = e_title - time_distance
        plt.annotate(education.header, (left, e_header), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(education.title, (left, e_title), weight='bold', fontsize=10)
        plt.annotate(education.time, (left, e_time), weight='regular', fontsize=9, alpha=.6)

    def visitSkills(self, skill: Skills):
        s_header = .85
        s_desc = s_header - desc_distance
        plt.annotate(skill.header, (right, s_header), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(skill.desc, (right, s_desc), weight='regular', fontsize=10, color='#ffffff')