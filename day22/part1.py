import re


input = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''

# with open('input') as file:
#     input = file.read()


def move_down(bricks):
    bricks_final = []
    cubes_occupied = set()
    for brick in sorted(bricks, key=lambda x: x[1][2]):
        currCubes = set()
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                for z in range(brick[0][2], brick[1][2] + 1):
                    currCubes.add((x, y, z))
        assert len(currCubes & cubes_occupied) == 0

        while brick[0][2] > 1:
            brick = ((brick[0][0], brick[0][1], brick[0][2] - 1), (brick[1][0], brick[1][1], brick[1][2] - 1))

            nextCubes = set()
            for x in range(brick[0][0], brick[1][0] + 1):
                for y in range(brick[0][1], brick[1][1] + 1):
                    for z in range(brick[0][2], brick[1][2] + 1):
                        nextCubes.add((x, y, z))
            if len(nextCubes & cubes_occupied) == 0:
                currCubes = nextCubes
                continue
            else:
                brick = ((brick[0][0], brick[0][1], brick[0][2] + 1), (brick[1][0], brick[1][1], brick[1][2] + 1))
                break

        cubes_occupied |= currCubes
        bricks_final.append(brick)
    assert len(bricks_final) == len(bricks)
    return bricks_final


bricks = []
for line in input.splitlines():
    match = re.match('(\\d+),(\\d+),(\\d+)~(\\d+),(\\d+),(\\d+)', line)
    bricks.append(((int(match.group(1)), int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)), int(match.group(6)))))

bricks = move_down(bricks)

nbDisintegrated = 0
for brick_disintegrated in sorted(bricks, key=lambda x: x[1][2]):
    bricks_original = [b for b in bricks if b != brick_disintegrated]
    bricks_movedDown = move_down(bricks_original)
    if set(bricks_movedDown) == set(bricks_original):
        nbDisintegrated += 1


print(nbDisintegrated)
