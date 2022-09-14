import random
class Terning():
    def __init__(self, fv):
        self.FaceValue = fv

    def Roll(self):
        self.FaceValue=random.randint(1,6)    

    def GetFaceValue(self):
        return self.FaceValue
