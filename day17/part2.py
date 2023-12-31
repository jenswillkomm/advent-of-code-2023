import heapq


input = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''

input = '''111111111111
999999999991
999999999991
999999999991
999999999991
'''

# with open('input') as f:
#     input = f.read()


map = [list(map(int, list(s))) for s in input.splitlines()]
m_max = len(map)
n_max = len(map[0])

DIRECTIONS = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

REVERSE_DIRECTIONS = {
    'U': 'D',
    'R': 'L',
    'D': 'U',
    'L': 'R'
}

pos_start = (0, 0)
pos_end = (m_max - 1, n_max - 1)


def bfs():
    queue = [(0, pos_start, '')]
    heapq.heapify(queue)
    visited = {(pos_start, '')}

    while len(queue) > 0:
        heat_loss, pos, history_dirs = heapq.heappop(queue)

        if len(history_dirs) >= 4 and pos == pos_end:
            return heat_loss

        # set direction restrictions
        reverse_direction = set(REVERSE_DIRECTIONS[history_dirs[-1]]) if len(history_dirs) > 0 else set()
        min_straight_line = DIRECTIONS.keys() - set(history_dirs[-1]) if 0 < len(history_dirs) < 4 else set()
        max_straight_line = set(history_dirs[-1]) if len(history_dirs) >= 10 else set()

        for dir in DIRECTIONS.keys() - reverse_direction - min_straight_line - max_straight_line:
            pos_next = (pos[0] + DIRECTIONS[dir][0], pos[1] + DIRECTIONS[dir][1])
            if not (0 <= pos_next[0] < m_max and 0 <= pos_next[1] < n_max):
                continue

            history_dirs_next = dir
            if len(history_dirs) > 0 and dir == history_dirs[-1]:
                history_dirs_next = history_dirs + dir

            if (pos_next, history_dirs_next) in visited:
                continue

            visited.add((pos_next, history_dirs_next))
            heapq.heappush(queue, (heat_loss + map[pos_next[0]][pos_next[1]], pos_next, history_dirs_next))
    assert False
    return -1


print(bfs())
