input = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''

# with open('input') as f:
#     input = f.read()


records = [line.split(' ') for line in input.splitlines()]


def arrangements(springs, groups):
    if len(springs) == 0 or set(springs) == {'.'}:
        if len(groups) == 0:
            return 1
        else:
            return 0

    if len(groups) == 0:
        if '#' in set(springs):
            return 0
        else:
            return 1

    match springs[0]:
        case '.':
            res = arrangements(springs[1:], groups)
            return res
        case '?':
            res1 = arrangements('.' + springs[1:], groups)
            res2 = arrangements('#' + springs[1:], groups)
            return res1 + res2
        case '#':
            has_min_len = len(springs) >= groups[0] and '.' not in set(springs[:groups[0]])
            is_not_longer = len(springs) <= groups[0] or springs[groups[0]] != '#'

            if has_min_len and is_not_longer:
                res = arrangements(springs[groups[0] + 1:], groups[1:])
                return res
            else:
                return 0
        case _:
            assert False
    assert False


print(sum(
    [
        arrangements(springs, tuple(map(int, groups.split(','))))
        for springs, groups in records
    ]
))
