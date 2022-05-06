from components.component import Component

class Projects(Component):

    def __init__(self, title=None, time=None, desc=None):
        super().__init__("PROJETOS", title, time, desc)