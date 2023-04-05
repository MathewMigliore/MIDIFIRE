import math
class TimeComplexity(object):
    maximumIterations = [0]*3
    maximumIteration = 0
    timeComplexityString = ""
    maxHeightIterationsInside = [0]*5
    maxHeightMaximumIteration = 0

    cubeCompareIterationsInside = [0]*1
    cubeCompareMaximumIteration = 0

    alternateTestCubeIterationsInside = [0]*1
    alternateTestCubeMaximumIteration = 0

    alternateTestStackIterationsInside = [0]*3
    alternateTestStackMaximumIteration = 0

    isStackableIterationsInside = [0]*4
    isStackableMaximumIteration = 0

    checkStackValueIterationsInside = [0]*2
    checkStackValueMaximumIteration = 0

    alternateTestStackCALLINGisStackable = [0]*1
    alternateTestStackCALLINGisStackableMaximumIteration = 0

    isStackableCALLINGalternateTestCube = [0]*1
    isStackableCALLINGalternateTestCubeMaximumIteration = 0

    isStackableCALLINGcubeCompare = [0]*5
    isStackableCALLINGcubeCompareMaximumIteration = 0

    maxHeightCALLINGalternateTestStack = [0]*1
    maxHeightCALLINGalternateTestStackMaximumIteration = 0

    maxHeightCALLINGcheckStackValue = [0]*1
    maxHeightCALLINGcheckStackValueMaximumIteration = 0

    def __init__(self, maxHeightIterationsInside, maxHeightMaximumIteration, cubeCompareIterationsInside, cubeCompareMaximumIteration, alternateTestCubeIterationsInside, alternateTestCubeMaximumIteration, alternateTestStackIterationsInside, alternateTestStackMaximumIteration, isStackableIterationsInside, isStackableMaximumIteration, checkStackValueIterationsInside, checkStackValueMaximumIteration, alternateTestStackCALLINGisStackable, alternateTestStackCALLINGisStackableMaximumIteration, isStackableCALLINGalternateTestCube, isStackableCALLINGalternateTestCubeMaximumIteration, isStackableCALLINGcubeCompare, isStackableCALLINGcubeCompareMaximumIteration, maxHeightCALLINGalternateTestStack, maxHeightCALLINGalternateTestStackMaximumIteration, maxHeightCALLINGcheckStackValue, maxHeightCALLINGcheckStackValueMaximumIteration,  timeComplexityString):

        self.maxHeightIterationsInside = maxHeightIterationsInside
        self.maxHeightMaximumIteration = maxHeightMaximumIteration
        self.cubeCompareIterationsInside = cubeCompareIterationsInside
        self.cubeCompareMaximumIteration = cubeCompareMaximumIteration
        self.alternateTestCubeIterationsInside = alternateTestCubeIterationsInside
        self.alternateTestCubeMaximumIteration = alternateTestCubeMaximumIteration
        self.alternateTestStackIterationsInside = alternateTestStackIterationsInside
        self.alternateTestStackMaximumIteration = alternateTestStackMaximumIteration
        self.isStackableIterationsInside = isStackableIterationsInside
        self.isStackableMaximumIteration = isStackableMaximumIteration
        self.checkStackValueIterationsInside = checkStackValueIterationsInside
        self.checkStackValueMaximumIteration = checkStackValueMaximumIteration
        self.alternateTestStackCALLINGisStackable = alternateTestStackCALLINGisStackable
        self.alternateTestStackCALLINGisStackableMaximumIteration = alternateTestStackCALLINGisStackableMaximumIteration
        self.isStackableCALLINGalternateTestCube = isStackableCALLINGalternateTestCube
        self.isStackableCALLINGalternateTestCubeMaximumIteration = isStackableCALLINGalternateTestCubeMaximumIteration
        self.isStackableCALLINGcubeCompare = isStackableCALLINGcubeCompare
        self.isStackableCALLINGcubeCompareMaximumIteration = isStackableCALLINGcubeCompareMaximumIteration
        self.maxHeightCALLINGalternateTestStack = maxHeightCALLINGalternateTestStack
        self.maxHeightCALLINGalternateTestStackMaximumIteration = maxHeightCALLINGalternateTestStackMaximumIteration
        self.maxHeightCALLINGcheckStackValue = maxHeightCALLINGcheckStackValue
        self.maxHeightCALLINGcheckStackValueMaximumIteration = maxHeightCALLINGcheckStackValueMaximumIteration
def calculateDefComplexity(calls):
    maxIteration = 0
    for call in calls:
        if call > maxIteration:
            maxIteration = call
    if calls[0] > 0:
        return maxIteration//calls[0]
    return maxIteration

def calculateCallComplexity(calls):
    maxIteration = 0
    minIteration = 0
    for call in calls:
        if call > maxIteration:
            maxIteration = call
        elif call < minIteration:
            minIteration = call
def calculateComplexity(length):
    TimeComplexity.maxHeightMaximumIteration = calculateDefComplexity(TimeComplexity.maxHeightIterationsInside)
    TimeComplexity.cubeCompareMaximumIteration = calculateDefComplexity(TimeComplexity.cubeCompareIterationsInside)
    TimeComplexity.alternateTestCubeMaximumIteration = calculateDefComplexity(TimeComplexity.alternateTestCubeIterationsInside)
    TimeComplexity.alternateTestStackMaximumIteration = calculateDefComplexity(TimeComplexity.alternateTestStackIterationsInside)
    TimeComplexity.isStackableMaximumIteration = calculateDefComplexity(TimeComplexity.isStackableIterationsInside)
    TimeComplexity.checkStackValueMaximumIteration = calculateDefComplexity(TimeComplexity.checkStackValueIterationsInside)
    TimeComplexity.alternateTestStackCALLINGisStackable = calculateDefComplexity(TimeComplexity.alternateTestStackCALLINGisStackable)
    TimeComplexity.isStackableCALLINGalternateTestCube = calculateDefComplexity(TimeComplexity.isStackableCALLINGalternateTestCube)
    TimeComplexity.isStackableCALLINGcubeCompare = calculateDefComplexity(TimeComplexity.isStackableCALLINGcubeCompare)
    TimeComplexity.maxHeightCALLINGalternateTestStack = calculateDefComplexity(TimeComplexity.maxHeightCALLINGalternateTestStack)
    TimeComplexity.maxHeightCALLINGcheckStackValue = calculateDefComplexity(TimeComplexity.maxHeightCALLINGcheckStackValue)

    TimeComplexity.maximumIterations[0] = TimeComplexity.maxHeightMaximumIteration*TimeComplexity.alternateTestStackMaximumIteration*TimeComplexity.isStackableMaximumIteration*TimeComplexity.alternateTestCubeMaximumIteration*1
    TimeComplexity.maximumIterations[1] = TimeComplexity.maxHeightMaximumIteration*TimeComplexity.checkStackValueMaximumIteration*1
    TimeComplexity.maximumIterations[2] = TimeComplexity.maxHeightMaximumIteration*TimeComplexity.alternateTestStackMaximumIteration*TimeComplexity.isStackableMaximumIteration*TimeComplexity.cubeCompareMaximumIteration*1
    TimeComplexity.maximumIterations.sort()
    TimeComplexity.maximumIteration = TimeComplexity.maximumIterations[-1]
    if TimeComplexity.maximumIteration == 1:
        TimeComplexity.timeComplexityString = "O(1)"
    else:
        length = len(length)
        while TimeComplexity.maximumIteration > math.log(length):
            TimeComplexity.timeComplexityString+=returnComplexity(length)
        TimeComplexity.timeComplexityString = "O(" + TimeComplexity.timeComplexityString + ")"
