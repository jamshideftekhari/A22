import re
from Terning import Terning
class TerningSpil():
# constructor makes 2 instances of the die with d1 and d2 name 
    def __init__(self):
        self.D1= Terning(0)
        self.D2 = Terning(0)
        self.FvSum = 0
        
     # play method to roll and display values. 
    def Play(self):
        self.D1.Roll()
        fv1 = self.D1.GetFaceValue()
        print ("face value 1 : " + str(fv1))
        self.D2.Roll()
        fv2 = self.D2.GetFaceValue()
        print ("face value 2: " + str(fv2))
        self.FvSum = fv1 + fv2
        if self.FvSum==7:
            print("**********Hurra you win*********")
        else:
            print("************You loose************")    
        
    def GetFvSum(self):
        return self.FvSum

