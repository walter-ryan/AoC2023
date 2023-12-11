with open('./09/input.txt','r') as file:
    lines = file.readlines()

def deriv(seqStack):
    prev = seqStack[-1]
    nextLine = [prev[i+1]-prev[i] for i in range(len(prev)-1)]
    return nextLine

seqs = []

for line in lines:
    seqs.append([int(n) for n in line.split()])

totNext = 0
totPrev = 0
for seq in seqs:
    seqStack = [seq]
    while any(seqStack[-1]):
        seqStack.append(deriv(seqStack))
    next = sum([seq[-1] for seq in seqStack])
    # print('Next in sequence:',next)
    firsts = [seq[0] for seq in seqStack]
    prev = 0
    for i in range(len(firsts)):
        if i % 2 == 0:
            prev += firsts[i]
        else:
            prev -= firsts[i]
    print('Previous in sequence:',prev)
    totNext += next
    totPrev += prev

# print('Sum of next values:',totNext)
print('Sum of previous values:',totPrev)