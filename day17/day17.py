import heapq
from math import inf
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]
h,w = len(ls), len(ls[0])
grid = {(x,y) : int(ls[x][y]) for (x,y) in product(range(h),range(w))}

DIRS = {0: (-1,0), 1: (0,1), 2: (1,0), 3: (0,-1)}
Q = [(0,0,0,0,0)]
cost = {}
while Q:
    curcost, x, y, diri, t = heapq.heappop(Q)
    if (x, y, diri, t) in cost:
        continue
    cost[(x, y, diri, t)] = curcost
    for i in range(4):
        dx,dy = DIRS[i]
        nt = 1 if i != diri else t+1
        nx = x + dx
        ny = y + dy
        if 0 <= nx < h and 0 <= ny < w and nt <= 3 and ((i+2)%4 != diri):
            edge = grid[(nx,ny)]
            heapq.heappush(Q, (curcost+edge, nx, ny, i, nt))
 
tx,ty = h-1,w-1

answer = inf
for (x,y,diri,t) in cost.keys():
    if x == tx and y == ty:
        answer = min(cost[(x,y,diri,t)], answer)
print(answer)