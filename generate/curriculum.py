from components.component import Component
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from components.visitor.annotateVisitor import AnnotateVisitor

class ResumeBuilder:

    def __init__(self, info, proj, work, edu, skill, type):
        # Set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))
        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
        plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
        # Set background color
        ax.set_facecolor('white')
        # Remove axes
        plt.axis('off')

        resume_text = [info, proj, work, edu, skill]
        annotateVisitor = AnnotateVisitor()
        [resume.accept(annotateVisitor) for resume in resume_text]
        
        # Add QR Code
        plt.annotate("Github do criador", (.754,.145), weight='bold', fontsize=10, color='#ffffff')
        qr_code = mpimg.imread('runiorrportfolio.png')
        imagebox = OffsetImage(qr_code, zoom=0.055)
        ab = AnnotationBbox(imagebox, (0.84, 0.08))
        ax.add_artist(ab)

        plt.savefig(f'resume.{type}',format=type , dpi=300, bbox_inches='tight')