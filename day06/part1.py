import re
from functools import reduce
from operator import mul


input = '''Time:      7  15   30
Distance:  9  40  200
'''

# with open('input') as file:
#     input = file.read()


input = input.splitlines()
times = re.findall('\\d+', input[0])
times = map(int, times)
distances = re.findall('\\d+', input[1])
distances = map(int, distances)


print(
    reduce(mul,
        [
            sum([1 if ms * (t - ms) > d else 0 for ms in range(1, t - 1)])
            for t, d in zip(times, distances)
        ]
    )
)
