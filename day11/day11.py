from utils import *
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = f.readlines()
ls = [l.rstrip() for l in ls]
h, w = len(ls), len(ls[0])

grid = dict()
stars = []
for (x,y) in product(range(h),range(w)):
    if ls[x][y] == ".":
        grid[(x,y)] = False
    else:
        assert ls[x][y] == "#"
        grid[(x,y)] = True
        stars.append((x,y))

emptycols = []
for y in range(w):
    if all(not grid[(x,y)] for x in range(h)):
        emptycols.append(y)

emptyrows = []
for x in range(h):
    if all(not grid[(x,y)] for y in range(w)):
        emptyrows.append(x)

def n_between(xs, i, j):
    if i > j: return n_between(xs, j, i)
    r = 0
    for x in xs:
        if x > i and x < j:
            r += 1
    return r

def distance(s,t, expansion):
    return abs(s[0]-t[0]) + abs(s[1]-t[1]) + (expansion-1) * n_between(emptyrows,s[0],t[0]) + (expansion-1) * n_between(emptycols,s[1],t[1])

answer = 0

for i, s in enumerate(stars):
    for j,t in enumerate(stars[i+1:]):
        answer += distance(s,t,1000000)
        # print(i+1,"to", i+1+j+1, distance(s,t))

expected = 0
report(filename, [answer], [expected])
