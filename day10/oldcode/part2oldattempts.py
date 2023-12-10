from itertools import product

filename = "smalltest3.txt"

with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]
    
h, w = len(ls), len(ls[0])

grid = {(i,j) : ls[i][j] for (i,j) in product(range(h),range(w))}

connections = {".": [], 
               "|": [(-1,0), (1, 0)], 
               "-": [(0,-1), (0, 1)], 
               "L": [(0, 1), (-1,0)], 
               "J": [(0,-1), (-1,0)],
               "F": [(0, 1), (1, 0)],
               "7": [(0,-1), (1, 0)],
               "S": [(0,1),(1,0),(-1,0),(0,-1)]}

# calculate main loop

startnode = [(i,j) for (i,j) in product(range(h),range(w)) if grid[(i,j)] == "S"][0]

loop = [startnode]
onloop = {(i,j): False for (i,j) in product(range(h),range(w))}
onloop[startnode] = True

neighbors = {}
for i, j in product(range(h), range(w)):
    neighbors[(i,j)] = []
    for d in connections[grid[(i,j)]]:
        md = (-d[0],-d[1])
        v = (i + d[0], j + d[1])
        if not(0 <= v[0] < h and 0 <= v[1] < w): continue
        if md in connections[grid[v]]:
            neighbors[(i,j)].append(v)

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



# graph = {(x,y): [(x+dx,y+dy) for (dx,dy) in product([-1,0,1],[-1,0,1]) if (dx,dy) != (0,0)] 
#                  for (x,y) in product(range(h),range(w))}

# for (x,y) in loop:

loopgrid = {}
for (x,y) in product(range(h),range(w)):
    if onloop[(x,y)]:
        loopgrid[(x,y)] = grid[(x,y)]
    else:
        loopgrid[(x,y)] = "."

connecttostart = [loop[1],loop[-1]]
delta = [(x-startnode[0], y-startnode[1]) for (x,y) in connecttostart]
for c in "|-LFJ7":
    if set(delta) == set(connections[c]):
        startpipe = c
        break 
loopgrid[startnode] = startpipe
# print(startpipe)

# for (i,j) in product(range(h),range(w)):
#      print(loopgrid[(i,j)],end="")
#      if j == w-1: print()

# F-7    0
# |.|    1
# L-J    2

# OOOOO  -1
# .----.
# O|OOO|O  0
# O|OOO|O  1
# O|OOO|O  2
# OOOOO  3


rooms = [(x,y) for x,y in product(range(-1,h+1),range(-1,w+1))]
graph = {}

# first put every possible connection in graph
for (x,y) in rooms:
    graph[(x,y)] = []
    for (dx,dy) in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx, ny = x + dx, y + dy
        if not(-1 <= nx <= h and -1 <= ny <= w):
            continue    
        graph[(x,y)].append((nx,ny))

breaks = {"F": [(-1,0),(0,-1)],
          "|": [(0,1),(0,-1)],
          "-": [(1,0),(-1,0)],
          "L": [(1,0),(0,-1)],
          "J": [(0,1),(1,0)],
          "7": [(0,1),(-1,0)]}
# break connections according to pipes on loop
for (x,y) in loop:
    wall = loopgrid[(x,y)]
    for b in breaks[wall]:
        rx1, ry1 = x,y
        rx2, ry2 = x + b[0], y + b[1]
        # assert -1 <= rx1 <= h and -1 <= rx2 <= w
        if (rx2,ry2) in graph[(rx1,ry1)]:
            graph[(rx1,ry1)].remove((rx2,ry2))
        if (rx1,ry1) in graph[(rx2,ry2)]:
            graph[(rx2,ry2)].remove((rx1,ry1))

# for (x,y) in rooms:
#     print(f"{(x,y)}: {graph[(x,y)]}")

outside = {(-1,y) for y in range(-1,w+1)}.union({(h,y) for y in range(-1,w+1)}).union({(x,-1) for x in range(-1,h+1)}).union({(x,w) for x in range(-1,h+1)})

newcount = len(outside)
oldcount = 0
is_outside = {(x,y) : False for x,y in product(range(h),range(w))}

# print(outside)
while len(outside) > oldcount:
    oldcount = len(outside)
    for room in outside:
        outside = outside.union(set(graph[room]))
        for r in graph[room]:
            is_outside[r] = True

