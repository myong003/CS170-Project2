import sys
import math

class Ob:
    def __init__(self, classType, features):
        self.classType = classType
        self.features = features

def GetDistance(ob1, ob2, featuresToUse=[1, 2, 3, 4, 5, 6]):
    # dist1 = (ob1.f1 - ob2.f1) * (ob1.f1 - ob2.f1)
    # dist1 = (float(ob1.f2) - float(ob2.f2)) * (float(ob1.f2) - float(ob2.f2))
    # dist2 = (float(ob1.f3) - float(ob2.f3)) * (float(ob1.f3) - float(ob2.f3))
    # dist3 = (float(ob1.f4) - float(ob2.f4)) * (float(ob1.f4) - float(ob2.f4))
    # dist4 = (float(ob1.f5) - float(ob2.f5)) * (float(ob1.f5) - float(ob2.f5))
    # dist5 = (float(ob1.f6) - float(ob2.f6)) * (float(ob1.f6) - float(ob2.f6))
    # dist6 = (float(ob1.f7) - float(ob2.f7)) * (float(ob1.f7) - float(ob2.f7))

    distances = []
    for index in range(len(ob1.features)):
        float1 = float(ob1.features[index])
        float2 = float(ob2.features[index])
        distance = (float1 - float2) * (float1 - float2)
        distances.append(distance)

    sum = 0
    for num in featuresToUse:
        sum += distances[num - 1]

    return math.sqrt(sum)

def BuildNearestNeighbor(featuresToUse):
    numCorrect = 0
    for i in range(len(lines)) :
        entry = lines[i].split()
        newOb = Ob(entry[0], entry[1:len(entry)])

        minDistance = sys.maxsize
        minType = 0

        for k in range(len(lines)) :
            if k != i:
                entry2 = lines[k].split()
                newOb2 = Ob(entry2[0], entry2[1:len(entry2)])
                distance = GetDistance(newOb, newOb2, featuresToUse)
                if distance < minDistance:
                    minDistance = distance
                    minType = newOb2.classType

        # print("Object " + newOb.f1 + " is class " + newOb.f2)
        # print("It's nearest neighbor is " + str(minLocation) + " which is in class " + minType)

        if newOb.classType == minType:
            numCorrect += 1

        accuracy = numCorrect / len(lines)
    return accuracy


# ------MAIN-------

# algorithmType = 0
# while algorithmType != "1" and algorithmType != "2":
#     algorithmType = input("Type the number of the algorithm you want to run. \n1. Forward Selection\n2. Backward Elimination\n")

with open("CS170_Large_Data__10.txt") as file:
    lines = [line.rstrip() for line in file]

maxNumFeatures = len(lines[0].split()) - 1

currBestFeature = 0
currBestFeatures = []
maxAccuracy = 0
bestFeatures = []
bestAccuracy = 0

currentFeatures = [[1], [2], [3], [4], [5], [6]]
numFeatures = 1

while numFeatures < maxNumFeatures:
    maxAccuracy = 0
    for features in currentFeatures:
        tempAccuracy = BuildNearestNeighbor(features)

        if tempAccuracy > maxAccuracy:
            currBestFeature = features[numFeatures - 1]
            currBestFeatures = features
            maxAccuracy = tempAccuracy
        
        print("Features " + str(features) + " has " + str(tempAccuracy) + " accuracy")
    
    if maxAccuracy > bestAccuracy:
        bestAccuracy = maxAccuracy
        bestFeatures = currBestFeatures

    print("Current best feature added is " + str(currBestFeature))

    currentFeatures.clear()
    for index in range(maxNumFeatures):
        if (index + 1) not in currBestFeatures:
            newList = currBestFeatures.copy()
            newList.append(index + 1)
            currentFeatures.append(newList)
    
    numFeatures += 1


bestFeatures.sort()
print("Features " + str(bestFeatures) + " has the best accuracy of " + str(bestAccuracy))

