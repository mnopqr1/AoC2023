filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

nodes = []
for l in ls:
    cur, neighbors = l.split(": ")
    neighbors = neighbors.split(" ")
    nodes.append(cur)
    for n in neighbors:
        nodes.append(n)

assert all(len(name) == 3 for name in nodes)

nodes = list(set(nodes))
N = len(nodes)
w = {u : {v: 0 for v in nodes} for u in nodes}

for l in ls:
    cur, neighbors = l.split(": ")
    neighbors = neighbors.split(" ")
    for n in neighbors:
        w[cur][n] = 1
        w[n][cur] = 1

# implementation of Stoer & Wagner https://dl.acm.org/doi/10.1145/263867.263872
phasescores = []
phases = []

while len(nodes) > 1:
    # one phase:
    # find the next pair to be merged
    a = nodes[0]
    A = [a]
    B = [v for v in nodes if v != a]
    node = a
    strength = {u : 0 for u in nodes}

    # add nodes to A one by one, see what's added last
    while len(A) < len(nodes):
        best = 0
        newnode = None
        for u in B:
            strength[u] += w[node][u]
            if strength[u] > best:
                best = strength[u]
                newnode = u
        node = newnode
        A.append(node)
        B.remove(node)
        prev = best

    # record the score and result of this phase
    phasescores.append(prev)
    phases.append(A[-1])

    # if we have found a phase of size 3, we can break
    if prev == 3: break

    # merge the last two nodes that were added to A
    s, t = A[-1], A[-2]
    new = s + t
    nodes.remove(s)
    nodes.remove(t)
    nodes.append(new)
    w[new] = {u : w[s][u] + w[t][u] for u in nodes if u != new}
    w[new][new] = 0
    for u in nodes:
        if u != new:
            del w[u][s]
            del w[u][t]
        w[u][new] = w[new][u]
    del w[s]
    del w[t]

# find the minimal phase
# mincutscore = N + 1
# mincut = []
# for p, s in enumerate(phasescores):
#     if s < mincutscore:
#         mincutscore = s
#         mincut = phases[p]
# k = len(mincut)//3
# print(k * (N-k))

# we know the last phase was minimal (because of the break at size 3)
assert prev == 3
mincut = phases[-1]
k = len(mincut) // 3
answer = k * (N-k)
assert answer == 591890
