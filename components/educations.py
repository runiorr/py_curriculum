from components.component import Component

class Education(Component):

    def __init__(self, title=None, time=None, desc=None):
        super().__init__("EDUCAÇÃO", title, time, desc)