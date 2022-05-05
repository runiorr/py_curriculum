class Component:

    def __init__(self, header, title=None, time=None, desc=None):
        self.header = header
        self.title = title
        self.time = time
        self.desc = desc
    
    def setHeader(self, header):
        self.header = header

    def setTitle(self, title):
        self.title = title
    
    def setTime(self, time):
        self.time = time
    
    def setDesc(self, desc):
        self.desc = desc
    