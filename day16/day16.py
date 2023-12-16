from typing import List, Tuple
from utils import *
from itertools import product
from dataclasses import dataclass

@dataclass
class Beam:
    x: int
    y: int
    dx: int
    dy: int

    def register(self):
        visited[(self.x,self.y,self.dx,self.dy)] = True

    def step(self):
        self.register()
        self.x += self.dx
        self.y += self.dy

    def update(self) -> List:
        while (0 <= self.x < h) and (0 <= self.y < w) and grid[(self.x,self.y)] == ".":
            if visited[(self.x,self.y,self.dx,self.dy)]:
                return []
            self.step()
 
        if not ((0 <= self.x < h) and (0 <= self.y < w)):
            return []

        c = grid[(self.x,self.y)]
        if c == "/" or c== "\\":
            self.register()
            self.dx, self.dy = MIRROR[c][(self.dx,self.dy)]
            self.register()
            self.step()
            return [self]
        else:
            # assert c == "-" or c == "|"
            newdirs = MIRROR[c][(self.dx,self.dy)]
            if len(newdirs) == 0:
                self.register()
                self.step()
                return [self]
            else:
                return [Beam(self.x,self.y,dx,dy) for (dx,dy) in newdirs]

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]
h, w = len(ls), len(ls[0])
grid = {(x,y) : ls[x][y] for (x,y) in product(range(h),range(w))}
DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

MIRROR = {"/" : {(0,1):(-1,0), (-1,0):(0,1), (1,0):(0,-1), (0,-1):(1,0)},
          "\\" : {(0,1):(1,0), (-1,0):(0,-1), (1,0):(0,1), (0,-1):(-1,0)},
          "-" : {(0,1) : [], (0,-1): [], (1,0) : [(0,1),(0,-1)], (-1,0) : [(0,1),(0,-1)]},
          "|" : {(1,0) : [], (-1,0): [], (0,1) : [(1,0),(-1,0)], (0,-1) : [(1,0),(-1,0)]}}

def reset():
    for (x,y) in product(range(h),range(w)):
        for (dx,dy) in DIRS:
            visited[(x,y,dx,dy)] = False

def test(x,y,dx,dy):
    reset()
    beams = [Beam(x,y,dx,dy)]
    while len(beams) > 0:
        newbeams = []
        for b in beams:
            newbeams += b.update()
        beams = newbeams
    return len([(x,y) for (x,y) in product(range(h),range(w)) if any(visited[(x,y,dx,dy)] for (dx,dy) in DIRS)])
    
visited = {(x,y,dx,dy) : False for (x,y) in product(range(h),range(w)) for (dx,dy) in DIRS}
results = []
for x in range(h):
    results.append(test(x,0,0,1))
    results.append(test(x,w-1,0,-1))
for y in range(w):
    results.append(test(0,y,1,0))
    results.append(test(h-1,y,-1,0))

assert results[0] == 7623
assert max(results) == 8244 
