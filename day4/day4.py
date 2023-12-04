from utils import *

def parse(ls):
    cs = [0] * len(ls)
    for i, l in enumerate(ls):
        w, h = l.rstrip().split(":")[1].split("|")
        wn = [int(n) for n in w.split()]
        hn = [int(n) for n in h.split()]
        cs[i] = (wn,hn)
    return cs

def n_wins(c):
    w,h = c
    return len(set(w).intersection(set(h))) 

def solve1(cs):
    return sum(2 ** (n_wins(c)-1) for c in cs if n_wins(c) != 0)

def solve2(cs):
    scores = {n+1: n_wins(c) for n,c in enumerate(cs)}
    counts = {n+1: 1 for n in range(len(cs))}
    for n in range(1,len(cs)+1):
        for k in range(1, scores[n]+1):
            if n + k <= len(cs):
                counts[n+k] += counts[n]
    return sum(counts[n] for n in counts.keys())

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    cs = parse(ls)
    s = [solve1(cs), solve2(cs)]
    
    report(filename, s, expected)
    
if __name__ == "__main__":
    solve("test.txt", [13,30])
    solve("input.txt")
