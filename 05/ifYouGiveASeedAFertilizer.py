with open('./05/input.txt','r') as file:
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
    newPointList = set()
    for map in transformations[stage]:
        newPointList.add(map[1])
        for point in pointList:
            newValue = point
            if (map[0] + map[2]) <= point < (map[1] + map[2]):
                    newValue = point - (map[2])
            newPointList.add(newValue)
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
pointList = {0}
stages = list(range(len(transformations)))
stages.reverse()
for stage in stages:
    pointList = stepBack(pointList,stage)




minLoc = float('inf')
for seed in p1seeds:
    newLoc = runSeed(seed)
    if newLoc < minLoc:
        minLoc = newLoc

print("Minimum location for part 1:",minLoc)
minLoc = float('inf')

print("total Seeds to test:", len(pointList))

seedsToRun = list(pointList)
seedsToRun.sort()
res = {}
for i in range(len(seedsToRun)):
    seed = seedsToRun[i]
    res[seed] = runSeed(seed)
print(res)

print("Minimum location for part 2:",minLoc)