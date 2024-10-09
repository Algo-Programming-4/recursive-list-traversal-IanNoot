import random

class valueHolder():
    addedValue = 0
    recursions = 0
    deepestRecursion = 0

    
def traverseList(input, depth):

    if (depth != 0):
        valueHolder.recursions += 1
        if depth > valueHolder.deepestRecursion:
            valueHolder.deepestRecursion = depth

    for i in input:
        if type(i) == type([0,1,2]):
            if len(input) > 0:
                traverseList(i, depth + 1)
            else:
                valueHolder.recursions += 1
                if depth + 1 > valueHolder.deepestRecursion:
                    valueHolder.deepestRecursion = depth + 1
        elif type(i) == type(1):
            valueHolder.addedValue += i
    
outputList = []
def createList(input, listDepth):
    if (listDepth < 10):
        for i in range(0, random.randint(1,10), 1):
            createSubList = random.randint(1,3)
            if createSubList == 1:
                input.append(createList([], listDepth + 1))
            else:
                input.append(random.randint(0,10))
    return input

outputList = createList([], 0)
    
print(outputList)

traverseList(outputList, 0)
print("total " + str(valueHolder.addedValue))
print("deepest " + str(valueHolder.deepestRecursion))
print("recursions " + str(valueHolder.recursions))