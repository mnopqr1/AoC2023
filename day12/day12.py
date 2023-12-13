import os
from utils import *

def readdot(p, bp):
    if p == len(w) - 1: # end of word
        return 1 if bp >= len(cts) else 0
    else: # not end of word, recurse
        return arrangements(p+1,bp,w[p+1])

def readhash(p, bp):
    i = 1
    while p+i < len(w) and i < cts[bp] and (w[p+i] == "#" or w[p+i] == "?"):
        i += 1
    if i < cts[bp]: # could not read all #s of this block
        return 0
    elif p + i < len(w) and w[p+i] == "#": # block was too long
        return 0
    elif p + i == len(w) or p + i + 1 == len(w): # read this block successfully and reached end of word
        return 1 if bp + 1 == len(cts) else 0
    else: # read successfully and did not reach end of word
        if bp + 1 == len(cts):
            if "#" in w[p+i+1:]: # found loose # later in word
                return 0
            else: # read last block successfully and can put . everywhere after
                return 1
        else: # did not reach last block, recurse
            return arrangements(p+i+1,bp+1,w[p+i+1])

# number of ways to insert the blocks in cts[bp:] into w,
# if we start reading at p and replace the character at p (if it's a ?) by c
# cts and w are global variables 
def arrangements(p,bp,c):
    key = (p,bp,c)
    
    if key in mem: # cache hit
        return mem[key]
    
    if p >= len(w): # beyond end of word
        mem[key] = 1 if bp >= len(cts) else 0
        return mem[key]
    
    if c == ".":
        mem[key] = readdot(p,bp)
        return mem[key]
    
    if c == "#":
        mem[key] = readhash(p,bp)
        return mem[key]
    
    if c == "?": # try both . and # at this position, see what you get
        mem[key] = arrangements(p,bp,".") + arrangements(p,bp,"#")
        return mem[key]


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as file:
        ls = [l.rstrip() for l in file.readlines()]
    part2 = True

    answer = 0
    for i, l in enumerate(ls):
        w, ctsraw = l.split(" ")
        cts = [int(n) for n in ctsraw.split(",")]
        if part2:
            w = "?".join([w,w,w,w,w])
            cts = cts + cts + cts + cts + cts
        mem = {}
        r = arrangements(0,0,w[0])
        answer += r

    expected = 204640299929836 if part2 else 8270
    assert answer == expected
