import re


input = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''

input = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

# with open('input') as file:
#     input = file.read()


class Navigator:
    def __init__(self, directions):
        self.directions = directions
        self.pos = 0

    def next(self):
        element = self.directions[self.pos]
        self.pos = (self.pos + 1) % len(self.directions)
        return element

    def pos(self):
        return self.pos


input = input.splitlines()

nav = Navigator(input[0])
network = {}

for line in input[2:]:
    match = re.match('([A-Z0-9]{3}) = \\(([A-Z0-9]{3}), ([A-Z0-9]{3})\\)', line)
    network[match.group(1)] = (match.group(2), match.group(3))

currPos = 'AAA'
cntSteps = 0
while currPos != 'ZZZ':
    # print(currPos)
    nextPos = network[currPos]
    nextDir = nav.next()
    cntSteps += 1
    if nextDir == 'L':
        currPos = nextPos[0]
        continue
    if nextDir == 'R':
        currPos = nextPos[1]
        continue
    assert False


print(cntSteps)
