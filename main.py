from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills
from generate.curriculum import ResumeBuilder

info = Informations()
info.setName()
info.setRole()
info.setContact()
info.setSites()

proj = Projects()
proj.setTitle()
proj.setDesc()

work = Works()
work.setTitle()
work.setTime()
work.setDesc()

edu = Educations()
edu.setTitle()
edu.setTime()

skill = Skills()
skill.setDesc()

print("Pronto! Espere o download começar.")

resume = ResumeBuilder(info, proj, work, edu, skill)
resume.build_resume(type="pdf")



