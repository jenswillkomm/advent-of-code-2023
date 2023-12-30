import re
from functools import reduce
from operator import mul


input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

# with open('input') as file:
#     input = file.read()


coordinates_symbols = set()
coordinates_partNumbers = set()
sum = 0
partNumbers = []


def is_near_symbol(lines, pos):
    return len(set([(x, y) for x in pos for y in lines]).intersection([c[0] for c in coordinates_symbols])) > 0


for lineNr, line in enumerate(input.split('\n')):
    for match in re.finditer('[^\\.\\d]', line):
        coordinates_symbols.add(((match.start(), lineNr), match.group(0)))
        # print('(%s, %s): %s' % (match.start(), lineNr, match.group(0)))

for lineNr, line in enumerate(input.split('\n')):
    for match in re.finditer('\\d+', line):
        coordinates_partNumbers.add(((range(match.start(), match.end()), lineNr), int(match.group(0))))
        # print('(%s, %s): %s' % (match.start(), lineNr, match.group(0)))
        if is_near_symbol(range(lineNr - 1, lineNr + 2), range(match.start() - 1, match.end() + 1)):
            sum += int(match.group(0))
            partNumbers.append(int(match.group(0)))

sum = 0
for gear in [s for s in coordinates_symbols if s[1] == '*']:
    gearRatioFactors = []
    for partNumbers in [p for p in coordinates_partNumbers if gear[0][1] - 1 <= p[0][1] <= gear[0][1] + 1]:
        if gear[0][0] in range(partNumbers[0][0].start - 1, partNumbers[0][0].stop + 1):
            gearRatioFactors.append(partNumbers)
    if len(gearRatioFactors) == 2:
        ratio = reduce(mul, map(lambda x: x[1], gearRatioFactors))
        sum += ratio


print(sum)