def returnComplexity(length):
    if TimeComplexity.maximumIteration >= length**length:
        TimeComplexity.maximumIteration/= length**length
        return "n^n"
    elif TimeComplexity.maximumIteration >= math.factorial(length):
        TimeComplexity.maximumIteration/= math.factorial(length)
        return "n!"
    elif TimeComplexity.maximumIteration >= 2**length:
        TimeComplexity.maximumIteration/= 2**length
        return "2^n"
    elif TimeComplexity.maximumIteration >= length**4:
        TimeComplexity.maximumIteration/= length**4
        return "n^4"
    elif TimeComplexity.maximumIteration >= length**3:
        TimeComplexity.maximumIteration/= length**3
        return "n^3"
    elif TimeComplexity.maximumIteration >= length**2:
        TimeComplexity.maximumIteration/= length**2
        return "n^2"
    elif TimeComplexity.maximumIteration >= length:
        TimeComplexity.maximumIteration/= length
        return "n"
    elif TimeComplexity.maximumIteration >= math.sqrt(length):
        TimeComplexity.maximumIteration/= math.sqrt(length)
        return "sqrt(n)"
    elif TimeComplexity.maximumIteration >= math.log(length):
        TimeComplexity.maximumIteration/= math.log(length)
        return "log(n)"
# Users function will go here
def isStackableCALLINGcubeCompareFunction2():
    TimeComplexity.isStackableCALLINGcubeCompare[2]+=1
    return True

def isStackableCALLINGcubeCompareFunction1():
    TimeComplexity.isStackableCALLINGcubeCompare[1]+=1
    return True

def maxHeight(cuboids):
    TimeComplexity.maxHeightIterationsInside[0]+=1
    def cubeCompare(cubeOne, LTorGT, cubeTwo):
        TimeComplexity.cubeCompareIterationsInside[0]+=1
        if (LTorGT == "<="):
            if ((cubeOne[0] <= cubeTwo[0]) & (cubeOne[1] <= cubeTwo[1]) & (cubeOne[2] <= cubeTwo[2])):
                return True
        elif (LTorGT == ">="):
            if ((cubeOne[0] >= cubeTwo[0]) & (cubeOne[1] >= cubeTwo[1]) & (cubeOne[2] >= cubeTwo[2])):
                return True
        else:
            return False
    def alternateTestCube(cube, index):
        TimeComplexity.alternateTestCubeIterationsInside[0]+=1
        if index%2==0:
            cube[0], cube[1] = cube [1], cube[0]
        else:
            cube[1], cube[-1] = cube [-1], cube[1]
        return cube
    def alternateTestStack(variationStack, testCubes):
        TimeComplexity.alternateTestStackIterationsInside[0]+=1
        variationStackHolder = []
        variationStackHolderHolder = []
        variationStack = [variationStack]
        for i, testCube in enumerate(testCubes):
            TimeComplexity.alternateTestStackIterationsInside[1]+=1
            for vStack in variationStack:
                TimeComplexity.alternateTestStackIterationsInside[2]+=1
                variationStackHolder = isStackable(vStack, testCube[:])
                TimeComplexity.alternateTestStackCALLINGisStackable[0]+=1
                if len(variationStackHolder)>0:
                    variationStackHolderHolder.append(variationStackHolder)
            if (len(variationStackHolderHolder)>0):
                variationStack = variationStackHolderHolder[0]
            variationStackHolder = []
            variationStackHolderHolder = []
        return variationStack
    def isStackable(testCubeList, testCube):
        TimeComplexity.isStackableIterationsInside[0]+=1
        variationCubeList = []
        alternateCube = []
        i=0
        while (i<len(testCubeList)):
            TimeComplexity.isStackableIterationsInside[1]+=1
            z=0
            while(z<6):
                TimeComplexity.isStackableIterationsInside[2]+=1
                if z>0:
                    alternateCube = alternateTestCube(testCube, z)
                    TimeComplexity.isStackableCALLINGalternateTestCube[0]+=1
                else:
                    alternateCube = testCube
                TimeComplexity.isStackableCALLINGcubeCompare[0]+=1
                if (cubeCompare(testCubeList[-1], "<=", alternateCube)):
                    testCubeList.append(alternateCube[:])
                    variationCubeList.append(testCubeList[:])
                    del testCubeList[-1]
                elif(isStackableCALLINGcubeCompareFunction1() and (cubeCompare(testCubeList[0], ">=", alternateCube))):

                    testCubeList.insert((0), alternateCube[:])
                    variationCubeList.append(testCubeList[:])
                    del testCubeList[0]
                elif(isStackableCALLINGcubeCompareFunction2() and  (cubeCompare(testCubeList[0], "<=", alternateCube))):

                    x=0
                    while(x<len(testCubeList)-1):
                        TimeComplexity.isStackableIterationsInside[3]+=1
                        TimeComplexity.isStackableCALLINGcubeCompare[3]+=1
                        if (cubeCompare(testCubeList[x], "<=", alternateCube)):
                            TimeComplexity.isStackableCALLINGcubeCompare[4]+=1
                            if (cubeCompare(testCubeList[x+1], ">=", alternateCube)):
                                testCubeList.insert((x+1), alternateCube[:])
                                variationCubeList.append(testCubeList[:])
                                del testCubeList[x+1]
                                break
                        x+=1
                z+=1
            i+=1
        return variationCubeList
    def checkStackValue(cubeList):
        TimeComplexity.checkStackValueIterationsInside[0]+=1
        stackValue = 0
        valueOne = 0
        valueTwo = 0
        valueThree = 0
        for cube in cubeList:
                TimeComplexity.checkStackValueIterationsInside[1]+=1
                valueOne+=cube[0]
                valueTwo+=cube[1]
                valueThree+=cube[2]
        cubeList = [valueOne, valueTwo, valueThree]
        cubeList.sort()
        stackValue = cubeList[-1]
        return stackValue
    sortedCubes = []
    testCubeList = []
    testCubeListAll = []
    cuberHolder = []
    finalValue = 0
    x=0
    for cube in cuboids:
        TimeComplexity.maxHeightIterationsInside[1]+=1
        cubeHolder = cube
        sortedCubes.append(sorted(cubeHolder))
    if len(sortedCubes)==1:
        finalValue = sortedCubes[0][-1]
    else:
        i=0
        while(i<len(sortedCubes)):
            TimeComplexity.maxHeightIterationsInside[2]+=1
            stackValue = 0
            testCubeList.append(sortedCubes[i])
            testSortedCubes = sortedCubes[:]
            testSortedCubes.remove(sortedCubes[i])
            z=0
            while (z<len(testSortedCubes)):
                TimeComplexity.maxHeightIterationsInside[3]+=1
                inputCubes = alternateTestStack(testCubeList, (testSortedCubes[z:] + testSortedCubes[:z]))
                TimeComplexity.maxHeightCALLINGalternateTestStack[0]+=1
                for stack in inputCubes:
                    TimeComplexity.maxHeightIterationsInside[4]+=1
                    stackValue = checkStackValue(stack)
                    TimeComplexity.maxHeightCALLINGcheckStackValue[0]+=1
                    if(finalValue<stackValue):
                        finalValue=stackValue
                z+=1
            testCubeList = []
            i+=1
    return finalValue


