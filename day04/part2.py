import re
from functools import reduce
from operator import add


input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

# with open('input') as file:
#     input = file.read()


cards = {}
sum = 0

for line in input.split('\n')[:-1]:
    lineSplit = line.split(':')
    cardNr = int(re.match('Card\\s+(\\d+)', lineSplit[0]).group(1))
    numberSplit = lineSplit[1].split(' |')
    winningNumbers = [numberSplit[0][i:i + 3] for i in range(0, len(numberSplit[0]), 3)]
    cardNumbers = [numberSplit[1][i:i + 3] for i in range(0, len(numberSplit[1]), 3)]
    myWinningNumbers = len(set(winningNumbers).intersection(set(cardNumbers)))
    if myWinningNumbers > 0:
        sum += 2 ** (myWinningNumbers - 1)
    cards[cardNr] = myWinningNumbers


cache = {}  # TODO: use functools.cache annotation instead
def card_copies(cardnr):
    if cardnr in cache:
        return cache[cardnr]

    copies = 1
    for i in range(cards[cardnr]):
        copies += card_copies(cardnr + i + 1)
    cache[cardnr] = copies
    return copies


print(
    reduce(add,
           [
               card_copies(i + 1) for i
               in range(len(cards))
           ]
    )
)
