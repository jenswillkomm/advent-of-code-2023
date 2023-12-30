import re


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

boxes = [[] for i in range(265)]
for s in input:
    match = re.match('(\\w+)([=-])(\\d*)', s)
    label = match.group(1)
    operation = match.group(2)
    focalLength = match.group(3)
    boxNr = hash(label)
    match operation:
        case '-':
            i = [i for i, l in enumerate(boxes[boxNr]) if l.split(' ')[0] == label]
            assert len(i) < 2
            if len(i) > 0:
                del boxes[boxNr][i[0]]
        case '=':
            i = [i for i, l in enumerate(boxes[boxNr]) if l.split(' ')[0] == label]
            assert len(i) < 2
            if len(i) > 0:  # Does the label already exist?
                boxes[boxNr][i[0]] = ' '.join([boxes[boxNr][i[0]].split(' ')[0], focalLength])
            else:
                boxes[boxNr].append(' '.join([label, focalLength]))
        case _:
            assert False

sum = 0
for i, box in enumerate(boxes):
    for j, slot in enumerate(box):
        focalLength = int(slot.split(' ')[1])
        sum += (i + 1) * (j + 1) * focalLength


print(sum)