inside = {(x,y) for (x,y) in rooms if not is_outside[(x,y)] and not onloop[(x,y)]}

for (x,y) in product(range(h),range(w)):
    if onloop[(x,y)]:
        print(loopgrid[(x,y)], end="")
    elif is_outside[(x,y)]: 
        print("O",end="")
    else:
        print("I", end="")
    if y == w-1: print()
# print(len(inside))

def rotate45(grid):
    for (x,y) in product(range(w),range(h)):
        print(grid[(y,x)], end="")
        if y == h-1: print()

rotate45(grid)




# def hasfreedom(x,y,outside,occupied):
#     if occupied[(x,y)]:
#         return False
#     for d in [(-1,0),(1,0),(0,1),(0,-1)]:
#         nx, ny = x + d[0], y + d[1]
#         if (nx,ny) in outside and not occupied[(nx,ny)]:
#             return True
#     return False

def hasfreedom(x,y,outside,occupied):
    if occupied[(x,y)]:
        return False
    for dx,dy in product([-1,0,1],[-1,0,1]):
        if (dx,dy) == (0,0): continue
        nx, ny = x + dx, y + dy
        if (nx,ny) in outside and not occupied[(nx,ny)]:
            return True
    return False

def solve2(dist,h,w):
    # showgrid(dist, h, w, {inf: "."}, ",")

    occupied = {(x,y) : dist[(x,y)] != inf for x,y in product(range(h),range(w))}

    showgrid(occupied,h,w, {True:"X", False:"."}, "")
    outside = {(-1,y) for y in range(w)}.union({(h,y) for y in range(w)}).union({(x,-1) for x in range(h)}).union({(x,w) for x in range(h)})
    for y in range(w):
        occupied[(-1,y)] = False
        occupied[(h,y)] = False
    for x in range(h):
        occupied[(x,-1)] = False
        occupied[(x,w)] = False

    ringsize = len(outside)
    assert ringsize == 2 * (h+w)
    assert h == w
    b, e = 0, h-1
    while b < e:
        for y in range(w):
            if hasfreedom(b,y,outside,occupied):
                outside.add((b,y))
            if hasfreedom(e,y,outside,occupied):
                outside.add((e,y))
        for x in range(h):
            if hasfreedom(x,b,outside,occupied):
                outside.add((x,b))
            if hasfreedom(x,e,outside,occupied):
                outside.add((x,e))
        b += 1
        e -= 1
    
    showgrid({(i,j) : (i,j) in outside for i,j in product(range(h),range(w))}, h,w,{True:"O", False:"."}, "")
    inside = {(i,j) for i,j in product(range(h),range(w)) if not occupied[(i,j)] and (i,j) not in outside}
    showgrid({(i,j) : (i,j) in inside for i,j in product(range(h),range(w))}, h,w,{True:"I", False:"."}, "")
    return len(inside)

#  OOOO
# OXXXXO
# OX.XXO
# OXX.XO
# OXX..O
#  OOOO

def show_in_one_grid(ls):
    h, w = len(ls) // 3, len(ls[0])
    # occupied = 0, outside = 1, inside = 2
    grid = {}
    lc = 0
    symbol = {0: "X", 1: "O", 2: "I"}
    for k in range(3):
        for x in range(h):
            for y in range(w):
                if ls[lc][y] == symbol[k]:
                    assert (x,y) not in grid.keys()
                    grid[(x,y)] = k
            lc += 1
    showgrid(grid,h,w,symbol,"")

def showpipes(grid, h, w):
    tiles =   {".": ["...","...","..."], 
               "|": [".X.",".X.",".X."], 
               "-": ["...","XXX","..."], 
               "L": ["X..","X..","XXX"], 
               "J": ["..X","..X","XXX"],
               "F": ["XXX", "X..","X.."],
               "7": ["XXX","..X","..X"],
               "S": ["...",".S.","..."]}
    outgrid = [[0] * (w * 3) for _ in range(h*3)]
    for x in range(h):
        for y in range(w):
            for i in range(3):
                for j in range(3):
                    outgrid[x*3+i][y*3+j] = tiles[grid[(x,y)]][i][j]
    
    for l in outgrid:
        print("".join(l))


        
def testoutput(file):
    with open(file) as f:
        ls = [l.rstrip() for l in f.readlines()]