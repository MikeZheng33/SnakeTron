class Agent:
    def __init__(self, length, id, position):
        self.length = length
        self.id = id
        self.positon = position

    def getLength(self):
        return self.length
    
    def setLength(self, value):
        self.length = value
        
    def getId(self):
        return self.id
    
    def setId(self, value):
        self.id = value
        
    def getPosition(self):
        return self.position
    
    def setPosition(self, value):
        self.position = value
