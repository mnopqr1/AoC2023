from utils import *
from typing import List, Tuple
from functools import cmp_to_key
from collections import Counter

CARDS = "AKQT98765432J"

def parse(ls : List[str]) -> List[Tuple[str,int]]:
    hs = [0] * len(ls)
    for i, l in enumerate(ls):
        h, s = l.split(" ")
        hs[i] = (h,int(s.rstrip()))
    return hs

def cmpcard(c1, c2):
    return CARDS.find(c2) - CARDS.find(c1)

def cmplex(h1, h2):
    for i in range(len(h1)):
        c = cmpcard(h1[i],h2[i])
        if c != 0:
            return c
    return 0

def score1(h):
    cts = Counter(h)
    if 5 in cts.values(): return 6
    if 4 in cts.values(): return 5
    if 3 in cts.values():
        if 2 in cts.values(): return 4
        else: return 3
    twos = [k for k in cts.keys() if cts[k]==2]
    return len(twos) 

def score_with_joker(h):
    if 'J' not in h: return score1(h)
    if h == 'JJJJJ': return 6
    best = 0
    for c in CARDS:
        if c == 'J' or c not in h: continue
        newh = h.replace('J', c)
        s = score1(newh)
        if s > best:
            best = s
    return best

def cmphand(h1, h2):
    s1, s2 = score_with_joker(h1), score_with_joker(h2)
    if s1 != s2: return s1 - s2
    else: return cmplex(h1, h2)

def solve2(xs):
    ys = sorted(xs, key=cmp_to_key(lambda x1, x2: cmphand(x1[0],x2[0])))
    t = 0
    for r, y in enumerate(ys):
        t += (r+1) * y[1]
    return t

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    xs = parse(ls)
    s = [solve2(xs)]
    report(filename, s, expected)
    
if __name__ == "__main__":
    solve("test.txt", [5905])
    solve("input.txt")