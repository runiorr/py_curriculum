from components.informations import Information 
from components.projects import Project
from components.works import Work 
from components.educations import Education 
from components.skills import Skill
from generate.curriculum import ResumeBuilder

info = Information(
    name="JOSE RODRIGUES", 
    title="Analista de sistemas", 
    contact="51994241220",
    sites="www.github.com/runiorr"
    )

proj = Project(
    title="Gerador de currículo", 
    desc="ele gera um curriculo"
    )

work = Work(
    title="DB | Desenvolvedor full stack", 
    time="02/2022 - Presente", 
    desc="- Coleta de dados da AWS utilizando Python e Kafka para consumir em Data lake"
    )

edu = Education(
    title="Estácio de Sá, Análise e desenvolvimento de sistemas",
    time="2021 - 2024"
)

skill = Skill(
    desc="- Python, Pandas, Power BI, SQL")

print("Pronto! Espere o download começar.")

resume = ResumeBuilder(info, proj, work, edu, skill)
resume.build_resume(type="pdf")