inputCases = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
maxHeight(inputCases)
calculateComplexity(inputCases)
print(TimeComplexity.timeComplexityString)
# class TimeComplexity(object):
#     maximumIterations = [0]*3
#     maximumIteration = 0
#     timeComplexityString = ""
#     maxHeightIterationsInside = [0]*5
#     maxHeightMaximumIteration = 0

#     cubeCompareIterationsInside = [0]*1
#     cubeCompareMaximumIteration = 0

#     alternateTestCubeIterationsInside = [0]*1
#     alternateTestCubeMaximumIteration = 0

#     alternateTestStackIterationsInside = [0]*3
#     alternateTestStackMaximumIteration = 0

#     isStackableIterationsInside = [0]*4
#     isStackableMaximumIteration = 0

#     checkStackValueIterationsInside = [0]*2
#     checkStackValueMaximumIteration = 0

#     alternateTestStackCALLINGisStackable = [0]*1
#     alternateTestStackCALLINGisStackableMaximumIteration = 0

#     isStackableCALLINGalternateTestCube = [0]*1
#     isStackableCALLINGalternateTestCubeMaximumIteration = 0

#     isStackableCALLINGcubeCompare = [0]*5
#     isStackableCALLINGcubeCompareMaximumIteration = 0

#     maxHeightCALLINGalternateTestStack = [0]*1
#     maxHeightCALLINGalternateTestStackMaximumIteration = 0

#     maxHeightCALLINGcheckStackValue = [0]*1
#     maxHeightCALLINGcheckStackValueMaximumIteration = 0

#     def __init__(self, maxHeightIterationsInside, maxHeightMaximumIteration, cubeCompareIterationsInside, cubeCompareMaximumIteration, alternateTestCubeIterationsInside, alternateTestCubeMaximumIteration, alternateTestStackIterationsInside, alternateTestStackMaximumIteration, isStackableIterationsInside, isStackableMaximumIteration, checkStackValueIterationsInside, checkStackValueMaximumIteration, alternateTestStackCALLINGisStackable, alternateTestStackCALLINGisStackableMaximumIteration, isStackableCALLINGalternateTestCube, isStackableCALLINGalternateTestCubeMaximumIteration, isStackableCALLINGcubeCompare, isStackableCALLINGcubeCompareMaximumIteration, maxHeightCALLINGalternateTestStack, maxHeightCALLINGalternateTestStackMaximumIteration, maxHeightCALLINGcheckStackValue, maxHeightCALLINGcheckStackValueMaximumIteration,  timeComplexityString):

#         self.maxHeightIterationsInside = maxHeightIterationsInside
#         self.maxHeightMaximumIteration = maxHeightMaximumIteration
#         self.cubeCompareIterationsInside = cubeCompareIterationsInside
#         self.cubeCompareMaximumIteration = cubeCompareMaximumIteration
#         self.alternateTestCubeIterationsInside = alternateTestCubeIterationsInside
#         self.alternateTestCubeMaximumIteration = alternateTestCubeMaximumIteration
#         self.alternateTestStackIterationsInside = alternateTestStackIterationsInside
#         self.alternateTestStackMaximumIteration = alternateTestStackMaximumIteration
#         self.isStackableIterationsInside = isStackableIterationsInside
#         self.isStackableMaximumIteration = isStackableMaximumIteration
#         self.checkStackValueIterationsInside = checkStackValueIterationsInside
#         self.checkStackValueMaximumIteration = checkStackValueMaximumIteration
#         self.alternateTestStackCALLINGisStackable = alternateTestStackCALLINGisStackable
#         self.alternateTestStackCALLINGisStackableMaximumIteration = alternateTestStackCALLINGisStackableMaximumIteration
#         self.isStackableCALLINGalternateTestCube = isStackableCALLINGalternateTestCube
#         self.isStackableCALLINGalternateTestCubeMaximumIteration = isStackableCALLINGalternateTestCubeMaximumIteration
#         self.isStackableCALLINGcubeCompare = isStackableCALLINGcubeCompare
#         self.isStackableCALLINGcubeCompareMaximumIteration = isStackableCALLINGcubeCompareMaximumIteration
#         self.maxHeightCALLINGalternateTestStack = maxHeightCALLINGalternateTestStack
#         self.maxHeightCALLINGalternateTestStackMaximumIteration = maxHeightCALLINGalternateTestStackMaximumIteration
#         self.maxHeightCALLINGcheckStackValue = maxHeightCALLINGcheckStackValue
#         self.maxHeightCALLINGcheckStackValueMaximumIteration = maxHeightCALLINGcheckStackValueMaximumIteration
# def calculateDefComplexity(calls):
#     maxIteration = 0
#     for call in calls:
#         if call > maxIteration:
#             maxIteration = call
#     if calls[0] > 0:
#         return maxIteration//calls[0]
#     return maxIteration

# def calculateCallComplexity(calls):
#     maxIteration = 0
#     minIteration = 0
#     for call in calls:
#         if call > maxIteration:
#             maxIteration = call
#         elif call < minIteration:
#             minIteration = call
# def calculateComplexity(length):
#     print("maxHeightIterationsInside", TimeComplexity.maxHeightIterationsInside)
#     print("cubeCompareIterationsInside",TimeComplexity.cubeCompareIterationsInside)
#     print("alternateTestCubeIterationsInside",TimeComplexity.alternateTestCubeIterationsInside)
#     print("isStackableIterationsInside",TimeComplexity.isStackableIterationsInside)
#     print("checkStackValueIterationsInside",TimeComplexity.checkStackValueIterationsInside)
#     TimeComplexity.maxHeightMaximumIteration = calculateDefComplexity(TimeComplexity.maxHeightIterationsInside)
#     TimeComplexity.cubeCompareMaximumIteration = calculateDefComplexity(TimeComplexity.cubeCompareIterationsInside)
#     TimeComplexity.alternateTestCubeMaximumIteration = calculateDefComplexity(TimeComplexity.alternateTestCubeIterationsInside)
#     TimeComplexity.alternateTestStackMaximumIteration = calculateDefComplexity(TimeComplexity.alternateTestStackIterationsInside)
#     TimeComplexity.isStackableMaximumIteration = calculateDefComplexity(TimeComplexity.isStackableIterationsInside)
#     TimeComplexity.checkStackValueMaximumIteration = calculateDefComplexity(TimeComplexity.checkStackValueIterationsInside)
#     TimeComplexity.alternateTestStackCALLINGisStackable = calculateDefComplexity(TimeComplexity.alternateTestStackCALLINGisStackable)
#     TimeComplexity.isStackableCALLINGalternateTestCube = calculateDefComplexity(TimeComplexity.isStackableCALLINGalternateTestCube)
#     TimeComplexity.isStackableCALLINGcubeCompare = calculateDefComplexity(TimeComplexity.isStackableCALLINGcubeCompare)
#     TimeComplexity.maxHeightCALLINGalternateTestStack = calculateDefComplexity(TimeComplexity.maxHeightCALLINGalternateTestStack)
#     TimeComplexity.maxHeightCALLINGcheckStackValue = calculateDefComplexity(TimeComplexity.maxHeightCALLINGcheckStackValue)
#     print("maxHeightMaximumIteration", TimeComplexity.maxHeightMaximumIteration)
#     print("cubeCompareMaximumIteration",TimeComplexity.cubeCompareMaximumIteration)
#     print("alternateTestCubeMaximumIteration",TimeComplexity.alternateTestCubeMaximumIteration)
#     print("alternateTestStackMaximumIteration",TimeComplexity.alternateTestStackMaximumIteration)
#     print("isStackableMaximumIteration",TimeComplexity.isStackableMaximumIteration)
#     TimeComplexity.maximumIterations[0] = TimeComplexity.maxHeightMaximumIteration*TimeComplexity.alternateTestStackMaximumIteration*TimeComplexity.isStackableMaximumIteration*TimeComplexity.alternateTestCubeMaximumIteration*1
#     TimeComplexity.maximumIterations[1] = TimeComplexity.maxHeightMaximumIteration*TimeComplexity.checkStackValueMaximumIteration*1
#     TimeComplexity.maximumIterations[2] = TimeComplexity.maxHeightMaximumIteration*TimeComplexity.alternateTestStackMaximumIteration*TimeComplexity.isStackableMaximumIteration*TimeComplexity.cubeCompareMaximumIteration*1
#     TimeComplexity.maximumIterations.sort()
#     TimeComplexity.maximumIteration = TimeComplexity.maximumIterations[-1]
#     print("maximumIteration",TimeComplexity.maximumIteration)
    
