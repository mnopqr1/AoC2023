from utils import *
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

answer = 0

def count(w):
    p = 0
    l = []
    while p < len(w):
        if w[p] == "#":
            b = 0
            while (p < len(w) and w[p] == "#"):
                p += 1
                b += 1
            l.append(b)
        elif w[p] == ".":
            p += 1
        else:
            assert False, "tried to count incomplete w"
    return l

# print(count(".#.#.###"))

def arrangements(w,cts):
    q = w.find("?")
    if q == -1:
        if count(w) == cts:
            return 1
        else:
            return 0
    else:
        r = 0
        new = w[:q] + "." + w[q+1:]
        r += arrangements(new,cts)
        new = w[:q] + "#" + w[q+1:]
        r += arrangements(new,cts)
    return r

for i, l in enumerate(ls):
    w, ctsraw = l.split(" ")
    cts = [int(n) for n in ctsraw.split(",")]
    
    r = arrangements(w,cts)
    answer += r
    print(i, r)

    
expected = None
report(filename, [answer], [expected])
