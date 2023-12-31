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


MAX_DISTANCE = 6
# MAX_DISTANCE = 64


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

    if currDist == MAX_DISTANCE:
        continue

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


print(len(
    [
        p for p, d
        in distances.items() if d % 2 == 0
    ]
))
