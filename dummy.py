from components.informations import Informations
from components.projects import Projects
from components.works import Works
from components.educations import Educations 
from components.skills import Skills
from generate.curriculum import ResumeBuilder
from generate.curriculum import ResumeBuilder

info = Informations(
    name="JOSE RODRIGUES", 
    title="Analista de sistemas", 
    contact="51994241220",
    sites="www.github.com/runiorr"
    )

proj = Projects(
    title="Gerador de currículo", 
    desc="ele gera um curriculo"
    )

work = Works(
    title="DB | Desenvolvedor full stack", 
    time="02/2022 - Presente", 
    desc="- Coleta de dados da AWS utilizando Python e Kafka para consumir em Data lake"
    )

edu = Educations(
    title="Estácio de Sá, Análise e desenvolvimento de sistemas",
    time="2021 - 2024"
)

skill = Skills(
    desc="- Python, Pandas, Power BI, SQL")

print("Pronto! Espere o download começar.")

ResumeBuilder(info, proj, work, edu, skill, "pdf")



