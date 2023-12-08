from math import lcm
from time import time
startTime = time()
with open('./08/input.txt','r') as file:
    lines = file.readlines()

directions = lines[0][:-1]
def getDir(steps):
    dir = directions[steps % len(directions)]
    return dir

maps = {}
for line in lines[2:]:
    maps[line[:3]] = (line[7:10],line[12:15])

# Part 1
steps = 0
currentPos = 'AAA'
while currentPos != 'ZZZ':
    if getDir(steps) == 'L':
        currentPos = maps.get(currentPos)[0]
    else:
        currentPos = maps.get(currentPos)[1]
    steps += 1
print("Part 1:",steps,'steps')

#Part 2
part2Start = time()
positions = [pos for pos in maps.keys() if pos[-1] == 'A']
cycles = []
for i in range(len(positions)):
    currentPos = positions[i]
    steps = 0
    while currentPos[-1] != 'Z':
        if getDir(steps) == 'L':
            currentPos = maps.get(currentPos)[0]
        else:
            currentPos = maps.get(currentPos)[1]
        steps += 1
    cycles.append(steps)

totalSteps = lcm(*cycles)
part2Elapsed = time()-part2Start

print('Part 2:',totalSteps,'steps')
print('Time elapsed:', (time()-startTime)*1000, 'ms')

# How long would brute force take?
steps = 0
bruteStartTime = time()
positions = [pos for pos in maps.keys() if pos[-1] == 'A']
while steps <= 1000000:
    if getDir(steps) == 'L':
        positions = [maps.get(pos)[0] for pos in positions]
    else:
        positions = [maps.get(pos)[1] for pos in positions]
    steps += 1
bruteMilTime = time()-bruteStartTime
bruteTotTimeSeconds = bruteMilTime * totalSteps / 1000000
bruteTotTimeDays = bruteMilTime * totalSteps / 360000000 /24
improvement = bruteTotTimeSeconds / part2Elapsed
print('Estimated brute force time:',bruteTotTimeDays, 'days')
print('Speed improvement over brute force:',improvement,'times')