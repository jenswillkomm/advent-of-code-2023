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


# read-in as graph
V = {start}
E = set()

queue = [start]
while queue:
    v = queue.pop(0)

    for d in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        w = (v[0] + d[0], v[1] + d[1])
        if w[0] not in range(0, x_len) or w[1] not in range(0, y_len):
            continue
        if map[w[1]][w[0]] == '#':
            continue
        if (w, 1, v) not in E:
            E.add((v, 1, w))
        if w not in V:
            V.add(w)
            queue.append(w)


# reduce graph
for v in V.copy():
    edges = [e for e in E if e[0] == v or e[2] == v]
    if len(edges) == 2:
        vertices_connected = list({edges[0][0], edges[0][2], edges[1][0], edges[1][2]} - {v})
        assert len(vertices_connected) == 2
        E.remove(edges[0])
        E.remove(edges[1])
        V.remove(v)
        E.add((vertices_connected[0], edges[0][1] + edges[1][1], vertices_connected[1]))


# transform graph
paths_from = {}
for v in V:
    for e in [e for e in E if e[0] == v or e[2] == v]:
        if e[2] == v:
            e = (e[2], e[1], e[0])
        paths_from.setdefault(v, []).append((e[2], e[1]))


def DFS(v, dist, path):
    if v == end:
        return [(dist, path)]

    paths = []
    for w, d in paths_from[v]:
        if w in path:
            continue
        paths += DFS(w, dist + d, path + [v])
    return paths


print(max([p[0] for p in DFS(start, 0, [start])]))
