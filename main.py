from components.informations import Information 
from components.projects import Project
from components.works import Work 
from components.educations import Education 
from components.skills import Skill
from generate.curriculum import ResumeBuilder

# info = Information(
#     name="JOSE RODRIGUES", 
#     title="Analista de sistemas", 
#     contact="51994241220",
#     sites="www.github.com/runiorr"
#     )

# proj = Project(
#     title="Gerador de currículo", 
#     desc="ele gera um curriculo"
#     )

# work = Work(
#     title="DB | Desenvolvedor full stack", 
#     time="02/2022 - Presente", 
#     desc="- Construção de portal interno utilizando Java, Typescript, React e Oracle\n- Coleta de dados da AWS utilizando Python e Kafka para consumir em Data lake"
#     )

# edu = Education(
#     title="Estácio de Sá, Análise e desenvolvimento de sistemas",
#     time="2021 - 2024"
# )

# skill = Skill(
#     desc="- Python, Pandas, Power BI, SQL\n- Typescript, Node.js, React\n- Java, Spring\n- Kafka, Docker, Git\n- Microsserviços e APIs\n- Testes unitários\n- Padrões de projetos"
# )



info = Information(
    name=input("Nome: "), 
    title=input("Cargo: "), 
    contact=input("Contato: "),
    sites=input("Site: ")
    )

proj = Project(
    title=input("Título de projeto: "), 
    desc=input("Descrição do projeto: ")
    )

work = Work(
    title=input("Empresa | Cargo atual: "), 
    time=input("Período trabalhando: "), 
    desc=input("O que faz: ")
    )

edu = Education(
    title=input("Faculdade | Curso: "),
    time=input("Período de estudo: ")
)

skill = Skill(
    desc=input("Habilidades: ")
)

resume = ResumeBuilder(info, proj, work, edu, skill)


resume.build_resume(type="pdf")

print("Pronto! Espere o download começar.")


