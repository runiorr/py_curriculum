import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from visitor.pdfVisitor import PdfVisitor

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

        resume_section = [info, proj, work, edu, skill]
        pdfVisitor = PdfVisitor()
        [section.accept(pdfVisitor) for section in resume_section]
        
        # Add QR Code
        plt.annotate("Clique aqui para apoiar", (.717,.22), url="https://mpago.la/1bjYDLn", weight='bold', fontsize=11, color='#ffffff')
        qr_code = mpimg.imread('runiorr_qrcode.png')
        imagebox = OffsetImage(qr_code, zoom=0.22)
        ab = AnnotationBbox(imagebox, (0.84, 0.108))
        ax.add_artist(ab)

        plt.savefig(f'resume.{type}',format=type , dpi=350, bbox_inches='tight')