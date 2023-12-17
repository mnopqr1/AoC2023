from functools import cache
from math import inf
from itertools import product

filename = "test.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

answer = 0

SYMBOL = {(1,0) : "v", (-1,0): "^", (0,1): ">", (0,-1): "<"}
h,w = len(ls), len(ls[0])
grid = {(x,y) : int(ls[x][y]) for (x,y) in product(range(h),range(w))}

def show():
    for (x,y) in product(range(h),range(w)):
        if cost[(x,y)] == inf:
            print("---", end="|")
        else:
            if len(last3[(x,y)]) == 0:
                symb="|"
            else:
                symb=SYMBOL[last3[(x,y)][-1]]
            print(f"{symb}{cost[(x,y)]:3}",end="")
        if y == w-1:
            print()

def showpath():
    for (x,y) in product(range(h),range(w)):
        if cost[(x,y)] == inf:
            print("---", end="|")
        else:
            if (x,y) not in path:
                symb="|"
            else:
                symb=SYMBOL[last3[(x,y)][-1]]
            print(f"{symb}{grid[(x,y)]:3}",end="")
        if y == w-1:
            print()

sx,sy = 0,0
DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
nodes = [(x,y) for (x,y) in product(range(h),range(w))]
cost = {n : inf for n in nodes}
cost[(sx,sy)] = 0
last3 = {n : [] for n in nodes}

def mincost(queue):
    n = queue[0]
    mi = 0
    for i,other in enumerate(queue):
        if cost[other] < cost[n]:
            n = other
            mi = i
    return mi

queue = [n for n in nodes]


# moves = [(1,1),(1,2),(1,3),(-1,1),(-1,2),(-1,3),(-1,1),(1,-1),(1,-2),(1,-3),(-1,-1),(-1,-2),(-1,-3)]
done = {n : False for n in nodes}
while len(queue) > 0:
    mi = mincost(queue)
    cx, cy = queue.pop(mi)
    for (dx,dy) in DIRS:
        nx = cx + dx
        ny = cy + dy
        if not ((0 <= nx < h) and (0 <= ny < w)):
            continue
        if len(last3[(cx,cy)]) == 3 and all((dx0,dy0) == (dx,dy) for (dx0,dy0) in last3[(cx,cy)]):
            queue.append((cx+dx,cy+dy))
            continue
        if len(last3[(cx,cy)]) >= 1:
            ldx, ldy = last3[(cx,cy)][-1]
            if (dx,dy) == (-ldx,-ldy):
                continue
        if not done[(nx,ny)]:
            alt = cost[(cx,cy)] + grid[(nx,ny)]
            if alt < cost[(nx,ny)]:
                cost[(nx,ny)] = alt
                last3[(nx,ny)] = last3[(cx,cy)][-2:] + [(dx,dy)]
    # if not any((cx+dx,cy+dy) in queue for (dx,dy) in product(range(3),range(3)) if 0 <= cx + dx < h and 0<= cy+dy < w):
        # done[(cx,cy)] = True
    # show()
    # print(queue)
    # input()
tx,ty = h-1,w-1

p = (tx,ty)
path = []
while p != (0,0):
    path.append(p)
    dx, dy = last3[p][-1]
    p = p[0] - dx, p[1] - dy
print(path)

show()
# showpath()

answer = cost[(tx,ty)]

# 1047 too high
print(answer)