class Toolbox:
    tools = []
    def add(self, tool):
        self.tools.append(tool)
    def remove(self, tool):
        self.tools.pop(tool)

class Hammer:
    def __init__(self, color):
        self.color = color
    def smash(self):
        print('SMASH')
    def remove(self):
        print('I removed a nail')

class Screwdriver:
    def __init__(self, size):
        self.size = size
    def screw(self):
        print('I screw')
    def unscrew(self):
        print('I unscrew')