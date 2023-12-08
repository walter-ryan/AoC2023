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

print('Part 2:',lcm(*cycles),'steps')
print('Time elapsed:', (time()-startTime)*1000, 'ms')