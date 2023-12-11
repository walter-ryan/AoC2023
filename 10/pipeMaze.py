with open('./10/input.txt','r') as file:
    lines = file.readlines()

def findStart():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                return (i,j)
    return (-1,-1)

directions = [0,1,2,3]


print('Starting position:',findStart())

prevPos = [findStart(),findStart()]
prevMove = []

nextMove = {
    '|':[0,-1,2,-1],
    '-':[-1,1,-1,3],
    'L':[-1,-1,1,0],
    'J':[-1,0,3,-1],
    '7':[3,2,-1,-1],
    'F':[1,-1,-1,2],
    '.':[-1,-1,-1,-1]    
}

moves = {
    0:(-1,0),
    1:(0,1),
    2:(1,0),
    3:(0,-1)
}

prevMove = []
pos = []
verts = []
start = findStart()
for move in moves.keys():
    letterPos = (start[0]+moves[move][0],start[1]+moves[move][1])
    letter = lines[letterPos[0]][letterPos[1]]
    if nextMove[letter][move] != -1:
        pos.append(letterPos)
        prevMove.append(move)
print(prevMove)
for (letter,nm) in nextMove.items():
    if all([True if pm in nm else False for pm in prevMove]):
        print('Starting letter is',letter)
        lines[start[0]] = lines[start[0]].replace('S',letter)
        if letter != '-':
            verts.append((start,letter))
print(verts)
step = 1

# Find first moves
allPos = [start]
while pos[0] != pos[1]:
    for path in [0,1]:
        letter = lines[pos[path][0]][pos[path][1]]
        move = nextMove.get(letter)[prevMove[path]]
        prevMove[path] = move
        allPos.append(pos[path])
        if letter not in ['.','-']:
            verts.append((pos[path],letter))
        pos[path] = tuple(map(sum,zip(pos[path],moves[move])))
    step += 1
letter = lines[pos[0][0]][pos[0][1]]
allPos.append(pos[0])
if letter not in ['.','-']:
    verts.append((pos[0],letter))
print(step)
allPos.sort()
verts.sort()


cont = 0
for i in range(len(lines)):
    print('Line',i)
    lineCont = 0
    iall = [jj for (ii,jj) in allPos if ii == i]
    # print(iall)
    iverts = [(jj,l) for ((ii,jj),l) in verts if ii == i]
    # print(iverts)
    for j in range(len(lines[i])):
        v = 0
        if j in iall:
            pass
        else:
            line = [l for (jj,l) in iverts if jj > j]
            for i in range(len(line)):
                if line[i] == '|':
                    v += 1
                elif line[i] == 'L':
                    if line[i+1] == '7':
                        v += 1
                elif line[i] == 'F':
                    if line[i+1] == 'J':
                        v += 1
        if v % 2 == 1:
            lineCont += 1
    # print(lineCont)
    cont += lineCont

print(cont)