#     if TimeComplexity.maximumIteration == 1:
#         TimeComplexity.timeComplexityString = "O(1)"
#     else:
#         length = len(length)
#         while TimeComplexity.maximumIteration > math.log(length):
#             TimeComplexity.timeComplexityString+=returnComplexity(length)
#         TimeComplexity.timeComplexityString = "O(" + TimeComplexity.timeComplexityString + ")"
# def returnComplexity(length):
#     if TimeComplexity.maximumIteration >= length**length:
#         TimeComplexity.maximumIteration/= length**length
#         return "n^n"
#     elif TimeComplexity.maximumIteration >= math.factorial(length):
#         TimeComplexity.maximumIteration/= math.factorial(length)
#         return "n!"
#     elif TimeComplexity.maximumIteration >= 2**length:
#         TimeComplexity.maximumIteration/= 2**length
#         return "2^n"
#     elif TimeComplexity.maximumIteration >= length**4:
#         TimeComplexity.maximumIteration/= length**4
#         return "n^4"
#     elif TimeComplexity.maximumIteration >= length**3:
#         TimeComplexity.maximumIteration/= length**3
#         return "n^3"
#     elif TimeComplexity.maximumIteration >= length**2:
#         TimeComplexity.maximumIteration/= length**2
#         return "n^2"
#     elif TimeComplexity.maximumIteration >= length:
#         TimeComplexity.maximumIteration/= length
#         return "n"
#     elif TimeComplexity.maximumIteration >= math.sqrt(length):
#         TimeComplexity.maximumIteration/= math.sqrt(length)
#         return "sqrt(n)"
#     elif TimeComplexity.maximumIteration >= math.log(length):
#         TimeComplexity.maximumIteration/= math.log(length)
#         return "log(n)"
# # Users function will go here
# def isStackableCALLINGcubeCompareFunction2():
#     TimeComplexity.isStackableCALLINGcubeCompare[2]+=1
#     return True

# def isStackableCALLINGcubeCompareFunction1():
#     TimeComplexity.isStackableCALLINGcubeCompare[1]+=1
#     return True

# def maxHeight(cuboids):
#     TimeComplexity.maxHeightIterationsInside[0]+=1
#     def cubeCompare(cubeOne, LTorGT, cubeTwo):
#         TimeComplexity.cubeCompareIterationsInside[0]+=1
#         if (LTorGT == "<="):
#             if ((cubeOne[0] <= cubeTwo[0]) & (cubeOne[1] <= cubeTwo[1]) & (cubeOne[2] <= cubeTwo[2])):
#                 return True
#         elif (LTorGT == ">="):
#             if ((cubeOne[0] >= cubeTwo[0]) & (cubeOne[1] >= cubeTwo[1]) & (cubeOne[2] >= cubeTwo[2])):
#                 return True
#         else:
#             return False
#     def alternateTestCube(cube, index):
#         TimeComplexity.alternateTestCubeIterationsInside[0]+=1
#         if index%2==0:
#             cube[0], cube[1] = cube [1], cube[0]
#         else:
#             cube[1], cube[-1] = cube [-1], cube[1]
#         return cube
#     def alternateTestStack(variationStack, testCubes):
#         TimeComplexity.alternateTestStackIterationsInside[0]+=1
#         variationStackHolder = []
#         variationStackHolderHolder = []
#         variationStack = [variationStack]
#         for i, testCube in enumerate(testCubes):
#             TimeComplexity.alternateTestStackIterationsInside[1]+=1
#             for vStack in variationStack:
#                 TimeComplexity.alternateTestStackIterationsInside[2]+=1
#                 variationStackHolder = isStackable(vStack, testCube[:])
#                 TimeComplexity.alternateTestStackCALLINGisStackable[0]+=1
#                 if len(variationStackHolder)>0:
#                     variationStackHolderHolder.append(variationStackHolder)
#             if (len(variationStackHolderHolder)>0):
#                 variationStack = variationStackHolderHolder[0]
#             variationStackHolder = []
#             variationStackHolderHolder = []
#         return variationStack
#     def isStackable(testCubeList, testCube):
#         TimeComplexity.isStackableIterationsInside[0]+=1
#         variationCubeList = []
#         alternateCube = []
#         i=0
#         while (i<len(testCubeList)):
#             TimeComplexity.isStackableIterationsInside[1]+=1
#             z=0
#             while(z<6):
#                 TimeComplexity.isStackableIterationsInside[2]+=1
#                 if z>0:
#                     alternateCube = alternateTestCube(testCube, z)
#                     TimeComplexity.isStackableCALLINGalternateTestCube[0]+=1
#                 else:
#                     alternateCube = testCube
#                 TimeComplexity.isStackableCALLINGcubeCompare[0]+=1
#                 if (cubeCompare(testCubeList[-1], "<=", alternateCube)):
#                     testCubeList.append(alternateCube[:])
#                     variationCubeList.append(testCubeList[:])
#                     del testCubeList[-1]
#                 elif(isStackableCALLINGcubeCompareFunction1() and (cubeCompare(testCubeList[0], ">=", alternateCube))):

#                     testCubeList.insert((0), alternateCube[:])
#                     variationCubeList.append(testCubeList[:])
#                     del testCubeList[0]
#                 elif(isStackableCALLINGcubeCompareFunction2() and  (cubeCompare(testCubeList[0], "<=", alternateCube))):

