import re


input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

# with open('input') as file:
#     input = file.read()


seeds = []
lines = input.split('\n')

for lineNr in range(len(lines)):
    match = re.match('seeds:((\\s\\d+)+)', lines[lineNr])
    if match:
        seeds = [int(s) for s in match.group(1).split(' ')[1:]]
        seedRanges = []
        for i in range(0, len(seeds), 2):
            seedRanges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
        seeds = seedRanges
        continue
    match = re.match('([a-z-]+) map:', lines[lineNr])
    if match:
        # print('=== Seed ranges: ' + str(seeds) + ' ===')
        # print('Mapping: ' + match.group(1))
        lineNr += 1
        newSeeds = []
        while lines[lineNr]:
            destinationRangeStart, sourceRangeStart, rangeLength = [int(s) for s in lines[lineNr].split(' ')]
            sourceRange = (sourceRangeStart, sourceRangeStart + rangeLength - 1)
            offset = destinationRangeStart - sourceRangeStart
            for seedRange in seeds.copy():
                if seedRange[0] >= sourceRange[0] and seedRange[1] <= sourceRange[1]:
                    seeds.remove(seedRange)
                    newSeeds.append((seedRange[0] + offset, seedRange[1] + offset))
                elif seedRange[0] >= sourceRange[0] and seedRange[1] > sourceRange[1] and seedRange[0] <= sourceRange[1]:
                    seeds.remove(seedRange)
                    seeds.append((sourceRange[1] + 1, seedRange[1]))
                    newSeeds.append((seedRange[0] + offset, sourceRange[1] + offset))
                elif seedRange[0] < sourceRange[0] and seedRange[1] >= sourceRange[0] and seedRange[1] <= sourceRange[1]:
                    seeds.remove(seedRange)
                    seeds.append((seedRange[0], sourceRange[0] - 1))
                    newSeeds.append((sourceRange[0] + offset, seedRange[1] + offset))
                elif seedRange[0] < sourceRange[0] and seedRange[1] > sourceRange[1]:
                    seeds.remove(seedRange)
                    seeds.append((seedRange[0], sourceRange[0] - 1))
                    seeds.append((sourceRange[1] + 1, seedRange[1]))
                    newSeeds.append((sourceRange[0] + offset, sourceRange[1] + offset))
            lineNr += 1
        newSeeds.extend(seeds)
        seeds = newSeeds
        # TODO: merge connected ranges into one


print(sorted(seeds)[0][0])
