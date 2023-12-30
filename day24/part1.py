import re
from itertools import combinations


input = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''

# with open('input') as file:
#     input = file.read()


TESTAREA_MIN = 7
TESTAREA_MAX = 27
# TESTAREA_MIN = 200000000000000
# TESTAREA_MAX = 400000000000000


hailstones = []
for line in input.splitlines():
    match = re.match('(\\d+), (\\d+), (\\d+) @ +(-?\\d+), +(-?\\d+), +(-?\\d+)', line)
    # [(p_x, p_y, p_z), (v_x, v_y, v_z)]
    hailstones.append([(int(match.group(1)), int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)), int(match.group(6)))])

nbIntersections = 0
for h1, h2 in combinations(hailstones, 2):
    l1_p1 = h1[0]
    l1_p2 = (h1[0][0] + h1[1][0], h1[0][1] + h1[1][1], h1[0][2] + h1[1][2])
    l2_p1 = h2[0]
    l2_p2 = (h2[0][0] + h2[1][0], h2[0][1] + h2[1][1], h2[0][2] + h2[1][2])
    p_x_denominator = (l1_p1[0] - l1_p2[0]) * (l2_p1[1] - l2_p2[1]) - (l1_p1[1] - l1_p2[1]) * (l2_p1[0] - l2_p2[0])
    p_y_denominator = (l1_p1[0] - l1_p2[0]) * (l2_p1[1] - l2_p2[1]) - (l1_p1[1] - l1_p2[1]) * (l2_p1[0] - l2_p2[0])
    if p_x_denominator == 0 or p_y_denominator == 0:
        # print('Paths are parallel; they never intersect')
        continue

    p_x_numerator = (l1_p1[0] * l1_p2[1] - l1_p1[1] * l1_p2[0]) * (l2_p1[0] - l2_p2[0]) - (l1_p1[0] - l1_p2[0]) * (l2_p1[0] * l2_p2[1] - l2_p1[1] * l2_p2[0])
    p_y_numerator = (l1_p1[0] * l1_p2[1] - l1_p1[1] * l1_p2[0]) * (l2_p1[1] - l2_p2[1]) - (l1_p1[1] - l1_p2[1]) * (l2_p1[0] * l2_p2[1] - l2_p1[1] * l2_p2[0])
    p_x = p_x_numerator/p_x_denominator
    p_y = p_y_numerator / p_y_denominator
    p = (p_x, p_y)

    # assert abs((p[0] - h1[0][0]) / h1[1][0] - (p[1] - h1[0][1]) / h1[1][1]) < 0.0001
    # assert abs((p[0] - h2[0][0]) / h2[1][0] - (p[1] - h2[0][1]) / h2[1][1]) < 0.0001
    delta1 = (p[0] - h1[0][0]) / h1[1][0]
    delta2 = (p[0] - h2[0][0]) / h2[1][0]

    if delta1 < 0 or delta2 < 0:
        # print('Paths crossed in the past')
        continue

    if not (TESTAREA_MIN <= p[0] <= TESTAREA_MAX and TESTAREA_MIN <= p[1] <= TESTAREA_MAX):
        # print('Paths will cross outside the test area')
        continue

    nbIntersections += 1


print(nbIntersections)
