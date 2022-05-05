from components.component import Component

class Work(Component):

    def __init__(self, title, time, desc):
        super().__init__("EXPERIÊNCIA", title, time, desc)