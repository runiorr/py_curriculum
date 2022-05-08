html_string = """
<!DOCTYPE html>
<html>
    <head>
        <title>Resume</title>
    </head>
    <style>
        body {body}
        html, body {html}
        h2 {h2}

        #right {right}
        #right_box {right_box}
        #right_header {right_header}
        #right_content {right_content}

        #left {left}
        .information {information}
    </style>
    <body>
        <div id="right">
            <div id="right_box" class="contact">
                <h3 id="right_header">Contato</h3>
                <div id="right_content">
                    <p>{cellphone}</p>
                    <p>{email}</p>
                    <p>{linkedin}</p>
                    <p>{github}</p>
                </div>
            </div>
            <div class="skills/support">
                <div id="right_box">
                    <h3 id="right_header">Habilidades</h3>
                    <div id="right_content">
                        <p>{skills}</p>
                    </div>
                </div>
                <div id="right_box">
                    <h3 id="right_header">Apoie o criador</h3>
                    <img src={qrcode} width="100" width="110" height="110">
                </div>
            </div>
        </div>
        <div id="left">
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
    body="{ background-color: white; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; margin:10px; }",
    html="{ height: 1100px; width: 850px; }",
    h2="{ color:rgba(0, 255, 255, 0.603) }",
    right="{ float:right; justify-content:space-between; margin-left: 0; margin-right: auto; }",
    right_box="{ background-color:gray; padding-block-end: 5px; padding-inline-start: 10px; padding-right: 100px; }",
    right_header="{ color:white; padding-top: 5px; }",
    right_content="{ color:lightgray }",
    left="{ float:left; justify-content:space-between; margin-left: auto; margin-right: 0; }",
    information="{ color: red; }",

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

# print(html_string)

with open("template/resume.html", "w") as file:
    file.write(html_string)

print("DONE")