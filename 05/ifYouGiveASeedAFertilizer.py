with open('./05/test.txt','r') as file:
    lines = file.readlines()

def runSeed(seed):
    transformationHistory = [seed]
    for stage in range(len(transformations)):
        newValue = transformationHistory[-1]
        for map in transformations[stage]:
            if map[0] <= transformationHistory[-1] < map[1]:
                newValue = transformationHistory[-1] + (map[2])
        transformationHistory.append(newValue)
    return transformationHistory[-1]

def stepBack(pointList, stage):
    newPointList = []
    for map in transformations[stage]:
        print(map[1])
        newPointList.append(map[1])
        for point in pointList:
            map =  transformations[stage]
            newValue = point
            if (map[0] + map[2]) <= point < (map[1] + map[2]):
                    newValue = point - (map[2])
            newPointList.append(newValue)
    return newPointList

p1seeds = [int(n) for n in lines[0][7:].split()]
p2seedStart = p1seeds[::2]
p2seedEnd = p1seeds[1::2]

transformations = []
transNo = 0
seedsToRun = []
for line in lines[2:]:
    if line[0].isalpha():
        transformations.append([])
    elif line[0].isdigit():
        map = [int(n) for n in line.split()]
        map = [map[1], map[1] + map[2], map[0]-map[1]]
        transformations[-1].append(map)


### CREATE A LIST OF SEEDS TO TEST
pointList = []
for stage in list(range(len(transformations))):
    print("stage = ",stage)
    pointList = stepBack(pointList,stage)
    print("success")



minLoc = float('inf')
for seed in p1seeds:
    newLoc = runSeed(seed)
    if newLoc < minLoc:
        minLoc = newLoc

print("Minimum location for part 1:",minLoc)
minLoc = float('inf')

# print("total Seeds to test:", len(seedsToRun))
# for i in range(len(seedsToRun)):
#     print("Start:", seedsToRun[i], "End:", seedsToRun[i])
#     seed = p2seedStart[i]
#     while seed < p2seedStart[i] + p2seedEnd[i]:
#         newLoc = runSeed(seed)
#         if newLoc < minLoc:
#             minLoc = newLoc
#         seed += 1

print("Minimum location for part 2:",minLoc)