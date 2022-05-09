from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills
from visitor.margins import left, right, paragraph, header_distance, mini_header_distance, title_distance, time_distance, desc_distance, paragraph_distance

import matplotlib.pyplot as plt

class PdfVisitor:
    last_project = 0
    last_work = 0

    def visitInformations(self, information: Informations):
        footer = '>>> Esse currículo foi feito 100% em Python. Considere ao lado >>>'
        plt.annotate(footer, (left, 0.008), weight='regular', fontsize=8, alpha=.75)

        name_heigh = .93
        role_heigh = name_heigh - .026
        plt.annotate(information.header, (left, name_heigh), weight='bold', fontsize=20) # Name
        plt.annotate(information.title, (left, role_heigh), weight='regular', fontsize=14) # Role
        
        CONTATO_header = .978
        cellphone = CONTATO_header - desc_distance # contatos
        email = cellphone - desc_distance # contatos
        linkedin = email - desc_distance # sites
        github = linkedin - desc_distance # sites
        usr_linkedin = information.desc.split(',')[0]
        usr_github = information.desc.split(',')[1]
        plt.annotate("Contato", (right, CONTATO_header), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(f"Telefone: {information.time.split(',')[0]}", (right, cellphone), weight='regular', fontsize=8, color='#ffffff')
        plt.annotate(information.time.split(',')[1], (right, email), weight='regular', fontsize=8, color='#ffffff')
        plt.annotate(f"Linkedin/in/{usr_linkedin}", (right, linkedin),url=f"www.linkedin.com/in/{usr_linkedin}", weight='regular', fontsize=8, color='#ffffff')
        plt.annotate(f"Github/{usr_github}", (right, github),url=f"www.github.com/{usr_github}", weight='regular', fontsize=8, color='#ffffff')

    def visitProjects(self, project: Projects):
        p_header = .86
        p_title = p_header - title_distance
        p_desc = p_title - desc_distance
        if (project.title == None):
            PdfVisitor.last_project = p_header
            return
        plt.annotate(project.header, (left, p_header), weight='bold', fontsize=10, color='#58C1B2')
        for ind in range(len(project.title)):
            plt.annotate(project.title[ind], (left, p_title), weight='bold', fontsize=10)
            for text in range(len(project.desc[ind])):
                plt.annotate(project.desc[ind][text], (paragraph, p_desc), weight='regular', fontsize=9)
                p_desc = p_desc - paragraph_distance
            p_title = p_desc - mini_header_distance
            p_desc = p_title - desc_distance
        PdfVisitor.last_project = p_desc

    def visitWorks(self, work: Works):
        w_header = PdfVisitor.last_project - header_distance
        w_title = w_header - title_distance
        w_time = w_title - time_distance
        w_desc = w_time - desc_distance
        if (work.title == None):
            PdfVisitor.last_work = PdfVisitor.last_project
            return
        plt.annotate(work.header, (left, w_header), weight='bold', fontsize=10, color='#58C1B2')
        for ind in range(len(work.title)):
            plt.annotate(work.title[ind], (left, w_title), weight='bold', fontsize=10)
            plt.annotate(work.time[ind], (left, w_time), weight='regular', fontsize=9, alpha=.6)
            for text in range(len(work.desc[ind])):
                plt.annotate(work.desc[ind][text], (paragraph, w_desc), weight='regular', fontsize=9)
                w_desc = w_desc - paragraph_distance
            w_title = w_desc - mini_header_distance
            w_time = w_title - time_distance
            w_desc = w_time - desc_distance
        PdfVisitor.last_work = w_desc

    def visitEducations(self, education: Educations):
        e_header = PdfVisitor.last_work - header_distance
        e_title = e_header - title_distance
        e_time = e_title - time_distance
        if (education.title == None):
            return
        plt.annotate(education.header, (left, e_header), weight='bold', fontsize=10, color='#58C1B2')
        for ind in range(len(education.title)):
            plt.annotate(education.title[ind], (left, e_title), weight='bold', fontsize=10)
            plt.annotate(education.time[ind], (left, e_time), weight='regular', fontsize=9, alpha=.6)
            e_title = e_time - mini_header_distance
            e_time = e_title - time_distance

    def visitSkills(self, skill: Skills):
        s_header = .85
        plt.annotate(skill.header, (right, s_header), weight='bold', fontsize=10, color='#ffffff')
        for s in skill.desc:
            s = s.strip().title()
            s_desc = s_header - desc_distance
            plt.annotate(s, (right, s_desc), weight='regular', fontsize=10, color='#ffffff')
            s_header -= desc_distance