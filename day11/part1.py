import itertools


input = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''

# with open('input') as file:
#     input = file.read()


def dist(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


coordinates = [(x, y) for y, line in enumerate(input.splitlines()) for x, char in enumerate(line) if char == '#']

maxCoords = (max(coordinates, key=lambda x: x[0])[0], max(coordinates, key=lambda x: x[1])[1])
x_expanded = [x for x in range(maxCoords[0]) if x not in [x for x, y in coordinates]]
y_expanded = [y for y in range(maxCoords[1]) if y not in [y for x, y in coordinates]]

coordinates_expanded = []
for galaxy in coordinates:
    newX = galaxy[0] + (len([x for x in x_expanded if x < galaxy[0]]))
    newY = galaxy[1] + (len([y for y in y_expanded if y < galaxy[1]]))
    coordinates_expanded.append((newX, newY))

sum = 0
for galaxyPair in itertools.combinations(coordinates_expanded, 2):
    sum += dist(galaxyPair[0], galaxyPair[1])


print(sum)
