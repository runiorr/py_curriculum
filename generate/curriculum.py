from components.component import Component
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


class ResumeBuilder:

    def __init__(self, info, proj, work, edu, skill):
        self.info : Component = info
        self.project : Component = proj
        self.work : Component = work
        self.education : Component = edu
        self.skills : Component = skill
    
    #name, title, contact, sites
    def fill_info(self, info:Component):
        print(self.info)
        self.info.header = info.header
        self.info.title = info.title
        self.info.time = info.time
        self.info.desc = info.desc

    def fill_project(self, project:Component):
        self.project.header = project.header
        self.project.title = project.title
        self.project.time = project.time
        self.project.desc = project.desc

    def fill_work(self, work:Component):
        self.work.header = work.header
        self.work.title = work.title
        self.work.time = work.time
        self.work.desc = work.desc

    def fill_education(self, education:Component):
        self.education.header = education.header
        self.education.title = education.title
        self.education.time = education.time
        self.education.desc = education.desc

    def fill_skill(self, skills:Component):
        self.skills.header = skills.header
        self.skills.title = skills.title
        self.skills.time = skills.time
        self.skills.desc = skills.desc

    def build_resume(self, type):
        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))
        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
        plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
        # set background color
        ax.set_facecolor('white')
        # remove axes
        plt.axis('off')
        # Figure(850x1100)
        # add text

        Header = '>>>Esse currículo foi feito 100% em Python. Para código fonte, leia o QR Code.'

        plt.annotate(Header, (.02,.99), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(self.info.header, (.02,.94), weight='bold', fontsize=20)
        plt.annotate(self.info.title, (.02,.915), weight='regular', fontsize=14)
        plt.annotate("Contato", (.07,.96), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(self.info.time, (.07,.915), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(self.info.desc, (.07,.9), weight='regular', fontsize=8, color='#ffffff')

        plt.annotate(self.project.header, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(self.project.title, (.02,.832), weight='bold', fontsize=10)
        plt.annotate(self.project.desc, (.04,.8), weight='regular', fontsize=9)

        plt.annotate(self.work.header, (.02,.745), weight='bold', fontsize=10, color='#58C1B2')

        plt.annotate(self.work.title, (.02,.715), weight='bold', fontsize=10) # 30 de diferença p de cima
        plt.annotate(self.work.time, (.02,.698), weight='regular', fontsize=9, alpha=.6) # 15 de diferença pro de cima
        plt.annotate(self.work.desc, (.04,.668), weight='regular', fontsize=9) # 30 de diferença pro de cima

        # plt.annotate(self.work.title, (.02,.619), weight='bold', fontsize=10) # 62 de dif
        # plt.annotate(self.work.time, (.02,.601), weight='regular', fontsize=9, alpha=.6)
        # plt.annotate(self.work.desc, (.04,.555), weight='regular', fontsize=9)

        plt.annotate(self.education.header, (.02,.510), weight='bold', fontsize=10, color='#58C1B2')

        plt.annotate(self.education.title, (.02,.480), weight='bold', fontsize=10)
        plt.annotate(self.education.time, (.02,.465), weight='regular', fontsize=9, alpha=.6)

        plt.annotate(self.skills.header, (.7,.8), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(self.skills.desc, (.7,.65), weight='regular', fontsize=10, color='#ffffff')

        # #add qr code

        plt.annotate("Github do criador", (.754,.145), weight='bold', fontsize=10, color='#ffffff')
        qr_code = mpimg.imread('runiorrportolio.png')
        imagebox = OffsetImage(qr_code, zoom=0.055)
        ab = AnnotationBbox(imagebox, (0.84, 0.08))
        ax.add_artist(ab)

        plt.savefig(f'resume.{type}',format=type , dpi=300, bbox_inches='tight')