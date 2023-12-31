import math
import numpy as np


input = '''.....
.S-7.
.|.|.
.L-J.
.....
'''

input = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''

# with open('input') as file:
#    input = file.read()


CONNECTION_TO_NORTH = {'|', 'L', 'J', 'S'}
CONNECTION_TO_EAST = {'-', 'L', 'F', 'S'}
CONNECTION_TO_SOUTH = {'|', '7', 'F', 'S'}
CONNECTION_TO_WEST = {'-', 'J', '7', 'S'}


input = input.splitlines()
V = []
v_start = -1

for y in range(0, len(input)):
    for x in range(0, len(input[y])):
        if input[y][x] != '.':
            V.append((x, y))
        if input[y][x] == 'S':
            v_start = V.index((x, y))

E = np.zeros((len(V), len(V)))

for y in range(0, len(input)):
    for x in range(0, len(input[y])):
        # add edge to north
        if y > 0 and input[y][x] in CONNECTION_TO_NORTH and input[y - 1][x] in CONNECTION_TO_SOUTH:
            start = V.index((x, y))
            end = V.index((x, y-1))
            E[start, end] = 1

        # add edge to east
        if x < len(input[y]) - 1 and input[y][x] in CONNECTION_TO_EAST and input[y][x + 1] in CONNECTION_TO_WEST:
            start = V.index((x, y))
            end = V.index((x+1, y))
            E[start, end] = 1

        # add edge to south
        if y < len(input) - 1 and input[y][x] in CONNECTION_TO_SOUTH and input[y + 1][x] in CONNECTION_TO_NORTH:
            start = V.index((x, y))
            end = V.index((x, y+1))
            E[start, end] = 1

        # add edge to west
        if x > 0 and input[y][x] in CONNECTION_TO_WEST and input[y][x - 1] in CONNECTION_TO_EAST:
            start = V.index((x, y))
            end = V.index((x-1, y))
            E[start, end] = 1

# print(V)
# print(E)

queue = [(v_start, 0)]
visited = {v_start}
distances = [math.inf] * len(V)
distances[v_start] = 0
while queue:
    queue.sort(key=lambda x: x[1])
    v, d = queue.pop(0)
    for w in range(len(E[v])):
        if E[v, w] == 1 and w not in visited:
            visited.add(w)
            queue.append((w, d + 1))
            distances[w] = d + 1


print(max([d for d in distances if d != math.inf]))
