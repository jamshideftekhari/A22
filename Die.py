import random
class Die:
    def __init__(self, fv):
        self.FaceValue = 0

    def Roll(self):
        self.FaceValue = random.randint(1,6)

    def GetFaceValue(self):
        return self.FaceValue    
        

