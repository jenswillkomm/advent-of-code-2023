input = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''

# with open('input') as file:
#     input = file.read()


MAX_DISTANCE = 26501365


# (x,y) := map[y][x]
map = input.splitlines()
x_max = len(map[0])
y_max = len(map)

x = x_max // 2
y = y_max // 2
assert map[y][x] == 'S'


startPosition = (x, y)
queue = [(startPosition, 0)]
distances = {startPosition: 0}  # also functions as 'visited'
while len(queue) > 0:
    currPos, currDist = queue.pop(0)

    for step in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nextPos = (currPos[0] + step[0], currPos[1] + step[1])
        if nextPos[0] not in range(y_max) or nextPos[1] not in range(x_max):
            continue
        if map[nextPos[1]][nextPos[0]] == '#':
            continue
        if nextPos in distances:
            continue

        distances[nextPos] = currDist + 1
        queue.append((nextPos, currDist + 1))

# The following code assumes that each point on the square with Manhattan
# distance of x_max / 2 around the starting point can be reached with exactly
# x_max / 2 steps. This includes that there are no rocks horizontally and vertically
# from the starting position plus no rocks on this square around the starting point.
# This is true for the input file but not for the example input.
distances_even = [d for d in distances.values() if d % 2 == 0]
distances_odd = [d for d in distances.values() if d % 2 == 1]

distances_even_corners = [d for d in distances_even if d > x_max // 2]
distances_odd_corners = [d for d in distances_odd if d > x_max // 2]

nbMaps = (MAX_DISTANCE - (x_max // 2)) // x_max
assert nbMaps == 202300

nbGardenPlots = (nbMaps + 1) ** 2 * len(distances_odd) + nbMaps ** 2 * len(distances_even) - (nbMaps + 1) * len(distances_odd_corners) + nbMaps * len(distances_even_corners)


print(nbGardenPlots)
