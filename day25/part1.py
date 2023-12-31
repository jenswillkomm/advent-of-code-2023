import re
import random


input = '''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''

# with open('input') as file:
#     input = file.read()


vertexNames = sorted(list(set(
    [
        s for s
        in input.replace(':', '').replace(' ', '\n').splitlines()
    ]
)))

adjacencyList = set()
for line in input.splitlines():
    m = re.search('(\\w+): ([\\w ]+)', line)
    u = vertexNames.index(m[1])
    for e in m[2].split(' '):
        v = vertexNames.index(e)
        if u <= v:
            adjacencyList.add((u, v))
        else:
            adjacencyList.add((v, u))

adjacencyList = list(adjacencyList)
assert set(range(len(vertexNames))) == set([v for e in adjacencyList for v in e])

contractionsLog = [1] * len(vertexNames)


def kargers(V, E):
    global contractionsLog
    while len(V) > 2:
        nextE = []
        e = random.randrange(len(E))
        u, v = E[e]
        del E[e]  # remove edge between u and v
        for (s, t) in E:  # TODO: manipulate the elements directly instead of copying them to a new list
            if s == u and t == v or s == v and t == u:
                # do not copy edges between u and v
                continue
            if s == u and t == u or s == v and t == v:
                # do not copy self-loops
                continue
            if s == v:
                nextE.append((u, t))
                continue
            if t == v:
                nextE.append((s, u))
                continue
            nextE.append((s, t))
        E = nextE
        V.remove(vertexNames[v])
        contractionsLog[u] += contractionsLog[v]
        contractionsLog[v] = 0

        assert set(V) == set([vertexNames[v] for e in E for v in e])
    return V, E


while True:
    contractionsLog = [1] * len(vertexNames)
    V_mincut, E_mincut = kargers(vertexNames.copy(), adjacencyList.copy())

    if len(E_mincut) == 3:
        break
assert len(V_mincut) == 2


print(contractionsLog[vertexNames.index(V_mincut[0])] * contractionsLog[vertexNames.index(V_mincut[1])])
