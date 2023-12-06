from utils import *
from math import ceil, floor, sqrt
from functools import reduce
import operator

def parse1(ls):
    times, dists = [[int(n) for n in l.split(" ")[1:] if n != ""] for l in ls]
    return (times,dists)

def parse2(ls):
    t, d = [int(l.replace(" ", "").split(":")[1]) for l in ls]
    return (t,d)
    
def quadratic(a,b,c):
    D = b * b - 4 * a * c
    if D < 0: return None, None
    sD = sqrt(D)
    return (-b - sD) / (2 * a), (-b + sD) / (2 * a)

def nwins(t,d):
    # distance traveled when button held for x seconds = x * (t - x)
    # to solve x * (t - x) > d, we want x in [0,t] so that x^2 - tx + d < 0
    x1, x2 = quadratic(1, -t, d)
    # assert x1 is not None       # there's always some way to be better
    eps = .000001               # need a little offset because we want strictly better 
    x1r, x2r = ceil(x1+eps),floor(x2-eps)
    return x2r - x1r + 1

def solve1(ls):
    ts, ds = parse1(ls)
    return reduce(operator.mul, [nwins(ts[i],ds[i]) for i in range(len(ts))])

def solve2(ls):
    t, d = parse2(ls)
    return nwins(t,d)

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    s = [solve1(ls), solve2(ls)]
    
    report(filename, s, expected)
    
if __name__ == "__main__":
    solve("test.txt", [288,71503])
    solve("input.txt")
