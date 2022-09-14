import random
from Die import Die
from Player import Player
print ("hello py")

d1 = Die(0)
d1.Roll()

d2 = Die(0)
d2.Roll()

p = Player("Jamshid")

print(p)
result = d2.GetFaceValue() + d1.GetFaceValue()
print("face value is: " + str(result))

if (result == 7):
    print("you win")