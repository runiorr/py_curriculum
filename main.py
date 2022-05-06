from components.informations import Information 
from components.projects import Project
from components.works import Work 
from components.educations import Education 
from components.skills import Skill
from generate.curriculum import ResumeBuilder

info = Information()
info.setName()
info.setRole()
info.setContact()
info.setSites()

proj = Project()
proj.setTitle()
proj.setDesc()

work = Work()
work.setTitle()
work.setTime()
work.setDesc()

edu = Education()
edu.setTitle()
edu.setTime()

skill = Skill()
skill.setDesc()

print("Pronto! Espere o download começar.")

resume = ResumeBuilder(info, proj, work, edu, skill)
resume.build_resume(type="pdf")



