from components.component import Component

class Education(Component):

    def __init__(self, title, time, desc):
        super().__init__("EDUCAÇÃO", title, time, desc)