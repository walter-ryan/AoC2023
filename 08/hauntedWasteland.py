from math import lcm
with open('./08/input.txt','r') as file:
    lines = file.readlines()

directions = lines[0][:-1]
def getDir(steps):
    dir = directions[steps % len(directions)]
    return dir





maps = {}
for line in lines[2:]:
    maps[line[:3]] = (line[7:10],line[12:15])


# steps = 0
# currentPos = 'AAA'

# while currentPos != 'ZZZ':
#     print('At',currentPos)
#     print('Going',getDir(steps))
#     if getDir(steps) == 'L':
#         currentPos = maps.get(currentPos)[0]
#     else:
#         currentPos = maps.get(currentPos)[1]
#     print('Landed at', currentPos)
#     steps += 1
# print(steps)


positions = [pos for pos in maps.keys() if pos[-1] == 'A']
steps = 0

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
    print('Made it to Z in',steps)
    cycles.append(steps)

print(lcm(*cycles))