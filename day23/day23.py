from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

H, W = len(ls), len(ls[0])
grid = {(x,y) : ls[x][y] for (x,y) in product(range(H),range(W))}
DIR = {">": (0,1), "^": (-1,0), "v": (1,0), "<" : (-1,0)}
neighbors = dict()
part1 = True

for (x,y) in product(range(H),range(W)):
    if part1:
        if grid[(x,y)] in ">^v<":
            nx,ny = DIR[grid[(x,y)]]
            neighbors[(x,y)] = [(x + nx, y + ny)]
            continue
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

def show(c,h):
    cx,cy = c
    for (x,y) in product(range(H),range(W)):
        if (x,y) in h:
            print("X", end="")
        elif (x,y) == (cx,cy):
            print("!", end="")
        else:
            print(grid[(x,y)], end="")
        if y == W-1:
            print()

mem = {}

def longest(h):
    cur = h[-1]
    poss = [n for n in neighbors[cur] if n not in h]

    while len(poss) == 1:
        cur = poss[0]
        h.append(cur)
        poss = [n for n in neighbors[cur] if n not in h]

    if len(poss) == 0:
        if cur == (ex,ey):
            return len(h)-1
        else:
            return 0

    bestr = 0

    for n in poss:
        histvar = h + [n]
        possr = longest(histvar)
        if possr > bestr:
            bestr = possr
    return bestr

def debug(cur,h,poss):
    print(f"{cur=}, {neighbors[cur]=}, {poss=}")
    show(cur,h)
    input()


sx = 0
sy = ls[0].find(".")
ex = H-1
ey = ls[H-1].find(".")

answer = longest([(sx,sy)])
if part1:
    assert answer == 2438
print(answer)