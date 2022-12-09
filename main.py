import sys

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
    ob1.f1 - ob2.f2

with open("CS170_Small_Data__1.txt") as file:
    lines = [line.rstrip() for line in file]

numCorrect = 0

for i in range(len(lines)) :
    entry = lines[i].split()
    newOb = Ob(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])

    distance = sys.maxsize
    location = sys.maxsize

    for k in range(len(lines)) :
        if k != i:
            entry2 = lines[k].split()
            newOb2 = Ob(entry2[0], entry2[1], entry2[2], entry2[3], entry2[4], entry2[5], entry2[6])