#                     x=0
#                     while(x<len(testCubeList)-1):
#                         TimeComplexity.isStackableIterationsInside[3]+=1
#                         TimeComplexity.isStackableCALLINGcubeCompare[3]+=1
#                         if (cubeCompare(testCubeList[x], "<=", alternateCube)):
#                             TimeComplexity.isStackableCALLINGcubeCompare[4]+=1
#                             if (cubeCompare(testCubeList[x+1], ">=", alternateCube)):
#                                 testCubeList.insert((x+1), alternateCube[:])
#                                 variationCubeList.append(testCubeList[:])
#                                 del testCubeList[x+1]
#                                 break
#                         x+=1
#                 z+=1
#             i+=1
#         return variationCubeList
#     def checkStackValue(cubeList):
#         TimeComplexity.checkStackValueIterationsInside[0]+=1
#         stackValue = 0
#         valueOne = 0
#         valueTwo = 0
#         valueThree = 0
#         for cube in cubeList:
#                 TimeComplexity.checkStackValueIterationsInside[1]+=1
#                 valueOne+=cube[0]
#                 valueTwo+=cube[1]
#                 valueThree+=cube[2]
#         cubeList = [valueOne, valueTwo, valueThree]
#         cubeList.sort()
#         stackValue = cubeList[-1]
#         return stackValue
#     sortedCubes = []
#     testCubeList = []
#     testCubeListAll = []
#     cuberHolder = []
#     finalValue = 0
#     x=0
#     for cube in cuboids:
#         TimeComplexity.maxHeightIterationsInside[1]+=1
#         cubeHolder = cube
#         sortedCubes.append(sorted(cubeHolder))
#     if len(sortedCubes)==1:
#         finalValue = sortedCubes[0][-1]
#     else:
#         i=0
#         while(i<len(sortedCubes)):
#             TimeComplexity.maxHeightIterationsInside[2]+=1
#             stackValue = 0
#             testCubeList.append(sortedCubes[i])
#             testSortedCubes = sortedCubes[:]
#             testSortedCubes.remove(sortedCubes[i])
#             z=0
#             while (z<len(testSortedCubes)):
#                 TimeComplexity.maxHeightIterationsInside[3]+=1
#                 inputCubes = alternateTestStack(testCubeList, (testSortedCubes[z:] + testSortedCubes[:z]))
#                 TimeComplexity.maxHeightCALLINGalternateTestStack[0]+=1
#                 for stack in inputCubes:
#                     TimeComplexity.maxHeightIterationsInside[4]+=1
#                     stackValue = checkStackValue(stack)
#                     TimeComplexity.maxHeightCALLINGcheckStackValue[0]+=1
#                     if(finalValue<stackValue):
#                         finalValue=stackValue
#                 z+=1
#             testCubeList = []
#             i+=1
#     return finalValue


# inputCases = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6],[7, 8, 9],[4, 5, 6]]
# maxHeight(inputCases)
# calculateComplexity(inputCases)
# print(TimeComplexity.timeComplexityString)
# class TimeComplexity(object):
#     maximumIterations = [0]*
#     timeComplexityString = ""
#     cubeCompareIterationsInside = [0]*1
#     cubeCompareMaximumIteration = 0

#     alternateTestCubeIterationsInside = [0]*1
#     alternateTestCubeMaximumIteration = 0

#     alternateTestStackIterationsInside = [0]*3
#     alternateTestStackMaximumIteration = 0

#     isStackableIterationsInside = [0]*4
#     isStackableMaximumIteration = 0

#     checkStackValueIterationsInside = [0]*2
#     checkStackValueMaximumIteration = 0

#     maxHeightIterationsInside = [0]*8
#     maxHeightMaximumIteration = 0

#     alternateTestStackCALLINGisStackableCalls = [0]*1
#     alternateTestStackCALLINGisStackableCallsMaximumIteration = 0

#     isStackableCALLINGalternateTestCubeCalls = [0]*1
#     isStackableCALLINGalternateTestCubeCallsMaximumIteration = 0

#     isStackableCALLINGcubeCompareCalls = [0]*5
#     isStackableCALLINGcubeCompareCallsMaximumIteration = 0

#     checkStackValueCALLINGalternateTestStackCalls = [0]*1
#     checkStackValueCALLINGalternateTestStackCallsMaximumIteration = 0

#     checkStackValueCALLINGcheckStackValueCalls = [0]*1
#     checkStackValueCALLINGcheckStackValueCallsMaximumIteration = 0

#     def __init__(self, cubeCompareIterationsInside, cubeCompareMaximumIteration, alternateTestCubeIterationsInside, alternateTestCubeMaximumIteration, alternateTestStackIterationsInside, alternateTestStackMaximumIteration, isStackableIterationsInside, isStackableMaximumIteration, checkStackValueIterationsInside, checkStackValueMaximumIteration, maxHeightIterationsInside, maxHeightMaximumIteration, alternateTestStackCALLINGisStackableCalls, alternateTestStackCALLINGisStackableCallsMaximumIteration, isStackableCALLINGalternateTestCubeCalls, isStackableCALLINGalternateTestCubeCallsMaximumIteration, isStackableCALLINGcubeCompareCalls, isStackableCALLINGcubeCompareCallsMaximumIteration, checkStackValueCALLINGalternateTestStackCalls, checkStackValueCALLINGalternateTestStackCallsMaximumIteration, checkStackValueCALLINGcheckStackValueCalls, checkStackValueCALLINGcheckStackValueCallsMaximumIteration,  timeComplexityString):

#         self.cubeCompareIterationsInside = cubeCompareIterationsInside
#         self.cubeCompareMaximumIteration = cubeCompareMaximumIteration
#         self.alternateTestCubeIterationsInside = alternateTestCubeIterationsInside
#         self.alternateTestCubeMaximumIteration = alternateTestCubeMaximumIteration
#         self.alternateTestStackIterationsInside = alternateTestStackIterationsInside
#         self.alternateTestStackMaximumIteration = alternateTestStackMaximumIteration
#         self.isStackableIterationsInside = isStackableIterationsInside
#         self.isStackableMaximumIteration = isStackableMaximumIteration
#         self.checkStackValueIterationsInside = checkStackValueIterationsInside
#         self.checkStackValueMaximumIteration = checkStackValueMaximumIteration
#         self.maxHeightIterationsInside = maxHeightIterationsInside
#         self.maxHeightMaximumIteration = maxHeightMaximumIteration
#         self.alternateTestStackCALLINGisStackableCalls = alternateTestStackCALLINGisStackableCalls
#         self.alternateTestStackCALLINGisStackableCallsMaximumIteration = alternateTestStackCALLINGisStackableCallsMaximumIteration
#         self.isStackableCALLINGalternateTestCubeCalls = isStackableCALLINGalternateTestCubeCalls
#         self.isStackableCALLINGalternateTestCubeCallsMaximumIteration = isStackableCALLINGalternateTestCubeCallsMaximumIteration
#         self.isStackableCALLINGcubeCompareCalls = isStackableCALLINGcubeCompareCalls
#         self.isStackableCALLINGcubeCompareCallsMaximumIteration = isStackableCALLINGcubeCompareCallsMaximumIteration
#         self.checkStackValueCALLINGalternateTestStackCalls = checkStackValueCALLINGalternateTestStackCalls
#         self.checkStackValueCALLINGalternateTestStackCallsMaximumIteration = checkStackValueCALLINGalternateTestStackCallsMaximumIteration
#         self.checkStackValueCALLINGcheckStackValueCalls = checkStackValueCALLINGcheckStackValueCalls
#         self.checkStackValueCALLINGcheckStackValueCallsMaximumIteration = checkStackValueCALLINGcheckStackValueCallsMaximumIteration
# # Takes the calls and returns the max iteration
# def calculateDefComplexity(calls):
#     maxIteration = 0
#     for call in calls:
#         if call > maxIteration:
#             maxIteration = call
#     if calls[0] > 0:
#         return maxIteration//calls[0]
#     return maxIteration

