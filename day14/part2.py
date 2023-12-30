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


NB_ITERATIONS = 1000000000


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

results_log = [rocks_round.copy()]
for cycle in range(1, NB_ITERATIONS + 1):
    # roll to north
    for rock in sorted(rocks_round.copy(), key=lambda x: x[1]):
        rocks_round.remove(rock)
        x, y = rock
        while y > 0 and (x, y - 1) not in rocks_solid and (x, y - 1) not in rocks_round:
            y -= 1
        rocks_round.add((x, y))

    # roll to west
    for rock in sorted(rocks_round.copy(), key=lambda x: x[0]):
        rocks_round.remove(rock)
        x, y = rock
        while x > 0 and (x - 1, y) not in rocks_solid and (x - 1, y) not in rocks_round:
            x -= 1
        rocks_round.add((x, y))

    # roll to south
    for rock in sorted(rocks_round.copy(), key=lambda x: x[1], reverse=True):
        rocks_round.remove(rock)
        x, y = rock
        while y < y_max - 1 and (x, y + 1) not in rocks_solid and (x, y + 1) not in rocks_round:
            y += 1
        rocks_round.add((x, y))

    # roll to east
    for rock in sorted(rocks_round.copy(), key=lambda x: x[0], reverse=True):
        rocks_round.remove(rock)
        x, y = rock
        while x < x_max - 1 and (x + 1, y) not in rocks_solid and (x + 1, y) not in rocks_round:
            x += 1
        rocks_round.add((x, y))

    # check for cycles
    if rocks_round in results_log:
        cycle_start = results_log.index(rocks_round)
        cycle_end = cycle
        cycle_len = cycle_end - cycle_start

        remaining_cycles = ((NB_ITERATIONS - cycle_start) % cycle_len) + cycle_start
        rocks_round = results_log[remaining_cycles]
        break

    results_log.append(rocks_round.copy())

# print(rocks_round)
# print(sorted([y_max - rock[1] for rock in rocks_round]))


print(sum([y_max - rock[1] for rock in rocks_round]))
