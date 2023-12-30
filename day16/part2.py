from enum import Enum


input = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
'''

# with open('input') as file:
#     input = file.read()


class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


x_max = len(input.splitlines()[0])
y_max = len(input.splitlines())

contraption = {}
for y, line in enumerate(input.splitlines()):
    for x, char in enumerate(line):
        if char != '.':
            contraption[(x, y)] = char

startPoints = set()
for x in range(x_max):
    startPoints.add((x, -1, Direction.DOWN))
    startPoints.add((x, y_max, Direction.UP))
for y in range(y_max):
    startPoints.add((-1, y, Direction.RIGHT))
    startPoints.add((x_max, y, Direction.LEFT))


bsf_energized = 0
bsf_startPoint = -1
for startPoint in startPoints:
    energized = set()
    lightBeam = [startPoint]
    while len(lightBeam) > 0:
        pos_x, pos_y, direction = lightBeam.pop(0)
        while True:
            if (pos_x, pos_y, direction) in energized:
                break
            energized.add((pos_x, pos_y, direction))
            match direction:
                case Direction.UP:
                    pos_y -= 1
                    if pos_y < 0:
                        break
                    if (pos_x, pos_y) not in contraption:
                        continue
                    match contraption[(pos_x, pos_y)]:
                        case '/':
                            direction = Direction.RIGHT
                        case '\\':
                            direction = Direction.LEFT
                        case '-':
                            direction = Direction.LEFT
                            lightBeam.append((pos_x, pos_y, direction.RIGHT))
                case Direction.DOWN:
                    pos_y += 1
                    if pos_y > y_max - 1:
                        break
                    if (pos_x, pos_y) not in contraption:
                        continue
                    match contraption[(pos_x, pos_y)]:
                        case '/':
                            direction = Direction.LEFT
                        case '\\':
                            direction = Direction.RIGHT
                        case '-':
                            direction = Direction.LEFT
                            lightBeam.append((pos_x, pos_y, direction.RIGHT))
                case Direction.LEFT:
                    pos_x -= 1
                    if pos_x < 0:
                        break
                    if (pos_x, pos_y) not in contraption:
                        continue
                    match contraption[(pos_x, pos_y)]:
                        case '/':
                            direction = Direction.DOWN
                        case '\\':
                            direction = Direction.UP
                        case '|':
                            direction = Direction.UP
                            lightBeam.append((pos_x, pos_y, direction.DOWN))
                case Direction.RIGHT:
                    pos_x += 1
                    if pos_x > x_max - 1:
                        break
                    if (pos_x, pos_y) not in contraption:
                        continue
                    match contraption[(pos_x, pos_y)]:
                        case '/':
                            direction = Direction.UP
                        case '\\':
                            direction = Direction.DOWN
                        case '|':
                            direction = Direction.UP
                            lightBeam.append((pos_x, pos_y, direction.DOWN))
                case _:
                    assert False

    fields_energized = len(set([(x, y) for x, y, _ in energized])) - 1
    if fields_energized > bsf_energized:
        bsf_energized = fields_energized
        bsf_startPoint = startPoint
assert bsf_startPoint != -1


print(bsf_energized)