# def calculateCallComplexity(calls):
#     maxIteration = 0
#     minIteration = 0
#     for call in calls:
#         if call > maxIteration:
#             maxIteration = call
#         elif call < minIteration:
#             minIteration = call  

# def calculateComplexity(length):
#     iterationsInside = [TimeComplexity.cubeCompareIterationsInside, TimeComplexity.alternateTestCubeIterationsInside, TimeComplexity.alternateTestStackIterationsInside, TimeComplexity.isStackableIterationsInside, TimeComplexity.checkStackValueIterationsInside, TimeComplexity.maxHeightIterationsInside, TimeComplexity.alternateTestStackCALLINGisStackableCalls, TimeComplexity.isStackableCALLINGalternateTestCubeCalls, TimeComplexity.isStackableCALLINGcubeCompareCalls, TimeComplexity.checkStackValueCALLINGalternateTestStackCalls, TimeComplexity.checkStackValueCALLINGcheckStackValueCalls, ]
#     TimeComplexity.cubeCompareMaximumIteration = calculateCallComplexity(TimeComplexity.cubeCompareIterationsInside)

    
#     TimeComplexity.alternateTestCubeIterationsInside
#     TimeComplexity.alternateTestStackIterationsInside
#     TimeComplexity.isStackableIterationsInside
#     TimeComplexity.checkStackValueIterationsInside
#     TimeComplexity.maxHeightIterationsInside

#     x = TimeComplexity.isStackableCALLINGcubeCompareCalls.sort

#     # Now you take these and find the highest value
#     # Make a function that takes the first value of the caller function and the arrays below 
#     # Once you have the highest value you multiply it by the maximum itration value of that function
#     # Make a function that iterates through them top
#     TimeComplexity.alternateTestStackCALLINGisStackableCalls
#     TimeComplexity.isStackableCALLINGalternateTestCubeCalls
#     TimeComplexity.isStackableCALLINGcubeCompareCalls
#     TimeComplexity.checkStackValueCALLINGalternateTestStackCalls
#     TimeComplexity.checkStackValueCALLINGcheckStackValueCalls
#     for iteration in iterationsInside:
#         for lineIteration in iteration:
#             if lineIteration > TimeComplexity.maximumIteration:
#                 TimeComplexity.maximumIteration = lineIteration
#     if TimeComplexity.maximumIteration == 1:
#         TimeComplexity.timeComplexityString = "O(1)"
#     else:
#         length = len(length)
#         while TimeComplexity.maximumIteration > math.log(length):
#             TimeComplexity.timeComplexityString+=returnComplexity(length)
#         TimeComplexity.timeComplexityString = "O(" + TimeComplexity.timeComplexityString + ")"
# def returnComplexity(length):
#     if TimeComplexity.maximumIteration >= length**length:
#         TimeComplexity.maximumIteration/= length**length
#         return "n^n"
#     elif TimeComplexity.maximumIteration >= math.factorial(length):
#         TimeComplexity.maximumIteration/= math.factorial(length)
#         return "n!"
#     elif TimeComplexity.maximumIteration >= 2**length:
#         TimeComplexity.maximumIteration/= 2**length
#         return "2^n"
#     elif TimeComplexity.maximumIteration >= length**4:
#         TimeComplexity.maximumIteration/= length**4
#         return "n^4"
#     elif TimeComplexity.maximumIteration >= length**3:
#         TimeComplexity.maximumIteration/= length**3
#         return "n^3"
#     elif TimeComplexity.maximumIteration >= length**2:
#         TimeComplexity.maximumIteration/= length**2
#         return "n^2"
#     elif TimeComplexity.maximumIteration >= length:
#         TimeComplexity.maximumIteration/= length
#         return "n"
#     elif TimeComplexity.maximumIteration >= math.sqrt(length):
#         TimeComplexity.maximumIteration/= math.sqrt(length)
#         return "sqrt(n)"
#     elif TimeComplexity.maximumIteration >= math.log(length):
#         TimeComplexity.maximumIteration/= math.log(length)
#         return "log(n)"
# # Users function will go here
# def isStackableCALLINGcubeCompareFunction2():
#     TimeComplexity.isStackableCALLINGcubeCompareCalls[2]+=1
#     return True

# def isStackableCALLINGcubeCompareFunction1():
#     TimeComplexity.isStackableCALLINGcubeCompareCalls[1]+=1
#     return True

