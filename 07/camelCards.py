with open('./07/input.txt','r') as file:
    lines = file.readlines()

cards = {
    'A':14,
    'K':13,
    'Q':12,
    'J':1,
    'T':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2
}
hands = {
    7:'Five of a kind',
    6:'Four of a kind',
    5:'Full house',
    4:'Three of a kind',
    3:'Two pair',
    2:'One pair',
    1:'High card'
}

handToBid = {}
handScores = []
for i in range(len(lines)):
    (hand,bid) = lines[i].split()
    handToBid[hand] = bid
    handCards = {card:0 for card in cards.keys()}
    jCount = 0
    for card in hand:
        if card != 'J':
            handCards[card] += 1
        else:
            jCount += 1
    handCards = [val for val in handCards.values()]
    handCards.sort()
    handCards[-1] += jCount
    if handCards[-1] == 5:
        score = 7
    elif handCards[-1] == 4:
        score = 6
    elif handCards[-1] == 3:
        if handCards[-2] == 2:
            score = 5
        else:
            score = 4
    elif handCards[-1] == 2:
        if handCards[-2] == 2:
            score = 3
        else:
            score = 2
    else:
        score = 1
    handVal = [cards.get(c) for c in hand]
    handScores.append((hand,score,handVal,bid))

sortedList = []
for score in hands.keys():
    unsortedList = [item for item in handScores if item[1] == score]
    unsortedList.sort(reverse=True,key = lambda x: x[2])
    for item in unsortedList:
        sortedList.append(item)
sortedList.reverse()
res = 0
for i in range(len(sortedList)):
    print('Hand:',sortedList[i][0], " - Thats a", hands.get(sortedList[i][1]))
    print()
    res += int(sortedList[i][3]) * (i+1)
print(res)
