from functools import cache
from itertools import product
import os

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

reach_pow = {s : dict() for s in range(0,7)}

def reachable_pow(s, x, y):
    """what we can reach in 2^s steps from x,y"""
    if s == 0:
        return set(neighbors[(x,y)])
    if (x,y) in reach_pow[s].keys():
        return reach_pow[s][(x,y)]
    l = reachable_pow(s-1,x,y)
    newl = set((xx,yy) for (nx,ny) in l for (xx,yy) in reachable_pow(s-1,nx,ny))
    reach_pow[s][(x,y)] = newl
    return newl

reach = dict()

def reachable(s,x,y):
    """what we can reach in s steps from (x,y)"""
    if s == 0:
        return {(x,y)}
    if (s,x,y) in reach.keys():
        return reach[(s,x,y)]
    ps = reachable(s-1,x,y)
    newps = set((xx,yy) for (nx,ny) in ps for (xx,yy) in neighbors[(nx,ny)])
    reach[(s,x,y)] = newps
    return newps

def show(g, ps):
    for (x,y) in product(range(h),range(w)):
        if (x,y) in ps:
            print(" O ", end="")
        else:
            print(f" {g[(x,y)]} ",end="")
        if y == w-1: print()

# exit()
# print(w)
M = 201
assert M%2 == 1
reached = dict()
for i in range(M):
    # os.system("clear")
    # print(f"step {i}")
    ps = reachable(i,sx,sy)
    for x in range(h):
        reached[(x,i)] = len({p for p in reachable(i,sx,sy) if p[0] == x})

for x in range(h):
    print(x, reached[(x,M-2)],reached[(x,M-1)])

N = 26501365

reached_on_sx = (N // w) * reached[(sx,M-1)] + reached[(sx,N%w)]
exit()

eventually = dict()
for offset in range(-h+1,h):
    results = []
    for i in range(100):
        qs = {p for p in reachable(i,sx,sy) if p[0]-offset == p[1]}
        results.append(len(qs))
        if len(results) > 4 and results[-1] == results[-3] > 0 and results[-2] == results[-4] > 0:
            break
    eventually[offset] = results[-2:]
    print(offset, results[-1],results[-2])

print(sum(eventually[o][0] for o in range(-h+1,h)))
print(sum(eventually[o][1] for o in range(-h+1,h)))


# for i, r in enumerate(results):
#     print(f"{i=} {r=}")
#     if i%2 == 0: print(f"r[{i}] + r[{i+1}]= {r + results[i+1]}")
print(len(reachable(98,sx,sy)))

print(len(reachable(99,sx,sy)))
# print(f"{results[-1]=},{results[-2]=}")
# acceven = [(testline,y) for y in range(0,w,2) if grid[(testline,y)] != "#"]
# accodd = [(testline,y) for y in range(1,w,2) if grid[(testline,y)] != "#"]
# print(f"{testline=}, {len(acceven)=}, {len(accodd)=}")

# for y in range(w):
#     print(grid[(testline,y)], end="")
# print()

"""
on the line of the start node, after s steps, we can reach at most s to the right,
and at most s to the left.
we can reach every node at distance the same parity as s.
except for # nodes.

if there were no #'s, we could reach after s steps a diamond of height and width s,
so exactly s * s nodes.
but in every diagonal of the grid we are missing some nodes.

"""
# for i in range(7):
#     print(len(reachable_pow(i,sx,sy)))
