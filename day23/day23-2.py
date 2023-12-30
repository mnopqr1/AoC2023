from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

H, W = len(ls), len(ls[0])
grid = {(x,y) : ls[x][y] for (x,y) in product(range(H),range(W))}
neighbors = dict()

for (x,y) in product(range(H),range(W)):
    if grid[(x,y)] == "#":
        neighbors[(x,y)] = []
        continue

    neighbors[(x,y)] = []

    for (dx,dy) in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if grid[(nx,ny)] != "#":
                neighbors[(x,y)].append((nx,ny))

mem = {"best" : 0}

def longest(h):
    cur, _ = h[-1]
    poss = [n for n in cgrid[cur] if n not in [x[0] for x in h]]
    
    while len(poss) == 1:
        prev, cur = cur, poss[0]
        h.append((cur, cgrid[prev][cur]))
        poss = [n for n in cgrid[cur] if n not in [x[0] for x in h]]

    if len(poss) == 0:
        if cur == (ex,ey):
            # print("reached end!")
            score = sum(x[1] for x in h)
            # print(score)
            return score
        else:
            return 0

    bestr = 0

    for n in poss:
        histvar = h + [(n,cgrid[cur][n])]
        possr = longest(histvar)
        if possr > bestr:
            bestr = possr

    if bestr > mem["best"]:
        mem["best"] = bestr
        print(bestr)
    return bestr

sx = 0
sy = ls[0].find(".")
ex = H-1
ey = ls[H-1].find(".")

cgrid = dict()
queue = [(sx,sy)]
seen = {(sx,sy)}
while len(queue) > 0:
    branch = queue.pop(0)
    if branch in cgrid:
        continue
    cgrid[branch] = dict()
    for st in neighbors[branch]:
        ct = 1
        prev = branch
        cur = st
        while len(neighbors[cur]) == 2:
            a,b = neighbors[cur]
            assert a == prev or b == prev
            if b == prev:
                a,b = b,a
            prev, cur = cur, b
            ct += 1
        cgrid[branch][cur] = ct
        queue.append(cur)

answer = longest([((sx,sy),0)])
