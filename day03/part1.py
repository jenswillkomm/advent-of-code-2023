import re


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


print(sum)
