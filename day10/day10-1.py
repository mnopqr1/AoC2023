from itertools import product
from math import inf
from utils import *

connections = {".": [], 
               "|": [(-1,0), (1, 0)], 
               "-": [(0,-1), (0, 1)], 
               "L": [(0, 1), (-1,0)], 
               "J": [(0,-1), (-1,0)],
               "F": [(0, 1), (1, 0)],
               "7": [(0,-1), (1, 0)],
               "S": [(0,1),(1,0),(-1,0),(0,-1)]}

def parse(ls):
    return ls

def dists(ls):
    grid = {}
    dist = {}
    
    h, w = len(ls), len(ls[0])
    for i, j in product(range(h), range(w)):
        grid[(i,j)] = ls[i][j]
        if ls[i][j] == "S":
            dist[(i,j)] = 0
        else:
            dist[(i,j)] = inf
    
    neighbors = {}
    for i, j in product(range(h), range(w)):
        neighbors[(i,j)] = []
        for d in connections[grid[(i,j)]]:
            md = (-d[0],-d[1])
            v = (i + d[0], j + d[1])
            if not(0 <= v[0] < h and 0 <= v[1] < w): continue
            if md in connections[grid[v]]:
                neighbors[(i,j)].append(v)
    
    new = True
    c = 0
    while new:
        new = False
        for u in grid.keys():
            for v in neighbors[u]:
                if dist[u] + 1 < dist[v]:
                    new = True
                    dist[v] = dist[u] + 1
        c += 1
    return dist, h, w

def showgrid(val, h, w, trans, sep):
    for i, j in product(range(h),range(w)):
        if val[(i,j)] in trans.keys():
            print(trans[val[(i,j)]], end=sep)
        else:
             print(val[(i,j)], end=sep)
        if j == w - 1: print()

def solve1(dist, h, w):
    return max(dist[(i,j)] for i, j in product(range(h),range(w)) if dist[(i,j)] != inf)


def solve(filename, expected=None):
    with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]
    
    h, w = len(ls), len(ls[0])

    dist, h, w = dists(ls)
    s = [solve1(dist,h,w)]
    
    report(filename, s, expected)
    
if __name__ == "__main__":
    solve("input.txt")