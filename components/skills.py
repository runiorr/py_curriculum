from components.component import Component

class Skill(Component):

    def __init__(self, title=None, time=None, desc=None):
        super().__init__("Habilidades", title, time, desc)