html_string = """
<!DOCTYPE html>
<html>
    <head>
        <title>Resume</title>
    </head>
    <body>
        <div class=".right">
            <div class="contact">
                <h3>Contato</h3>
                <p>{cellphone}</p>
                <p>{email}</p>
                <p>{linkedin}</p>
                <p>{github}</p>
            </div>
            <div class="skills">
                <h3>Habilidades</h3>
                <p>{skills}</p>
            </div>
            <div class="support">
                <h3>Apoie o criador</h3>
                <img src={qrcode}>
            </div>
        </div>
        <div class=".left">
            <div class="information">
                <h1>{name}</h1>
                <h2>{role}</h2>
            </div>
            <div class="projects">
                <h2>Projetos</h2>
                <p>{project_name}</p>
                <p>{project_desc}</p>
            </div>
            <div class="works">
                <h2>Experiência</h2>
                <p>{work_name}</p>
                <p>{work_time}</p>
                <p>{work_desc}</p>
            </div>
            <div class="education">
                <h2>Educação</h2>
                <p>{edu_name}</p>
                <p>{edu_time}</p>
            </div>
        </div>
    </body>
</html>
"""

html_string = html_string.format(
    name="Jose Rodrigues",
    role="Analista de desenvolvimento",
    cellphone="994241220",
    email="joseluisrjunior@gmail.com",
    linkedin="www.linkedin.com/in/joserodrigs",
    github="www.github.com/runiorr",
    skills="Python",
    qrcode="../runiorr_qrcode.png",
    project_name="Resume builder",
    project_desc="Cria curriculos de forma automatica",
    work_name="DB - Desenvolvedor full stack",
    work_time="02/2022 - Atualmente",
    work_desc="Desenvolvo automações",
    edu_name="Estácio de Sá - Análise e desenvolvimento de sistemas",
    edu_time="10/2021 - 04/2023",
    )

print(html_string)

with open("template/resume.html", "w") as file:
    file.write(html_string)

print("DONE")