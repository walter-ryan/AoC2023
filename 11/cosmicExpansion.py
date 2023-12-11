with open('./11/input.txt','r') as file:
    lines = file.readlines()

# newLines = []
# for line in lines:
#     newLines.append(line[:-1])
#     if line.count('#') == 0:
#         newLines.append(line[:-1])
# lines = newLines

# newLines = []
# vLen = len(lines)
# hLen = len(lines[0])
# newLines = ['' for l in range(vLen)]

# for j in range(hLen):
#     if any([lines[i][j] == '#' for i in range(vLen)]):
#         for i in range(len(lines)):
#             newLines[i] += lines[i][j]
#     else:
#         for i in range(vLen):
#             newLines[i] += '..'
# lines = newLines

horiz = []
verti = []
for j in range(len(lines[0])):
    if all([lines[i][j] == '.' for i in range(len(lines))]):
        if j == 0:
            horiz.append(1)
        else:
            horiz.append(horiz[-1]+1)
    else:
        if j == 0:
            horiz.append(0)
        else:
            horiz.append(horiz[-1])
for i in range(len(lines)):
    if lines[i].count('#') == 0:
        if i == 0:
            verti.append(1)
        else:
            verti.append(verti[-1]+1)
    else:
        if i == 0:
            verti.append(0)
        else:
            verti.append(verti[-1])
            

gap = 1000000
gals = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '#':
            gals.append((i + (verti[i]*(gap-1)),j + (horiz[j]*(gap-1))))



totDist = 0
pairs = 0
for i in range(len(gals)-1):
    start = gals[i]
    for end in gals[i+1:]:
        pairs += 1
        xDist = abs(end[1] - start[1])
        yDist = abs(end[0] - start[0])
        distance = xDist + yDist 
        totDist += distance
print(totDist)