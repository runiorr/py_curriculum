from components.component import Component

class Work(Component):

    def __init__(self, title=None, time=None, desc=None):
        super().__init__("EXPERIÊNCIA", title, time, desc)