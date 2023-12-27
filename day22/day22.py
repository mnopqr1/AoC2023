from itertools import product
from typing import List, Tuple

def direction(s,e):
    diff = [i for i in range(3) if s[i] != e[i]]
    assert len(diff) <= 1
    return diff[0] if len(diff) == 1 else None

def length(s,e):
    d = direction(s,e)
    if d is None: return 1
    assert e[d] > s[d]
    return e[d] - s[d] + 1

directions = [(1,0,0),(0,1,0),(0,0,1)]

class Brick:
    s: Tuple[int,int,int]
    d: int
    name: str
    key: int
    occupies: List[int]

    def __init__(self,s,e,name,key):
        self.s = s
        self.e = e
        self.name = name
        self.key = key
        self.occupies = [s]
        self.d = direction(s,e)
        
        sx, sy, sz = s
        if self.d is not None:
            dx,dy,dz = directions[self.d]
            for c in range(1,length(s,e)):
                self.occupies.append((sx+c*dx,sy+c*dy,sz+c*dz))
        # assert len(self.occupies) == length(s,e)

    def __repr__(self):
        return f"{self.name}: {self.s} - {self.e}, direction {self.d}, length {len(self.occupies)}"

    def dropone(self):
        sx,sy,sz = self.s
        ex,ey,ez = self.e
        self.s = (sx,sy,sz-1)
        self.e = (ex,ey,ez-1)
        self.occupies = [(x,y,z-1) for (x,y,z) in self.occupies]

class Grid:
    def __init__(self, maxs):
        self.content = {z: 
         {(i,j) : None for (i,j) in product(range(0,maxs[0]+1),range(0,maxs[1]+1))} 
         for z in range(1,maxs[2]+1)}
        self.maxx, self.maxy, self.maxz = maxs
        
    def set(self, x,y,z, b):
        self.content[z][(x,y)] = b

    def get(self, x,y,z):
        return self.content[z][(x,y)]
    
    def isempty(self,x,y,z):
        return self.content[z][(x,y)] is None
    
    def showlevel(self,z):
        for (x,y) in product(range(0,self.maxx+1),range(0,self.maxy+1)):
            print(self.content[z][(x,y)], end="")
            if y == self.maxy:
                print()

    def showfront(self):
        for z in range(self.maxz,0,-1):
            print(z, end=" ")
            for x in range(0,self.maxx+1):
                for y in range(0,self.maxy+1):
                    c = self.content[z][(x,y)]
                    if c is not None: 
                        print(c.name, end="")
                        break
                if y == self.maxy and c is None:
                    print(".", end="")
            print()

    def showside(self):
        for z in range(self.maxz,0,-1):
            print(z, end=" ")
            for y in range(0,self.maxy+1):
                for x in range(0,self.maxx+1):
                    c = self.content[z][(x,y)]
                    if c is not None: 
                        print(c.name, end="")
                        break
                if x == self.maxx and c is None:
                    print(".", end="")
            print()

def canfall(b,g):
    if b.s[2] == 1:
        return False
    for (x,y,z) in b.occupies:
        if z == b.s[2] and not g.isempty(x,y,z-1):
            return False
    return True

def dropone(b,g):
    for (x,y,z) in b.occupies:
        g.set(x,y,z, None)
    for (x,y,z) in b.occupies:
        assert g.isempty(x,y,z-1)
        g.set(x,y,z-1,b)
    b.dropone()

def supports(b,g):
    res = []
    if b.d == 0 or b.d == 1:
        for (x,y,z) in b.occupies:
            if z < g.maxz:
                c = g.get(x,y,z+1)
                if c is not None:
                    res.append(c)
    else:
        x,y,z = b.e
        if z < g.maxz:
            c = g.get(x,y,z+1)
            if c is not None:
                res.append(c)
    return list(set(res))

D = False
def debug(grid):
    grid.showfront()
    print("-" * 10)
    grid.showside()


def fall(b,grid):
    if D: 
        print(b)
        debug(grid)
    if not canfall(b,grid):
        if D: 
            print(f"{b.name} cannot fall, returning immediately")
            input()
        return True
    while canfall(b,grid):
        if D: print(f"{b.name} can fall")
        dropone(b,grid)
        if D: 
            print(f"after falling:")
            debug(grid)
            input()
    if D:
        print(f"{b.name} has stopped falling, returning")
        input()
    return False


def experiment(supporting, supportedby,b):
    queue = [b]
    reached = set()
    reached.add(b)
    while len(queue) > 0:
        cur = queue.pop(0)
        for c in supporting[cur]:
            if all(d in reached for d in supportedby[c]):
                queue.append(c)
                reached.add(c)
    return len(reached)-1

def main():
    filename = "input.txt"
    with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]

    bricks = []
    for i, l in enumerate(ls):
        s, e = [tuple(int(co) for co in p.split(",")) for p in l.split("~")]
        name = chr(ord('A')+(i%26))
        key = i
        bricks.append(Brick(s,e,name,key))

    if D:
        for b in bricks:
            print(b)

    maxs = [max(b.e[i] for b in bricks) for i in range(3)]
    grid = Grid(maxs)

    for b in bricks:
        for (nx,ny,nz) in b.occupies:
            assert grid.isempty(nx,ny,nz) # there should be no overlapping blocks in beginning
            grid.set(nx,ny,nz,b)
    
    done = False
    while not done:
        done = True
        for b in bricks:
            if D: print(f"starting to drop {b.name}")
            r = fall(b,grid)
            done = (done and r)
        if D:
            debug(grid)
            input()

    supporting = {b : [] for b in bricks}
    supportedby = {b : [] for b in bricks}
    for b in bricks:
        supporting[b] = supports(b,grid)
        for c in supporting[b]:
            supportedby[c].append(b)
    
    ct = 0
    for b in bricks:
        if D:
            print(f"{b.name} supports:")
            print(supporting[b])
            print(f"{b.name} is supported by:")
            print(supportedby[b])
        
        nec = False
        for c in supporting[b]:
            if len(supportedby[c]) == 1:
                nec = True
                # assert supportedby[c] == [b]
                if D: print(f"{b.name} cannot be removed")
        if not nec:
            ct += 1
    print(ct)
    ct2 = 0
    for b in bricks:
        ct2 += experiment(supporting,supportedby,b)
    print(ct2)

    assert ct == 441
    assert ct2 == 80778

main()
