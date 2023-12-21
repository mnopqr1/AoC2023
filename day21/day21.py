from functools import cache
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

h,w = len(ls), len(ls[0])
grid = {(i,j) : ls[i][j] for (i,j) in product(range(h),range(w))}

neighbors = {(i,j) : [] for (i,j) in product(range(h),range(w))}
for (x,y) in product(range(h),range(w)):
    for (dx,dy) in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and grid[(nx,ny)] != "#":
            neighbors[(x,y)].append((nx,ny))

def startnode():
    for (i,j) in product(range(h),range(w)):
        if grid[(i,j)] == "S":
            return (i,j)

sx, sy = startnode()

reach = {s : dict() for s in range(0,7)}

def reachable(s, x, y):
    """what we can reach in 2^s steps from x,y"""
    if s == 0:
        return set(neighbors[(x,y)])
    if (x,y) in reach[s].keys():
        return reach[s][(x,y)]
    l = reachable(s-1,x,y)
    newl = set((xx,yy) for (nx,ny) in l for (xx,yy) in reachable(s-1,nx,ny))
    reach[s][(x,y)] = newl
    return newl

for i in range(7):
    print(len(reachable(i,sx,sy)))
