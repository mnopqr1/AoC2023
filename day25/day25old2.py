
def showweights():
    for u in nodes:
        print(u, end=": ")
        for v in nodes:
            if w[u][v] > 0:
                print(f"{v}[{w[u][v]}]", end=" ")
        print()

def showstrength():
    print(node)
    for v in nodes:
        if strength[v] > 0:
            print(f"{v}:{strength[v]}", end=" ")
    print()

def crossweight(w,A,u):
    return sum(w[a][u] for a in A)

def tightest(nodes,w,A):
    best, node = -1, None
    for u in nodes:
        if u in A: continue
        score = crossweight(w,A,u)
        if best > score:
            best = score
            node = u
    assert node is not None
    return best, node

def merge(w,nodes,u,v):
    assert u in nodes and v in nodes
    i, j = nodes.index(u), nodes.index(v)
    nodes[i] = u+v
    w[u+v] = {z: w[u] + w[v] for z in nodes}
    del w[u]
    del w[v]
    del nodes[j]

# a = NODES[0]

# def mincutphase():
#     A = [a]
#     cur = a
#     cutofphase = -1
#     nodes = NODES.copy()
#     n = len(nodes)
#     w = {u : {v: W[u][v] for v in nodes} for u in nodes}
#     while len(A) < len(NODES):
#         prev = cur
#         s, cur = tightest(A)
#         if len(A) == len(NODES) - 1:
#             cutofphase = s
#     u, v = prev, cur
#     i, j = nodes.index(u), nodes.index(v)
#     nodes[i] = u+v
#     w[u+v] = {z: w[u] + w[v] for z in nodes}
#     del w[u]
#     del w[v]
#     del nodes[j]
#     return cutofphase

# mincut = inf
# while len(NODES) > 1:
#     score = mincutphase()
#     if score < mincut:
#         mincut = score


# NODES += ["START", "END"]
# GRAPH["START"] = NODES[:-2]
# GRAPH["END"] = []
# for n in NODES[:-2]:
#     GRAPH[n].append("END")

# CAPACITY = {u : {v : 1 if v in GRAPH[u] else 0 for v in NODES} for u in NODES}

# def isflow(f):
#     for u in NODES:
#         inf = 0
#         outf = 0
#         for v in NODES:
#             if f[u][v] > CAPACITY[u][v]: return False
#             outf += f[u][v]
#             inf += f[v][u]
#         if u != "START" and u != "END" and outf != inf: 
#             print(u, outf, inf)
#             return False
#     return True

# def iscut(A,B):
#     return "START" in A and "END" in B and \
#     len(A.intersection(B)) == 0 and len(A.union(B)) == len(NODES)

# def crossflow(f,A,B):
#     res = 0
#     for u in A:
#         for v in B:
#             res += f[u][v]
#     return res

# a: b c
# b: c d
# c: d

        
# a - b,c
# b - c,d
# c - d

exf = {u : {v : 0 for v in NODES} for u in NODES}
exf["START"]["a"] = 1
exf["a"]["START"] = -1
exf["a"]["b"] = 1
exf["b"]["a"] = -1
exf["b"]["d"] = 1
exf["d"]["b"] = -1
exf["d"]["END"] = 1
exf["END"]["d"] = -1
exf["b"]["c"] = 1
exf["c"]["b"] = -1
exf["START"]["b"] = 1
exf["b"]["START"] = -1
exA = {"START","a","b","c"}
exB = {"d", "END"}
assert iscut(exA,exB)
assert isflow(exf)
print(crossflow(exf,exA,exB))