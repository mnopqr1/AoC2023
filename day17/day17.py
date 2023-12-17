import heapq
from math import inf
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]
h,w = len(ls), len(ls[0])
grid = {(x,y) : int(ls[x][y]) for (x,y) in product(range(h),range(w))}

DIRS = {0: (-1,0), 1: (0,1), 2: (1,0), 3: (0,-1)}
cost = {}

part2 = True
UPPERLIM = 10 if part2 else 3
DELAY = 4 if part2 else 1
Q = [(0,0,0,0,0),(0,0,0,1,0)]

while Q:
    curcost, x, y, diri, t = heapq.heappop(Q)
    if (x, y, diri, t) in cost:
        continue
    cost[(x, y, diri, t)] = curcost
    for ndiri in range(4):
        if t < DELAY and ndiri != diri:
            continue
        if (ndiri+2)%4 == diri:
            continue
        dx,dy = DIRS[ndiri]
        if not (0 <= x + DELAY * dx < h and 0 <= y + DELAY * dy < w): continue
        nt = 0 if ndiri != diri else t
        nx, ny  = x, y
        ncost = curcost
        for _ in range(DELAY):
            nt += 1
            nx += dx
            ny += dy
            if not nt <= UPPERLIM:
                break
            ncost += grid[(nx,ny)]
            heapq.heappush(Q, (ncost, nx, ny, ndiri, nt))

tx, ty = h-1, w-1

answer = inf
for (x,y,diri,t) in cost.keys():
    if x == tx and y == ty:
        answer = min(cost[(x,y,diri,t)], answer)
print(answer)