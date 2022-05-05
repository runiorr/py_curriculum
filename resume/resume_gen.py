# Text Variables
Header = '>>>Esse currículo foi feito 100% em Python. Para código fonte, acesse meu github.'
Name = 'JOSE RODRIGUES'
Title = 'Analista de sistemas e dados'
Contact = '(51) 994241220\njoseluisrjunior@gmail.com\nwww.linkedin.com/in/joserodrigs\nwww.github.com/runiorr'

ProjectsHeader = 'PROJETOS'
ProjectOneTitle = 'Gerador de currículos'
ProjectOneDesc = '- Published by Towards Data Science\n- Analyzed user survey to recommend most profitable future revenue source\n- Cleaned/visualized data using pandas/matplotlib libraries in Python'

WorkHeader = 'EXPERIÊNCIA'
WorkOneTitle = 'DB | Desenvolvedor full stack'
WorkOneTime = '2/2022 - Presente'
WorkOneDesc = '- Construção de portal interno utilizando Java, Typescript, React e Oracle\n- Coleta de dados da AWS utilizando Python e Kafka para consumir em Data lake'

WorkTwoTitle = 'Chat2Desk Brasil | Cientista de dados - Estágio'
WorkTwoTime = '12/2021 - 2/2022'
WorkTwoDesc = '- Realizei ETL para alimentar planilhas de dados\n- Criei scripts para tratar dados de planilhas\n- Elaborei dashboards para projeções de negócio'

EduHeader = 'EDUCAÇÃO'
EduOneTitle = 'Estácio de Sá, Análise e desenvolvimento de sistemas'
EduOneTime = '2021-2024'

SkillsHeader = 'Habilidades'
SkillsDesc =   '- Python, Pandas, Power BI, SQL\n- Typescript, Node.js, React\n- Java, Spring\n- Kafka, Docker, Git\n- Microsserviços e APIs\n- Testes unitários\n- Padrões de projetos'

# ExtrasTitle = 'DataQuest\nData Scientist Path'
# ExtrasDesc = 'Learned popular data science\nlanguages, data cleaning and\nmanipulation, machine learning \nand statistical analysis'
# CodeTitle = 'View Portfolio'

# Setting style for bar graphs
import matplotlib.pyplot as plt
# %matplotlib inline

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))


# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# Figure(850x1100)

# add text
plt.annotate(Header, (.02,0.98), weight='regular', fontsize=8, alpha=.75)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate("Contato", (.7,.96), weight='bold', fontsize=14, color='#ffffff')
plt.annotate(Contact, (.7,.9), weight='regular', fontsize=8, color='#ffffff')

plt.annotate(ProjectsHeader, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(ProjectOneTitle, (.02,.832), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04,.78), weight='regular', fontsize=9)

plt.annotate(WorkHeader, (.02,.745), weight='bold', fontsize=10, color='#58C1B2')

plt.annotate(WorkOneTitle, (.02,.715), weight='bold', fontsize=10) # 30 de diferença p de cima
plt.annotate(WorkOneTime, (.02,.698), weight='regular', fontsize=9, alpha=.6) # 15 de diferença pro de cima
plt.annotate(WorkOneDesc, (.04,.668), weight='regular', fontsize=9) # 30 de diferença pro de cima

plt.annotate(WorkTwoTitle, (.02,.619), weight='bold', fontsize=10) # 62 de dif
plt.annotate(WorkTwoTime, (.02,.601), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.555), weight='regular', fontsize=9)

plt.annotate(EduHeader, (.02,.510), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02,.490), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02,.475), weight='regular', fontsize=9, alpha=.6)

plt.annotate(SkillsHeader, (.7,.8), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.65), weight='regular', fontsize=10, color='#ffffff')

# plt.annotate(ExtrasTitle, (.7,.43), weight='bold', fontsize=10, color='#ffffff')
# plt.annotate(ExtrasDesc, (.7,.345), weight='regular', fontsize=10, color='#ffffff')
# plt.annotate(CodeTitle, (.7,.2), weight='bold', fontsize=10, color='#ffffff')


# #add qr code

# from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
# import matplotlib.image as mpimg
# arr_code = mpimg.imread('ekresumecode.png')
# imagebox = OffsetImage(arr_code, zoom=0.5)
# ab = AnnotationBbox(imagebox, (0.84, 0.12))
# ax.add_artist(ab)

plt.savefig('resume.pdf',format='pdf' , dpi=300, bbox_inches='tight')
plt.savefig('resume.png', dpi=300, bbox_inches='tight')