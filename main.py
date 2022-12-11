import sys
import math

class Ob:
    def __init__(self, f1, f2, f3, f4, f5, f6, f7):
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.f4 = f4
        self.f5 = f5
        self.f6 = f6
        self.f7 = f7

def GetDistance(ob1, ob2):
    # dist1 = (ob1.f1 - ob2.f1) * (ob1.f1 - ob2.f1)
    # dist2 = (float(ob1.f2) - float(ob2.f2)) * (float(ob1.f2) - float(ob2.f2))
    # dist3 = (float(ob1.f3) - float(ob2.f3)) * (float(ob1.f3) - float(ob2.f3))
    dist4 = (float(ob1.f4) - float(ob2.f4)) * (float(ob1.f4) - float(ob2.f4))
    dist5 = (float(ob1.f5) - float(ob2.f5)) * (float(ob1.f5) - float(ob2.f5))
    dist6 = (float(ob1.f6) - float(ob2.f6)) * (float(ob1.f6) - float(ob2.f6))
    # dist7 = (float(ob1.f7) - float(ob2.f7)) * (float(ob1.f7) - float(ob2.f7))

    return math.sqrt(dist4 + dist5 + dist6)
    # return math.sqrt(dist2 + dist3 + dist4 + dist5 + dist6 + dist7)

with open("CS170_Small_Data__1.txt") as file:
    lines = [line.rstrip() for line in file]

numCorrect = 0

for i in range(len(lines)) :
    entry = lines[i].split()
    newOb = Ob(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
    

    minDistance = sys.maxsize
    minLocation = sys.maxsize
    minType = 0

    for k in range(len(lines)) :
        if k != i:
            entry2 = lines[k].split()
            newOb2 = Ob(entry2[0], entry2[1], entry2[2], entry2[3], entry2[4], entry2[5], entry2[6])
            distance = GetDistance(newOb, newOb2)
            if distance < minDistance:
                minDistance = distance
                minLocation = k
                minType = newOb2.f1

    print("Object " + newOb.f1 + " is class " + newOb.f2)
    print("It's nearest neighbor is " + str(minLocation) + " which is in class " + minType)

    if newOb.f1 == minType:
        numCorrect += 1

accuracy = numCorrect / len(lines)
print(accuracy)
