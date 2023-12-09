from functools import reduce
from utils import *
from typing import List

def parse(ls):
    return [[int(n) for n in l.rstrip().split()] for l in ls]
    
def value1(l: List[int]) -> int:
    newl = [x for x in l]
    r = 0
    while not all(x == 0 for x in newl):
        r += newl[-1]
        oldl = newl
        newl = [oldl[i+1] - oldl[i] for i in range(len(oldl)-1)]
    return r
    
def value2(l: List[int]) -> int:
    newl = [x for x in l]
    startvals = []
    while not all(x == 0 for x in newl):
        startvals.append(newl[0])
        oldl = newl
        newl = [oldl[i+1] - oldl[i] for i in range(len(oldl)-1)]
    startvals.reverse()
    return reduce(lambda x,y: y-x,startvals,0)

def solve1(xs):
    return sum(value1(l) for l in xs)

def solve2(xs):
    return sum(value2(l) for l in xs)

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    xs = parse(ls)
    s = [solve1(xs), solve2(xs)]
    report(filename, s, expected)
    
if __name__ == "__main__":
    # solve("test.txt", [None,None])
    solve("input.txt")