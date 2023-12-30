import re


input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

# with open('input') as file:
#     input = file.read()
input = input.split('\n')


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
