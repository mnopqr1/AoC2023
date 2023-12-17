from functools import cache
from math import inf
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

answer = 0

h,w = len(ls), len(ls[0])
grid = {(x,y) : int(ls[x][y]) for (x,y) in product(range(h),range(w))}
# graph = {}
# for (x,y) in product(range(h), range(w)):
#     steps = []

# cost = {(x,y) : inf for (x,y) in product(range(h),range(w))}
# cost[(h-1,w-1)] = 0

# mem = {}
# for d in [(0,1),(0,-1),(1,0),(-1,0)]:
#     for c in range(3):
#         mem[((h-1,w-1),c,d)] = 0
# visited = {(x,y): False for (x,y) in product(range(h), range(w))}
# def bestpath_rec(n,c,d): 
#     """Best path starting from node n if we have just done c steps in direction d."""
#     # visited[n] = True
#     key = (n,c,d)
#     if key in mem.keys():
#         return mem[key]
#     x,y = n
#     dx0,dy0 = d
#     poss = [(dx,dy) for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)] if (0 <= x + dx < h and 0 <= y + dy < w and (-dx,-dy) != (dx0,dy0))]
#     if c == 3:
#         if (dx0,dy0) in poss: poss.remove((dx0,dy0))
#         c = 0
#     m = inf
#     for (dx,dy) in poss:
#         newkey = ((x+dx,y+dy),c+1,(dx,dy))
#         newcost = inf
#         if not visited[newkey[0]]:
#             newcost = grid[(x+dx,y+dy)] + bestpath_rec(*newkey)
#         if newcost < m:
#             m = newcost
#     mem[key] = m
#     return m

# answer = bestpath_rec((11,11),0,(0,1))

def show(g):
    for (x,y) in product(range(h),range(w)):
        print(min(g[(x,y,c,dx,dy)] for c in range(3) for (dx,dy) in DIRS),end=",")
        if y == w-1:
            print()

sx,sy = 0,0
DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
nodes = [(x,y,c,dx,dy) for (x,y) in product(range(h),range(w)) for c in range(4) for (dx,dy) in DIRS]
cost = {n : inf for n in nodes}
for c in range(4):
    for (dx,dy) in DIRS:
        cost[(sx,sy,c,dx,dy)] = 0
NEIGHBORS = {}
for n in nodes:
    x,y,c,dx0,dy0 = n
    neighbors = []
    poss = [(dx,dy) for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)] if (0 <= x + dx < h and 0 <= y + dy < w and (-dx,-dy) != (dx0,dy0))]
    for (dx,dy) in poss:
        if c == 3 and (dx,dy) == (dx0,dy0):
            continue
        newc = c+1 if (dx,dy) == (dx0,dy0) else 0
        neighbors.append((x+dx,y+dy,newc,dx,dy))
    NEIGHBORS[(x,y,c,dx0,dy0)] = neighbors

queue = [n for n in nodes]

D = False
while len(queue) > 0:
    print(len(queue))
    n = queue[0]
    mi = 0
    for i,other in enumerate(queue):
        if cost[other] < cost[n]:
            n = other
            mi = i
    queue.pop(mi)

    # queue.sort(key=lambda n: cost[n])
    # n = queue.pop(0)
    if D: print(f"treating {n}")
    
    for newn in NEIGHBORS[n]:
        if D: print(f"considering {newn}")
        nx,ny,_,_,_ = newn
        alt = cost[n] + grid[(nx,ny)]
        if D: print(f"alt = {alt}")
        if alt < cost[newn]:
            cost[newn] = alt
    
    if D: show(cost)
    if D: input()

tx,ty = h-1,w-1

answer = min(cost[(tx,ty,c,dx,dy)] for c in range(3) for (dx,dy) in DIRS)

print(answer)