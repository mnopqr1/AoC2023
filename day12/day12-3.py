from functools import cache, lru_cache
from math import comb
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

# def arrangements(w,cts):
#     q = w.find("?")
#     if q == -1:
#         if count(w) == cts:
#             return 1
#         else:
#             return 0
#     else:
#         r = 0
#         new = w[:q] + "." + w[q+1:]
#         r += arrangements(new,cts)
#         new = w[:q] + "#" + w[q+1:]
#         r += arrangements(new,cts)
#     return r

# def arrangements(w,cts):
#     if len(cts) == 0:
#         if "#" in w:
#             return 0
#         else:
#             return 1
    
#     c = cts[0]
#     newcts = cts[1:]
#     p = w.find("#")
#     if p == -1:
#         return 0
#     s = p
#     while (w[s] != "."):
#         s -= 1
#     s += 1
#     e = p
#     while (w[e] != "."):
#         e += 1
#     e -= 1
#     # [s,e] is the first block containing a "#"
#     # .?#?  c = 3

DEBUG = False

def blockcanstart(w,n,p):
    if p > 0 and w[p-1] == "#":
        return False
    if p+n-1 >= len(w):
        return False
    if "." in w[p:p+n]:
        return False
    if p + n < len(w) and w[p+n] == "#":
        return False
    return True

# positions where a block of n #'s could start
def places(w, n):
    r = []
    for i in range(len(w)-n+1):
        if blockcanstart(w,n,i):
            r.append(i)
    return r

# def onlyqs(n, cts, fr):
#     if fr >= len(cts):
#         return 1
#     c = cts[fr]
#     if c > n:
#         return 0
#     s = 0
#     for p in range(n):
#         s += onlyqs(p+c+1, cts, fr+1)
#     return s

# total length 5, 3 blocks
# #.#.### -> length 7 is the minimum
# total length 9, 4 blocks
# ###.###.##.# -> 12 is the minimum

# placing k blocks of total length s in n spots
# if it's one block, there are n - s + 1 spots:
# n = 5, s = 3, k = 1
# ###..
# .###.
# ..###

# if we have 2 blocks, want to choose gaps
# ##...###
# .##..###
# ..##.###
# .##.###.

# 3 = 0 + 3 + 0
# 3 = 1 + 2 + 0
# 3 = 2 + 1 + 0
# 3 = 1 + 1 + 1

@cache
def onlyqs(n, s, k):
    if n < s + k - 1:
        return 0
    
    n = n - (s + k - 1) + 1
    return comb(n+(k-1),k)

# def onlyqs_manual(n, cts):
#     # print(n,cts)
#     if len(cts) == 1:
#         if n >= cts[0]:
#             # print(f"returning {n-cts[0]+1}")
#             return n-cts[0]+1
#         else:
#             # print(f"returning 0")
#             return 0
#     c = cts[0]
#     s = 0
#     p = 0
#     while n - (p+c+1) >= 0:
#         # print(f"placing block {c} at {p}")
#         # print(f"recursive call with {n-(p+c+1)}")
#         s += onlyqs_manual(n-(p+c+1),cts[1:])
#         p += 1
#     # print(f"returning {s}")
#     return s

# print(onlyqs_manual(16,[1,1,1,2,1]))
# cts = [2,3,2,3,4]
# for i in range(100):
#     print(i, onlyqs_manual(i,cts), onlyqs(i,sum(cts),len(cts)))
    
# input()
# exit()

def arrangements(w, cts):
    if len(cts) == 0:
        if "#" in w:
            return 0
        else:
            return 1
    if all(c == "?" for c in w):
        return onlyqs(len(w),sum(cts),len(cts))
    
    if DEBUG: print(f"word: {w}")
    c = max(cts)
    i = cts.index(c)
    if DEBUG: print(f"blocks to be placed: {cts}, largest: {c}")
    r = places(w,c)
    if DEBUG: print(f"possible places: {r}")

    if DEBUG: input()
    res = 0
    for p in r:
        if DEBUG: print(f"====\ntrying to place {c} blocks at {p} in {w}")
        leftcts = cts[:i]
        rightcts = cts[i+1:]
        if p > 1:
            leftw = w[:p-1]
        else:
            leftw = ""
        if p + c + 1 < len(w):
            rightw = w[p+c+1:]
        else:
            rightw = ""
        if DEBUG: print(f"LEFT")
        resl = arrangements(leftw, leftcts)
        if DEBUG: print(f"Left result: {resl}")
        if DEBUG: print(f"RIGHT")
        if resl != 0:
            resr = arrangements(rightw, rightcts)
            if DEBUG: print(f"Right result: {resr}")
        else:
            resr = 0
        res += resl * resr
    return res

for i, l in enumerate(ls):
    w, ctsraw = l.split(" ")
    cts = [int(n) for n in ctsraw.split(",")]
    
    r = arrangements(w,cts)

    r2 = arrangements(w + "?" + w, cts + cts)

    print(i, w, cts)

    # r5 = arrangements(w + "?" + w + "?" + w + "?" + w + "?" + w, cts + cts + cts + cts + cts)
    # print(f"once: {r}")
    # print(f"twice: {r2}")
    # # print(r, r2, r2//r)
    if abs((r2 / r) - r2 // r) < 0.00000001:
        r5 = r * ((r2//r) ** 4)
    else:
        # print(r2/r, r2//r)
        r5 = arrangements(w + "?" + w + "?" + w + "?" + w + "?" + w, cts + cts + cts + cts + cts)

    # print(f"five: {r5}")
    print(r5)
    answer += r5
    # print(i, r)

    
expected = None
report(filename, [answer], [expected])
