from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills
from resumeBuilder import ResumeBuilder
from visitor.fillVisitor import FillVisitor

info = Informations()
proj = Projects()
work = Works()
edu = Educations()
skill = Skills()

text_content = [info, proj, work, edu, skill]
fillVisitor = FillVisitor()
[text.accept(fillVisitor) for text in text_content]

print("Pronto! Espere o download começar.")

ResumeBuilder(info, proj, work, edu, skill, "pdf")



