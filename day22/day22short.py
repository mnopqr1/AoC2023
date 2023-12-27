from itertools import product
from typing import List, Tuple

directions = [(1,0,0),(0,1,0),(0,0,1)]

def direction(s,e):
    diff = [i for i in range(3) if s[i] != e[i]]
    return diff[0] if len(diff) == 1 else None

def length(s,e):
    d = direction(s,e)
    if d is None: return 1
    return e[d] - s[d] + 1

class Brick:
    s: Tuple[int,int,int]
    d: int
    key: int
    locations: List[int]

    def __init__(self,s,e,key):
        self.s = s
        self.e = e
        self.key = key
        self.d = direction(s,e)
        
        self.locations = [s]
        sx, sy, sz = s
        if self.d is not None:
            dx,dy,dz = directions[self.d]
            for c in range(1,length(s,e)):
                self.locations.append((sx+c*dx,sy+c*dy,sz+c*dz))

    def isvertical(self):
        return self.d in [0,1]
    
    def dropone(self):
        sx,sy,sz = self.s
        ex,ey,ez = self.e
        self.s = (sx,sy,sz-1)
        self.e = (ex,ey,ez-1)
        self.locations = [(x,y,z-1) for (x,y,z) in self.locations]

class Grid:
    def __init__(self, maxs):
        self.content = \
        {z: {(i,j) : None for (i,j) in product(range(0,maxs[0]+1),range(0,maxs[1]+1))} \
         for z in range(1,maxs[2]+1)}
        self.maxx, self.maxy, self.maxz = maxs

    def set(self, x, y, z, b):
        self.content[z][(x,y)] = b

    def get(self, x,y,z):
        return self.content[z][(x,y)]
    
    def isempty(self,x,y,z):
        return self.content[z][(x,y)] is None

def canfall(b,g):
    return b.s[2] != 1 and all(z != b.s[2] or g.isempty(x,y,z-1) for (x,y,z) in b.locations)

def dropone(b,g):
    for (x,y,z) in b.locations:
        g.set(x,y,z,None)
    for (x,y,z) in b.locations:
        g.set(x,y,z-1,b)
    b.dropone()

def fall(b,grid):
    if not canfall(b,grid):
        return True
    while canfall(b,grid):
        dropone(b,grid)
    return False

def supports(b,g):
    res = []
    toppart = b.locations if b.isvertical() else [b.e]
    for (x,y,z) in toppart:
        if z < g.maxz:
            c = g.get(x,y,z+1)
            if c is not None:
                res.append(c)
    return list(set(res))

def tryremoving(supporting, supportedby,b):
    queue = [b]
    reached = set()
    reached.add(b)
    while len(queue) > 0:
        cur = queue.pop(0)
        for c in supporting[cur]:
            if all(d in reached for d in supportedby[c]):
                queue.append(c)
                reached.add(c)
    return len(reached) - 1

def main():
    filename = "input.txt"
    with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]

    bricks = []
    for i, l in enumerate(ls):
        s, e = [tuple(int(co) for co in p.split(",")) for p in l.split("~")]
        key = i
        bricks.append(Brick(s,e,key))

    maxs = [max(b.e[i] for b in bricks) for i in range(3)]
    grid = Grid(maxs)

    for b in bricks:
        for (nx,ny,nz) in b.locations:
            grid.set(nx,ny,nz,b)
    
    done = False
    while not done:
        done = True
        for b in bricks:
            r = fall(b,grid)
            if not r:
                done = False

    supporting = {b : [] for b in bricks}
    supportedby = {b : [] for b in bricks}
    for b in bricks:
        supporting[b] = supports(b,grid)
        for c in supporting[b]:
            supportedby[c].append(b)
    
    ct1 = 0
    for b in bricks:
        if not any(len(supportedby[c]) == 1 for c in supporting[b]):
            ct1 += 1
    ct2 = 0
    for b in bricks:
        r = tryremoving(supporting,supportedby,b)
        ct2 += r

    assert ct1 == 441
    assert ct2 == 80778


if __name__ == "__main__":
    main()
