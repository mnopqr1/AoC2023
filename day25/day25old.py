from math import inf
import random

filename = "test.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

NODES = []

for l in ls:
    cur, neighbors = l.split(": ")
    neighbors = neighbors.split(" ")
    NODES.append(cur)
    for n in neighbors:
        NODES.append(n)
NODES = list(set(NODES))
NODES.sort()

GRAPH = {n : [] for n in NODES}
for l in ls:
    cur, neighbors = l.split(": ")
    neighbors = neighbors.split(" ")
    GRAPH[cur] += neighbors
    for n in neighbors:
        GRAPH[n].append(cur)

CAPACITY = {u : {v : 1 if v in GRAPH[u] else 0 for v in NODES} for u in NODES}

def augment(graph, capacity, flow, val, u, target, visit):
    visit[u] = True
    if u == target:
        return val
    for v in graph[u]:
        cuv = capacity[u][v]
        if not visit[v] and cuv > flow[u][v]:
            res = min(val, cuv - flow[u][v])
            delta = augment(graph, capacity, flow, res, v, target, visit)
            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta
    return 0

def maxflow(graph, capacity, s, t):
    flow = {u : {v : 0 for v in NODES} for u in NODES}
    visit = {n : False for n in NODES}
    while augment(graph, capacity, flow, inf, s, t, visit) > 0:
        pass
    return flow, sum(flow[s].values())

# s,t  = NODES[0], NODES[-1]
s = "cmg"
t = "bvb"
f, _ = maxflow(GRAPH, CAPACITY, s, t)

print(f[s])

for n in NODES:
    print(n, end=": ")
    for u in f[n]:
        if f[n][u] == 1:
            print("->", u, end=" ")
        if f[n][u] == -1:
            print("<-", u, end=" ")
    print()

res = {u: [] for u in NODES}
for u in NODES:
    for v in GRAPH[u]:
        if f[u][v] == 0:
            res[u].append(v)
print(res[s])
reach = {s}
queue = [s]
while len(queue) > 0:
    cur = queue.pop(0)
    for u in res[cur]:
        if u not in reach:
            reach.add(u)
            queue.append(u)

print(reach)
# assert t not in reach

exit()
# def _augment(graph, capacity, flow, val, u, target, visit):
# visit[u] = True
# if u == target:
# return val
# for v in graph[u]:
# cuv = capacity[u][v]
# if not visit[v] and cuv > flow[u][v]: # reachable arc
# res = min(val, cuv - flow[u][v])
# delta = _augment(graph, capacity, flow, res, v, target, visit)
# if delta > 0:
# flow[u][v] += delta
# # augment flow
# flow[v][u] -= delta
# return delta
# return 0
# def ford_fulkerson(graph, capacity, s, t):
# add_reverse_arcs(graph, capacity)
# n = len(graph)
# flow = [[0] * n for _ in range(n)]
# INF = float(’inf’)
# while _augment(graph, capacity, flow, INF, s, t, [False] * n) > 0:
# pass
# # work already done in _augment
# return (flow, sum(flow[s]))
# # flow network, amount of flow
# exit()
def experiment():
    n1, n2 = "", ""
    nodes = NODES.copy()
    graph = {n : GRAPH[n].copy() for n in nodes}
    group = {n: [n] for n in nodes}
    while len(nodes) > 2:
        # print("--CURRENT GRAPH")
        # for n in nodes:
        #     if n == n1 or n == n2:
        #         print("->", end="")
        #     print(n, graph[n])

        n2 = random.choice(nodes)
        nodes.remove(n2)
        n1 = random.choice(nodes)
        group[n1] += group[n2]
        del group[n2]
        # print(f"--MERGING {n1} and {n2}")
        graph[n1] += graph[n2]
        graph[n1] = list(set(graph[n1]))
        for n in nodes:
            # print(n, graph[n])
            if n2 in graph[n]:
                graph[n].remove(n2)
                if n1 not in graph[n]: graph[n].append(n1)
        del graph[n2]
        # input()
    return group

def n_edges(A,B):
    c = 0
    for a in A:
        # print(a, GRAPH[a])
        for n in GRAPH[a]:
            
            if n in B:
                c += 1
    return c
k = 4
while k > 3:
    groups = experiment()
    k = n_edges(*list(groups.values()))
    print(list(groups.values()), k)

    # while len(nodes) > 2:
    #     n1 = random.choice(nodes)
    #     nodes.remove(n1)
    #     n2 = random.choice(nodes)
    #     nodes.remove(n2)
    #     newn = n1 + "," + n2
    #     nodes.append(newn)
    #     for s in graph.keys():
    #         if n1 in graph[s]:
    #             graph[s][graph[s].index(n1)] = newn
    #         if n2 in graph[s]:
    #             graph[s][graph[s].index(n2)] = newn
    #     graph[newn] =  graph[n1] + graph[n2]
    #     del graph[n1]
    #     del graph[n2]
    #     repl1 = [i for i in range(len(edges)) if edges[i][0] == n1 or edges[i][1] == n1]
    #     for i in repl1:
    #         x,y = edges[i]
    #         if x == n1:
    #             edges[i] = (newn, y)
    #         else:
    #             edges[i] = (x, newn)
        
    #     repl2 = [i for i in range(len(edges)) if edges[i][0] == n2 or edges[i][1] == n2]
    #     for i in repl2:
    #         x,y = edges[i]
    #         if x == n2:
    #             edges[i] = (newn, y)
    #         else:
    #             edges[i] = (x, newn)

        # print(f"Merging {n1} and {n2}")
        # for s in graph:
        #     print(s, graph[s])
        # input()
    
    # return list(graph.keys())

# def edges_between(a,b):
#     c = 0
#     for e in EDGES:
#         # print(e)
#         x,y = e
#         if (x in a and y in b) or (x in b and y in a):
#             c += 1
#     return c

# k = 4
# c = 1
# while k > 3:
#     print(c)
#     a, b = experiment()
#     # print(a)
#     # print(b)
#     k = edges_between(a,b)
#     c += 1


# def connected_comps(g):
#     nodes = set(g.keys())
#     comps = []
#     while len(nodes) >= 1:
#         s = nodes.pop()
#         reach = {s}
#         queue = [s]
#         while len(queue) > 0:
#             t = queue.pop(0)
#             for u in g[t]:
#                 if u not in reach:
#                     reach.add(u)
#                     queue.append(u)
#                     nodes.remove(u)
#         comps.append(reach)
#     return comps


# print(len(a)*len(b))
# answer = 0

# print(answer)