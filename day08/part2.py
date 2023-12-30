import re
from math import lcm


input = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
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

currPos = [p for p in network.keys() if p[-1] == 'A']
cntSteps = 0
cycles = [-1] * len(currPos)
while len([p for p in currPos if p[-1] != 'Z']) > 0:
    # Check for cycles
    for i, p in enumerate(currPos):
        if p[-1] == 'Z' and cycles[i] < 0:
            cycles[i] = cntSteps
    if cycles.count(-1) < 1:
        break

    # print(currPos)
    nextDir = nav.next()
    cntSteps += 1
    if nextDir == 'L':
        currPos = [network[p][0] for p in currPos]
        continue
    if nextDir == 'R':
        currPos = [network[p][1] for p in currPos]
        continue
    assert False


print(lcm(*cycles))
