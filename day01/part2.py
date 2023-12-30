import re


input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

# with open('input') as file:
#     input = file.read()
input = input.split('\n')


DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def replace_digit(m):
    s = m.group(2)
    if s in DIGITS:
        return m.group(1) + DIGITS[s]
    else:
        return m.group(1) + m.group(2)


predicate = '|'.join(DIGITS.keys()) + '|\\d'
predicate_firstDig = "^(.*?)(" + predicate + ")"
predicate_lastDig = "^(.*)(" + predicate + ")"
input = [
    re.sub(predicate_lastDig, replace_digit,
           re.sub(predicate_firstDig, replace_digit, i))
    for i in input
]


print(
    sum(
        [
            int(
                str(re.search("^\\D*?(\\d)", i).group(1)) + str(re.search("(\\d)\\D*?$", i).group(1))
            )
            for i in input
            if re.search('\\d', i) is not None
        ]
    )
)
