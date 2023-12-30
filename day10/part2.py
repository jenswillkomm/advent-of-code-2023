import numpy as np


input = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
'''

input = '''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''

input = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
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

# reduce the number of vertices and sort by path
A = 0  # area
vertices_on_path = []
pathLen = 0
delta_prev = (0, 0)
v_curr = v_start
v_prev = v_start
while v_curr != v_start or len(vertices_on_path) < 1:
    v_next = -1
    for w in range(len(E[v_curr])):
        if E[v_curr, w] == 1 and w != v_prev:
            v_next = w
            break
    assert v_next != -1
    pathLen += 1

    delta = (V[v_next][0] - V[v_curr][0], V[v_next][1] - V[v_curr][1])
    if delta != delta_prev:
        vertices_on_path.append(V[v_curr])
        if len(vertices_on_path) > 1:
            p_curr = vertices_on_path[-1]
            p_prev = vertices_on_path[-2]
            A += p_prev[0] * p_curr[1] - p_curr[0] * p_prev[1]
    delta_prev = delta

    v_prev = v_curr
    v_curr = v_next
vertices_on_path.append(V[v_start])
p_curr = vertices_on_path[-1]
p_prev = vertices_on_path[-2]
A += p_prev[0] * p_curr[1] - p_curr[0] * p_prev[1]

# print(vertices_on_path)
# print(pathLen)


print(int(abs(A * 0.5) - pathLen / 2 + 1))
