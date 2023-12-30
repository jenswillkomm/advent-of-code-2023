import numpy as np


input = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''

# with open('input') as file:
#     input = file.read()


def find_reflection(puzzle):
    return find_row_reflection(puzzle), find_col_reflection(puzzle)


def find_row_reflection(puzzle):
    for row in range(puzzle.shape[0] - 1):
        # print('%s-th line pairs: %s' % (str(row), str([(i, j) for i, j in zip(range(row, -1, -1), range(row + 1, puzzle.shape[0]))])))
        if np.all([np.all(puzzle[i, :] == puzzle[j, :]) for i, j in zip(range(row, -1, -1), range(row + 1, puzzle.shape[0]))]):
            return row + 1
    return -1


def find_col_reflection(puzzle):
    for col in range(puzzle.shape[1] - 1):
        if np.all([np.all(puzzle[:, i] == puzzle[:, j]) for i, j in zip(range(col, -1, -1), range(col + 1, puzzle.shape[1]))]):
            return col + 1
    return -1


puzzles = input.split('\n\n')

sum = 0
for puzzle in puzzles:
    p = np.array([list(line) for line in puzzle.splitlines()])
    mirrorPos = find_col_reflection(p)
    if mirrorPos > 0:
        sum += mirrorPos
        continue

    mirrorPos = find_row_reflection(p)
    if mirrorPos > 0:
        sum += mirrorPos * 100
        continue

    assert False


print(sum)
