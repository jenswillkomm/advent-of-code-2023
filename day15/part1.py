input = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

# with open('input') as file:
#     input = file.read()


def hash(str):
    value = 0
    for c in list(str):
        ascii = ord(c)
        value += ascii
        value *= 17
        value %= 256
    return value


input = input.replace('\n', '').split(',')


print(sum(map(hash, input)))
