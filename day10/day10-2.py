from itertools import product
from debugging import * 

# how each pipe connects tiles to each other
connections = {".": [], 
               "|": [(-1,0), (1, 0)], 
               "-": [(0,-1), (0, 1)], 
               "L": [(0, 1), (-1,0)], 
               "J": [(0,-1), (-1,0)],
               "F": [(0, 1), (1, 0)],
               "7": [(0,-1), (1, 0)],
               "S": [(0,1),(1,0),(-1,0),(0,-1)]}

# read file
filename = "input.txt"
with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]
h, w = len(ls), len(ls[0])
grid = {(i,j) : ls[i][j] for (i,j) in product(range(h),range(w))}


# calculate the neighbors of every node
neighbors = {}
for i, j in product(range(h), range(w)):
    neighbors[(i,j)] = []
    for d in connections[grid[(i,j)]]:
        md = (-d[0],-d[1])
        v = (i + d[0], j + d[1])
        if not(0 <= v[0] < h and 0 <= v[1] < w): continue
        if md in connections[grid[v]]:
            neighbors[(i,j)].append(v)

# calculate where the loop is
startnode = [(i,j) for (i,j) in product(range(h),range(w)) if grid[(i,j)] == "S"][0]

loop = [startnode]
onloop = {(i,j): False for (i,j) in product(range(h),range(w))}
onloop[startnode] = True

def find_next(node,prev):
    for v in neighbors[node]:
         if v != prev:
              return v
    assert False, f"node: {node}, neighbors: {neighbors[node]}"

curr = find_next(startnode,None)
prev = startnode

while curr != startnode:
    loop.append(curr)
    onloop[curr] = True
    curr,prev = find_next(curr,prev),curr

# create a clean loopgrid
loopgrid = {}
for (x,y) in product(range(h),range(w)):
    if onloop[(x,y)]:
        loopgrid[(x,y)] = grid[(x,y)]
    else:
        loopgrid[(x,y)] = "."

# find the correct pipe for the start node
connecttostart = [loop[1],loop[-1]]
delta = [(x-startnode[0], y-startnode[1]) for (x,y) in connecttostart]
for c in "|-LFJ7":
    if set(delta) == set(connections[c]):
        startpipe = c
        break 
loopgrid[startnode] = startpipe

# create bigger grid
bigw = 2*w+2
bigh = 2*h+1
biggrid = {(i,j): "" for (i,j) in product(range(bigh),range(bigw))}

for x in range(h):
    for y in range(w):
        biggrid[(2 * x, 2 * y)] = "x"
        biggrid[(2 * x, 2 * y + 1)] = "x"
        biggrid[(2 * x + 1, 2 * y)] = "x"
        biggrid[(2 * x + 1, 2 * y + 1)] = loopgrid[(x,y)]
        
        biggrid[(2 * h, 2*y)] = "x"
        biggrid[(2*h,2*y+1)] = "x"
    biggrid[(2*x, 2 * w)] = "x"
    biggrid[(2*x+1, 2*w)] = "x"
biggrid[(2*h,2*w+1)] = "x"

# interpolate how the pipes are connected in this bigger grid
for x,y in product(range(h),range(w)):
    if onloop[(x,y)]:
        for ux, uy in neighbors[(x,y)]:
            d = (ux-x,uy-y)
            xb, yb = 2 * x + 1, 2 * y + 1
            if d[0] == 0:
                biggrid[xb,yb+d[1]] = "-"
            else:
                biggrid[xb+d[0],yb] = "|"

# find all the nodes that are outside this loop
is_outside = {(x,y) : False for x,y in product(range(bigh),range(bigw))}

new = []
for x in range(bigh):
    is_outside[(x,0)] = True
    is_outside[(x,bigw-1)] = True
    new.append((x,0))
    new.append((x,bigw-1))
for y in range(bigw):
    is_outside[(0,y)] = True
    is_outside[(bigh-1,y)] = True
    new.append((0,y))
    new.append((bigh-1,y))

while len(new) > 0:
    count = sum(is_outside.values())
    newnew = []
    for (x,y) in new:
        for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < bigh and 0 <= ny < bigw): continue
            if not is_outside[(nx,ny)] and biggrid[(nx,ny)] in ["x", "."]:
                is_outside[(nx,ny)] = True
                newnew.append((nx,ny))
    new = newnew

c = 0
for (x,y) in product(range(bigh),range(bigw)):
    if not is_outside[(x,y)] and biggrid[(x,y)] == ".":
        c += 1
print(c)
