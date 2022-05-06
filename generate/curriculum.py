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

        left = 0.02
        right = 0.7
        paragraph = .035
        header_distance = .045
        title_distance = .02
        time_distance = .015
        desc_distance = .02

        name_heigh = .93
        role_heigh = name_heigh - .026
        plt.annotate(Header, (left, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(self.info.header, (left, name_heigh), weight='bold', fontsize=20) # Name
        plt.annotate(self.info.title, (left, role_heigh), weight='regular', fontsize=14) # Role

        CONTATO_header = .97
        cellphone = CONTATO_header - desc_distance # contatos
        email = cellphone - desc_distance # contatos
        linkedin = email - desc_distance # sites
        github = linkedin - desc_distance # sites
        plt.annotate("Informações", (right, CONTATO_header), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(self.info.time.split()[0], (right, cellphone), weight='regular', fontsize=8, color='#ffffff') # Contact
        plt.annotate(self.info.time.split()[1], (right, email), weight='regular', fontsize=8, color='#ffffff') # Sites
        plt.annotate(self.info.desc.split()[0], (right, linkedin), weight='regular', fontsize=8, color='#ffffff')
        plt.annotate(self.info.desc.split()[1], (right, github), weight='regular', fontsize=8, color='#ffffff')
        
        p_header = .86
        p_title = p_header - title_distance
        p_desc = p_title - desc_distance

        plt.annotate(self.project.header, (left, p_header), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(self.project.title, (left, p_title), weight='bold', fontsize=10)
        plt.annotate(self.project.desc, (paragraph, p_desc), weight='regular', fontsize=9)

        w_header = p_desc - header_distance
        w_title = w_header - title_distance
        w_time = w_title - time_distance
        w_desc = w_time - desc_distance

        plt.annotate(self.work.header, (left, w_header), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(self.work.title, (left, w_title), weight='bold', fontsize=10)
        plt.annotate(self.work.time, (left, w_time), weight='regular', fontsize=9, alpha=.6)
        plt.annotate(self.work.desc, (paragraph, w_desc), weight='regular', fontsize=9)

        e_header = w_desc - header_distance
        e_title = e_header - title_distance
        e_time = e_title - time_distance

        plt.annotate(self.education.header, (left, e_header), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(self.education.title, (left, e_title), weight='bold', fontsize=10)
        plt.annotate(self.education.time, (left, e_time), weight='regular', fontsize=9, alpha=.6)

        s_header = .85
        s_desc = s_header - desc_distance

        plt.annotate(self.skills.header, (right, s_header), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(self.skills.desc, (right, s_desc), weight='regular', fontsize=10, color='#ffffff')

        # Add QR Code
        plt.annotate("Github do criador", (.754,.145), weight='bold', fontsize=10, color='#ffffff')
        qr_code = mpimg.imread('runiorrportolio.png')
        imagebox = OffsetImage(qr_code, zoom=0.055)
        ab = AnnotationBbox(imagebox, (0.84, 0.08))
        ax.add_artist(ab)

        plt.savefig(f'resume.{type}',format=type , dpi=300, bbox_inches='tight')