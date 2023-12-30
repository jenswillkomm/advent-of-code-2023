input = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''

# with open('input') as file:
#     input = file.read()


rocks_solid = set()
rocks_round = set()

x_max = len(input.splitlines()[0])
y_max = len(input.splitlines())

for y, line in enumerate(input.splitlines()):
    for x, char in enumerate(list(line)):
        match char:
            case '#':
                rocks_solid.add((x, y))
            case 'O':
                rocks_round.add((x, y))

for rock in sorted(rocks_round.copy(), key=lambda x: x[1]):
    rocks_round.remove(rock)
    x, y = rock
    while y > 0 and (x, y - 1) not in rocks_solid.union(rocks_round):
        y -= 1
    rocks_round.add((x, y))

# print(rocks_round)
# print(sorted([y_max - rock[1] for rock in rocks_round]))


print(sum([y_max - rock[1] for rock in rocks_round]))
