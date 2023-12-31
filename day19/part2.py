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


def adjust_ranges_workflow(accept_ranges, wf_name):
    if wf_name == 'A':
        return len(accept_ranges['x']) * len(accept_ranges['m']) * len(accept_ranges['a']) * len(accept_ranges['s'])
    if wf_name == 'R':
        return 0

    return adjust_ranges_instruction(accept_ranges, workflows[wf_name])


def adjust_ranges_instruction(accept_ranges, instruction_name):
    if re.fullmatch('[a-z]+|A|R', instruction_name):
        return adjust_ranges_workflow(accept_ranges, instruction_name)

    # prune
    if any([len(e) == 0 for e in accept_ranges.values()]):
        return 0

    match = re.match('([xmas])([<>])(\\d+):(\\w+)', instruction_name[:instruction_name.find(',')])
    categories = match.group(1)

    affected_ranges = {}
    for i in 'xmas'.replace(categories, ''):
        affected_ranges[i] = accept_ranges[i].copy()
    match match.group(2):
        case '<':
            affected_ranges[categories] = set([e for e in accept_ranges[categories] if e < int(match.group(3))])
            accept_ranges[categories] = set([e for e in accept_ranges[categories] if not e < int(match.group(3))])
        case '>':
            affected_ranges[categories] = set([e for e in accept_ranges[categories] if e > int(match.group(3))])
            accept_ranges[categories] = set([e for e in accept_ranges[categories] if not e > int(match.group(3))])

    combinations_affectedRanges = adjust_ranges_workflow(affected_ranges, match.group(4))
    combinations_acceptRanges = adjust_ranges_instruction(accept_ranges, instruction_name[instruction_name.find(',') + 1:])
    return combinations_affectedRanges + combinations_acceptRanges


accept_ranges = {}
for i in 'xmas':
    accept_ranges[i] = set(range(1, 4000 + 1))

accepted_combinations = adjust_ranges_workflow(accept_ranges, 'in')


print(accepted_combinations)
