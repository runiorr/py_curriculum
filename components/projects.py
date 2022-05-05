from components.component import Component

class Project(Component):

    def __init__(self, title, time, desc):
        super().__init__("PROJETOS", title, time, desc)