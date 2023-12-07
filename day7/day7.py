from utils import *
from typing import List, Tuple
from functools import cmp_to_key
from collections import Counter
cards = "AKQJT98765432"

def parse(ls : List[str]) -> List[Tuple[str,int]]:
    hs = [0] * len(ls)
    for i, l in enumerate(ls):
        h, s = l.split(" ")
        hs[i] = (h,int(s.rstrip()))
    return hs

#c1 better than c2 => positive
def cmpcard(c1, c2):
    s1, s2 = cards.find(c1), cards.find(c2)
    if s1 < s2: return 1
    if s1 == s2: return 0
    if s1 > s2: return -1

def cmplex(h1, h2):
    for i in range(len(h1)):
        c = cmpcard(h1[i],h2[i])
        if c != 0:
            return c
    return 0

def score(h):
    cts = Counter(h)
    # print(cts)
    if 5 in cts.values(): return 6
    if 4 in cts.values(): return 5
    if 3 in cts.values():
        if 2 in cts.values(): return 4
        else: return 3
    twos = [k for k in cts.keys() if cts[k]==2]
    return len(twos) 

#h1 better than h2 => positive
def cmphand(h1, h2):
    s1, s2 = score(h1), score(h2)
    if s1 != s2: return s1 - s2
    else: return cmplex(h1, h2)

def cmpitem (x1, x2):

    return cmphand(x1[0],x2[0])

def solve1(xs):
    ysunique = dict.fromkeys(xs)
    assert len(ysunique) == len(xs)
    ys = sorted(xs, key=cmp_to_key(cmpitem))
    print(ys)
    t = 0
    for r, y in enumerate(ys):
        t += (r+1) * y[1]
    return t

def solve2(xs):
    pass

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    xs = parse(ls)
    s = [solve1(xs), solve2(xs)]
    
    report(filename, s, expected)
    
if __name__ == "__main__":
    solve("test.txt", [6440,None])
    solve("input.txt")