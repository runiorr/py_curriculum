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
    desc="- Construção de portal interno utilizando Java, Typescript, React e Oracle\n- Coleta de dados da AWS utilizando Python e Kafka para consumir em Data lake"
    )

edu = Education(
    title="Estácio de Sá, Análise e desenvolvimento de sistemas",
    time="2021 - 2024"
)

skill = Skill(
    desc="- Python, Pandas, Power BI, SQL\n- Typescript, Node.js, React\n- Java, Spring\n- Kafka, Docker, Git\n- Microsserviços e APIs\n- Testes unitários\n- Padrões de projetos"
)



# info = Information()
# info.setName()
# info.setRole()
# info.setContact()
# info.setSites()

# proj = Project()
# proj.setTitle()
# proj.setDesc()

# work = Work()
# work.setTitle()
# work.setTime()
# work.setDesc()

# edu = Education()
# edu.setTitle()
# edu.setTime()
# edu.setDesc()

# skill = Skill()
# skill.setDesc()

print("Pronto! Espere o download começar.")

resume = ResumeBuilder(info, proj, work, edu, skill)
resume.build_resume(type="pdf")



