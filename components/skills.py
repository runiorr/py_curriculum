from components.component import Component

class Skill(Component):

    def __init__(self, title, time, desc):
        super().__init__("HABILIDADES", title, time, desc)