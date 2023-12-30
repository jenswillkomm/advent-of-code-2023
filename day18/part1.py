input = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
'''

# with open('input') as file:
#     input = file.read()


A = 0
border_len = 0

vertices = []
p_curr = (0, 0)
vertices.append(p_curr)
for line in input.splitlines():
    direction, steps, color = line.split(' ')
    steps = int(steps)
    border_len += steps
    p_prev = p_curr
    match direction:
        case 'U':
            p_curr = (p_curr[0], p_curr[1] - steps)
        case 'D':
            p_curr = (p_curr[0], p_curr[1] + steps)
        case 'R':
            p_curr = (p_curr[0] + steps, p_curr[1])
        case 'L':
            p_curr = (p_curr[0] - steps, p_curr[1])
        case _:
            assert False
    vertices.append(p_curr)

    A += p_prev[0] * p_curr[1] - p_curr[0] * p_prev[1]
assert vertices[0] == vertices[-1]


print(int(abs(A * 0.5) + border_len / 2 + 1))
