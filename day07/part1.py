from functools import cmp_to_key
from enum import Enum


input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

# with open('input') as file:
#     input = file.read()


CARD_VALUE = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


class CardType(Enum):
    FIVEOFAKIND = 7
    FOUROFAKIND = 6
    FULLHOUSE = 5
    THREEOFAKIND = 4
    TWOPAIR = 3
    ONEPAIR = 2
    HIGHCARD = 1


def cmp(lhs, rhs):
    # type
    ltype = card_type(lhs)
    rtype = card_type(rhs)
    if ltype != rtype:
        return ltype.value - rtype.value

    # value
    for l, r in zip(lhs, rhs):
        lval = CARD_VALUE[l]
        rval = CARD_VALUE[r]
        if lval == rval:
            continue
        return lval - rval


def card_type(cards):
    if len(set(cards)) == 1:
        return CardType.FIVEOFAKIND
    for c in set(cards):
        if cards.count(c) == 4:
            return CardType.FOUROFAKIND
    if len(set(cards)) == 2:
        return CardType.FULLHOUSE
    for c in set(cards):
        if cards.count(c) == 3:
            return CardType.THREEOFAKIND
    if len(set(cards)) == 3:
        pairs = 0
        for c in set(cards):
            if cards.count(c) == 2:
                pairs += 1
        if pairs == 2:
            return CardType.TWOPAIR
    for c in set(cards):
        if cards.count(c) == 2:
            return CardType.ONEPAIR
    return CardType.HIGHCARD

# for i, v in enumerate(sorted([l.split(' ') for l in input.splitlines()], key=cmp_to_key(lambda l, r: cmp(l[0], r[0]))), start=1):
#     print('%i: %s' % (i, v))


print(
    sum(
        [
            int(v[1]) * i for i, v
            in enumerate(sorted([line.split(' ') for line in input.splitlines()], key=cmp_to_key(lambda l, r: cmp(l[0], r[0]))), start=1)
        ]
    )
)