# def maxHeight(cuboids):
#     TimeComplexity.maxHeightIterationsInside[0]+=1
#     def cubeCompare(cubeOne, LTorGT, cubeTwo):
#         TimeComplexity.cubeCompareIterationsInside[0]+=1
#         if (LTorGT == "<="):
#             if ((cubeOne[0] <= cubeTwo[0]) & (cubeOne[1] <= cubeTwo[1]) & (cubeOne[2] <= cubeTwo[2])):
#                 return True
#         elif (LTorGT == ">="):
#             if ((cubeOne[0] >= cubeTwo[0]) & (cubeOne[1] >= cubeTwo[1]) & (cubeOne[2] >= cubeTwo[2])):
#                 return True
#         else:
#             return False
#     def alternateTestCube(cube, index):
#         TimeComplexity.alternateTestCubeIterationsInside[0]+=1
#         if index%2==0:
#             cube[0], cube[1] = cube [1], cube[0]
#         else:
#             cube[1], cube[-1] = cube [-1], cube[1]
#         return cube
#     def alternateTestStack(variationStack, testCubes):
#         TimeComplexity.alternateTestStackIterationsInside[0]+=1
#         variationStackHolder = []
#         variationStackHolderHolder = []
#         variationStack = [variationStack]
#         for i, testCube in enumerate(testCubes):
#             TimeComplexity.alternateTestStackIterationsInside[1]+=1
#             for vStack in variationStack:
#                 TimeComplexity.alternateTestStackIterationsInside[2]+=1
#                 variationStackHolder = isStackable(vStack, testCube[:])
#                 TimeComplexity.alternateTestStackCALLINGisStackableCalls[0]+=1
#                 if len(variationStackHolder)>0:
#                     variationStackHolderHolder.append(variationStackHolder)
#             if (len(variationStackHolderHolder)>0):
#                 variationStack = variationStackHolderHolder[0]
#             variationStackHolder = []
#             variationStackHolderHolder = []
#         return variationStack
#     def isStackable(testCubeList, testCube):
#         TimeComplexity.isStackableIterationsInside[0]+=1
#         variationCubeList = []
#         alternateCube = []
#         i=0
#         while (i<len(testCubeList)):
#             TimeComplexity.isStackableIterationsInside[1]+=1
#             z=0
#             while(z<6):
#                 TimeComplexity.isStackableIterationsInside[2]+=1
#                 if z>0:
#                     alternateCube = alternateTestCube(testCube, z)
#                     TimeComplexity.isStackableCALLINGalternateTestCubeCalls[0]+=1
#                 else:
#                     alternateCube = testCube
#                 TimeComplexity.isStackableCALLINGcubeCompareCalls[0]+=1
#                 if (cubeCompare(testCubeList[-1], "<=", alternateCube)):
#                     testCubeList.append(alternateCube[:])
#                     variationCubeList.append(testCubeList[:])
#                     del testCubeList[-1]
#                 elif(isStackableCALLINGcubeCompareFunction1() and (cubeCompare(testCubeList[0], ">=", alternateCube))):
#                     testCubeList.insert((0), alternateCube[:])
#                     variationCubeList.append(testCubeList[:])
#                     del testCubeList[0]
#                 elif(isStackableCALLINGcubeCompareFunction2() and  (cubeCompare(testCubeList[0], "<=", alternateCube))):
#                     x=0
#                     while(x<len(testCubeList)-1):
#                         TimeComplexity.isStackableIterationsInside[3]+=1
#                         TimeComplexity.isStackableCALLINGcubeCompareCalls[3]+=1
#                         if (cubeCompare(testCubeList[x], "<=", alternateCube)):
#                             TimeComplexity.isStackableCALLINGcubeCompareCalls[4]+=1
#                             if (cubeCompare(testCubeList[x+1], ">=", alternateCube)):
#                                 testCubeList.insert((x+1), alternateCube[:])
#                                 variationCubeList.append(testCubeList[:])
#                                 del testCubeList[x+1]
#                                 break
#                         x+=1
#                 z+=1
#             i+=1
#         return variationCubeList
#     def checkStackValue(cubeList):
#         TimeComplexity.checkStackValueIterationsInside[0]+=1
#         stackValue = 0
#         valueOne = 0
#         valueTwo = 0
#         valueThree = 0
#         for cube in cubeList:
#                 TimeComplexity.checkStackValueIterationsInside[1]+=1
#                 valueOne+=cube[0]
#                 valueTwo+=cube[1]
#                 valueThree+=cube[2]
#         cubeList = [valueOne, valueTwo, valueThree]
#         cubeList.sort()
#         stackValue = cubeList[-1]
#         return stackValue
#     sortedCubes = []
#     testCubeList = []
#     testCubeListAll = []
#     cuberHolder = []
#     finalValue = 0
#     x=0
#     for cube in cuboids:
#         TimeComplexity.maxHeightIterationsInside[1]+=1
#         cubeHolder = cube
#         sortedCubes.append(sorted(cubeHolder))
#     if len(sortedCubes)==1:
#         finalValue = sortedCubes[0][-1]
#     else:
#         i=0
#         while(i<len(sortedCubes)):
#             TimeComplexity.maxHeightIterationsInside[2]+=1
#             stackValue = 0
#             testCubeList.append(sortedCubes[i])
#             testSortedCubes = sortedCubes[:]
#             testSortedCubes.remove(sortedCubes[i])
#             z=0
#             while (z<len(testSortedCubes)):
#                 TimeComplexity.maxHeightIterationsInside[3]+=1
#                 inputCubes = alternateTestStack(testCubeList, (testSortedCubes[z:] + testSortedCubes[:z]))
#                 TimeComplexity.checkStackValueCALLINGalternateTestStackCalls[0]+=1
#                 for stack in inputCubes:
#                     TimeComplexity.maxHeightIterationsInside[4]+=1
#                     stackValue = checkStackValue(stack)
#                     TimeComplexity.checkStackValueCALLINGcheckStackValueCalls[0]+=1
#                     if(finalValue<stackValue):
#                         finalValue=stackValue
#                 z+=1
#             testCubeList = []
#             i+=1
#     return finalValue


# inputCases = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# maxHeight(inputCases)
# calculateComplexity(inputCases)
# print(TimeComplexity.timeComplexityString)









