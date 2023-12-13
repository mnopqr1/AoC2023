import os
from utils import *

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]


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

def show(p,bp,c):
    print(w)
    print(" " * p + c)
    print(cts)
    print(f"currently reading: {bp+1}nd block")

mem = {}
D = False
def f(p,bp,c):
    key = (p,bp,c)
    if D:
        input()
        os.system("clear")
        show(p,bp,c)
    
    if key in mem:
        return mem[key]
    if p >= len(w):
        mem[key] = 1 if bp >= len(cts) else 0
        if D: print(f"beyond end of word, returning {mem[key]}")
        # if D: input()
        return mem[key]
    if c == ".":
        if p == len(w) - 1:
            mem[key] = 1 if bp >= len(cts) else 0
            if D: print(f"end of word, return {mem[key]}")
        else:
            mem[key] = f(p+1,bp,w[p+1])
        return mem[key]
    if c == "#":
        i = 1
        while p+i < len(w) and i < cts[bp] and (w[p+i] == "#" or w[p+i] == "?"):
            i += 1
        if i < cts[bp]: 
            if D: print(f"could not read all #s of this block")
            mem[key] = 0
        elif p + i < len(w) and w[p+i] == "#":
            if D: print(f"block of # was too long")
            mem[key] = 0
        elif p + i == len(w):
            mem[key] = 1 if bp + 1 == len(cts) else 0
            if D: print(f"read successfully and reached end of word, return {mem[key]}")
        elif p + i + 1 == len(w):
            mem[key] = 1 if bp + 1 == len(cts) else 0
            if D: print(f"read successfully and can't read any more, almost at end, return {mem[key]}")
        else:
            if D: print(f"read successfully and did not reach end of word")
            if bp + 1 == len(cts):
                if "#" in w[p+i+1:]:
                    if D: print(f"found loose #, return 0")
                    mem[key] = 0
                else:
                    if D: print(f"read last block successfully, return 1")
                    mem[key] = 1
            else: 
                mem[key] = f(p+i+1,bp+1,w[p+i+1])
        return mem[key]
    if c == "?":
        mem[key] = f(p,bp,".") + f(p,bp,"#")
        return mem[key]


answer = 0

for i, l in enumerate(ls):
    w, ctsraw = l.split(" ")
    cts = [int(n) for n in ctsraw.split(",")]

    # # part 2
    # wrong: 4 (23, 7203), 7 (184756, ..)
    w = "?".join([w,w,w,w,w])
    cts = cts + cts + cts + cts + cts
    # w = "?".join([w,w])
    # cts = cts + cts
    wdeb = w
    # print(w, cts)
    r = f(0,0,w[0])
    if D: print(f"result received: {r}")
    mem.clear()
    answer += r
    print(i, r)

expected = None
report(filename, [answer], [expected])
