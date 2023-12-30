import re


input = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''

# with open('input') as file:
#     input = file.read()


input_workflows, input_parts = input.split('\n\n')
workflows = {}
accepted_parts = []

for workflow in input_workflows.splitlines():
    match = re.match('([a-z]+){(.+)}', workflow)
    name = match.group(1)
    instructions = match.group(2)
    workflows[name] = instructions


for part_str in input_parts.splitlines():
    match = re.match('{(.+)}', part_str)
    attributes = match.group(1).split(',')
    part = {}
    for attribute in attributes:
        symbol, value = attribute.split('=')
        part[symbol] = int(value)

    # execute workflow
    next_wf = 'in'
    while next_wf not in {'A', 'R'}:
        instructions = workflows[next_wf].split(',')
        for instruction in instructions:
            if re.fullmatch('[a-z]+|A|R', instruction):
                next_wf = instruction
                break
            match = re.match('([xmas])([<>])(\\d+):(\\w+)', instruction)
            operand = part[match.group(1)]
            expression = False
            match match.group(2):
                case '<':
                    expression = operand < int(match.group(3))
                case '>':
                    expression = operand > int(match.group(3))
            if expression:
                next_wf = match.group(4)
                break
            else:
                # next instruction
                continue
    if next_wf == 'A':
        accepted_parts.append(part)


print(sum([sum(p.values()) for p in accepted_parts]))
