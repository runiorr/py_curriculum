from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills
from template.resumeBuilder import ResumeBuilder
from visitor.fillVisitor import FillVisitor

info = Informations()
proj = Projects()
work = Works()
edu = Educations()
skill = Skills()

resume_section = [info, proj, work, edu, skill]
fillVisitor = FillVisitor()
[section.accept(fillVisitor) for section in resume_section]

print("Pronto! Espere o download começar.")

ResumeBuilder(info, proj, work, edu, skill, "pdf")