# class TimeComplexity(object):
#     storeLineIterations = [0]*10
#     maximumIteration = 0
#     timeComplexityString = ""
#     def __init__(self, storeLineIterations, maximumIteration, timeComplexityString):
#         self.storeLineIterations = storeLineIterations
#         self.maximumIteration = maximumIteration
#         self.timeComplexityString = timeComplexityString
# def calculateComplexity(length):
#     for lineIteration in TimeComplexity.storeLineIterations:
#         if lineIteration > TimeComplexity.maximumIteration:
#             TimeComplexity.maximumIteration = lineIteration
#     if TimeComplexity.maximumIteration == 1:
#         TimeComplexity.timeComplexityString = "O(1)"
#     else:
#         length = len(length)
#         while TimeComplexity.maximumIteration > math.log(length):
#             tempComp = returnComplexity(length)
#             TimeComplexity.timeComplexityString+="*"+tempComp
#         TimeComplexity.timeComplexityString = TimeComplexity.timeComplexityString[1:len(TimeComplexity.timeComplexityString)]
#         TimeComplexity.timeComplexityString = "O(" + TimeComplexity.timeComplexityString + ")"
# def returnComplexity(length):
#     if TimeComplexity.maximumIteration >= length**length:
#         TimeComplexity.maximumIteration/= length**length
#         return "n^n"
#     elif TimeComplexity.maximumIteration >= math.factorial(length):
#         TimeComplexity.maximumIteration/= math.factorial(length)
#         return "n!"
#     elif TimeComplexity.maximumIteration >= 2**length:
#         TimeComplexity.maximumIteration/= 2**length
#         return "2^n"
#     elif TimeComplexity.maximumIteration >= length**4:
#         TimeComplexity.maximumIteration/= length**4
#         return "n^4"
#     elif TimeComplexity.maximumIteration >= length**3:
#         TimeComplexity.maximumIteration/= length**3
#         return "n^3"
#     elif TimeComplexity.maximumIteration >= length**2:
#         TimeComplexity.maximumIteration/= length**2
#         return "n^2"
#     elif TimeComplexity.maximumIteration >= length:
#         TimeComplexity.maximumIteration/= length
#         return "n"
#     elif TimeComplexity.maximumIteration >= math.sqrt(length):
#         TimeComplexity.maximumIteration/= math.sqrt(length)
#         return "sqrt(n)"
#     elif TimeComplexity.maximumIteration >= math.log(length):
#         TimeComplexity.maximumIteration/= math.log(length)
#         return "log(n)"
# # Users function will go here
# def maxHeight(cuboids):
#     def cubeCompare(cubeOne, LTorGT, cubeTwo):
#         if (LTorGT == "<="):
#             if ((cubeOne[0] <= cubeTwo[0]) & (cubeOne[1] <= cubeTwo[1]) & (cubeOne[2] <= cubeTwo[2])):
#                 return True
#         elif (LTorGT == ">="):
#             if ((cubeOne[0] >= cubeTwo[0]) & (cubeOne[1] >= cubeTwo[1]) & (cubeOne[2] >= cubeTwo[2])):
#                 return True
#         else:
#             return False
#     def alternateTestCube(cube, index):
#         if index%2==0:
#             cube[0], cube[1] = cube [1], cube[0]
#         else:
#             cube[1], cube[-1] = cube [-1], cube[1]
#         return cube
#     def alternateTestStack(variationStack, testCubes):
#         variationStackHolder = []
#         variationStackHolderHolder = []
#         variationStack = [variationStack]
#         for i, testCube in enumerate(testCubes):
#             TimeComplexity.storeLineIterations[0]+=1
#             for vStack in variationStack:
#                 TimeComplexity.storeLineIterations[1]+=1
#                 variationStackHolder = isStackable(vStack, testCube[:])
#                 if len(variationStackHolder)>0:
#                     variationStackHolderHolder.append(variationStackHolder)
#             if (len(variationStackHolderHolder)>0):
#                 variationStack = variationStackHolderHolder[0]
#             variationStackHolder = []
#             variationStackHolderHolder = []
#         return variationStack
#     def isStackable(testCubeList, testCube):
#         variationCubeList = []
#         alternateCube = []
#         i=0
#         while (i<len(testCubeList)):
#             TimeComplexity.storeLineIterations[2]+=1
#             z=0
#             while(z<6):
#                 TimeComplexity.storeLineIterations[3]+=1
#                 if z>0:
#                     alternateCube = alternateTestCube(testCube, z)
#                 else:
#                     alternateCube = testCube
#                 if (cubeCompare(testCubeList[-1], "<=", alternateCube)):
#                     testCubeList.append(alternateCube[:])
#                     variationCubeList.append(testCubeList[:])
#                     del testCubeList[-1]
#                 elif(cubeCompare(testCubeList[0], ">=", alternateCube)):
#                     testCubeList.insert((0), alternateCube[:])
#                     variationCubeList.append(testCubeList[:])
#                     del testCubeList[0]
#                 elif (cubeCompare(testCubeList[0], "<=", alternateCube)):
#                     x=0
#                     while(x<len(testCubeList)-1):
#                         TimeComplexity.storeLineIterations[4]+=1
#                         if (cubeCompare(testCubeList[x], "<=", alternateCube)):
#                             if (cubeCompare(testCubeList[x+1], ">=", alternateCube)):
#                                 testCubeList.insert((x+1), alternateCube[:])
#                                 variationCubeList.append(testCubeList[:])
#                                 del testCubeList[x+1]
#                                 break
#                         x+=1
#                 z+=1
#             i+=1
#         return variationCubeList
#     def checkStackValue(cubeList):
#         stackValue = 0
#         valueOne = 0
#         valueTwo = 0
#         valueThree = 0
#         for cube in cubeList:
#                 TimeComplexity.storeLineIterations[5]+=1
#                 valueOne+=cube[0]
#                 valueTwo+=cube[1]
#                 valueThree+=cube[2]
#         cubeList = [valueOne, valueTwo, valueThree]
#         cubeList.sort()
#         stackValue = cubeList[-1]
#         return stackValue
#     sortedCubes = []
#     testCubeList = []
#     testCubeListAll = []
#     cuberHolder = []
#     finalValue = 0
#     x=0
#     for cube in cuboids:
#         TimeComplexity.storeLineIterations[6]+=1
#         cubeHolder = cube
#         sortedCubes.append(sorted(cubeHolder))
#     if len(sortedCubes)==1:
#         finalValue = sortedCubes[0][-1]
#     else:
#         i=0
#         while(i<len(sortedCubes)):
#             TimeComplexity.storeLineIterations[7]+=1
#             stackValue = 0
#             testCubeList.append(sortedCubes[i])
#             testSortedCubes = sortedCubes[:]
#             testSortedCubes.remove(sortedCubes[i])
#             z=0
#             while (z<len(testSortedCubes)):
#                 TimeComplexity.storeLineIterations[8]+=1
#                 inputCubes = alternateTestStack(testCubeList, (testSortedCubes[z:] + testSortedCubes[:z]))
#                 for stack in inputCubes:
#                     TimeComplexity.storeLineIterations[9]+=1
#                     stackValue = checkStackValue(stack)
#                     if(finalValue<stackValue):
#                         finalValue=stackValue
#                 z+=1
#             testCubeList = []
#             i+=1
#     return finalValue

# inputCases = [[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3],[1, 2, 3]]
# maxHeight(inputCases)
# calculateComplexity(inputCases)
# print(TimeComplexity.timeComplexityString)
# # class TimeComplexity(object):
# #     storeLineIterations = [0]*3
# #     maximumIteration = 0
# #     timeComplexityString = ""
# #     def __init__(self, storeLineIterations, maximumIteration, timeComplexityString):
# #         self.storeLineIterations = storeLineIterations
# #         self.maximumIteration = maximumIteration
# #         self.timeComplexityString = timeComplexityString

# # def calculateComplexity(length):
# #     for lineIteration in TimeComplexity.storeLineIterations:
# #         if lineIteration > TimeComplexity.maximumIteration:
# #             TimeComplexity.maximumIteration = lineIteration
    
# #     if TimeComplexity.maximumIteration == 1:
# #         TimeComplexity.timeComplexityString = "O(1)"
# #     else:
# #         length = len(length)
# #         while TimeComplexity.maximumIteration > math.log(length):
# #             TimeComplexity.timeComplexityString+=returnComplexity(length)
        
# #         TimeComplexity.timeComplexityString = "O(" + TimeComplexity.timeComplexityString + ")"

# # def returnComplexity(length):
# #     if TimeComplexity.maximumIteration >= length**length:
# #         TimeComplexity.maximumIteration/= length**length
# #         return "n^n"
# #     elif TimeComplexity.maximumIteration >= math.factorial(length):
# #         TimeComplexity.maximumIteration/= math.factorial(length)
# #         return "n!"
# #     elif TimeComplexity.maximumIteration >= 2**length:
# #         TimeComplexity.maximumIteration/= 2**length
# #         return "2^n"
# #     elif TimeComplexity.maximumIteration >= length**4:
# #         TimeComplexity.maximumIteration/= length**4
# #         return "n^4"
# #     elif TimeComplexity.maximumIteration >= length**3:
# #         TimeComplexity.maximumIteration/= length**3
# #         return "n^3"
# #     elif TimeComplexity.maximumIteration >= length**2:
# #         TimeComplexity.maximumIteration/= length**2
# #         return "n^2"
# #     elif TimeComplexity.maximumIteration >= length:
# #         TimeComplexity.maximumIteration/= length
# #         return "n"
# #     elif TimeComplexity.maximumIteration >= math.sqrt(length):
# #         TimeComplexity.maximumIteration/= math.sqrt(length)
# #         return "sqrt(n)"
# #     elif TimeComplexity.maximumIteration >= math.log(length):
# #         TimeComplexity.maximumIteration/= math.log(length)
# #         return "log(n)"




# # # Users function will go here
# # def testFunction(test):
# #     TimeComplexity.storeLineIterations[0]+=1 # Each indent will have an associated interable index
# #     for i in range(0, 10):
# #         TimeComplexity.storeLineIterations[1]+=1

# # test = 0

# # testFunction(test)
# # calculateComplexity(test)
# # print(TimeComplexity.timeComplexityString)