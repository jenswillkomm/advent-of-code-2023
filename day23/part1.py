import sys
sys.setrecursionlimit(3 * sys.getrecursionlimit())


input = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''

# with open('input') as file:
#     input = file.read()


# (x, y) := map[y][x]
map = input.splitlines()

x_len = len(map[0])
y_len = len(map)

start = (map[0].find('.'), 0)
end = (map[y_len - 1].find('.'), y_len - 1)

slopes = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1)
}


paths = []
def DFS(v, visited, path):
    global paths

    visited.add(v)
    path.append(v)

    if v == end:
        paths.append(path)
        # print('Path found with length ' + str(len(path) - 1))
        # print(path)

    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    if map[v[1]][v[0]] in slopes:
        directions = {slopes[map[v[1]][v[0]]]}
    for dir in directions:
        w = (v[0] + dir[0], v[1] + dir[1])
        if w[0] not in range(0, x_len) or w[1] not in range(0, y_len):
            continue
        if map[w[1]][w[0]] == '#':
            continue
        if w in visited:
            continue

        DFS(w, visited.copy(), path.copy())


DFS(start, set(), [])


print(sorted([len(p) - 1 for p in paths], reverse=True)[0])
