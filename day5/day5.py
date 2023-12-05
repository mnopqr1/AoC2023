from utils import *

def parse(ls):
    ls.append("")
    seeds = [int(s) for s in ls[0].split(":")[1][1:].split(" ")]
    l = 3
    maps = [0] * 7
    for m in range(0, 7):
        maps[m] = [] 
        while True:
            parts = ls[l].split()
            if len(parts) < 3: break
            d, s, r = [int(n) for n in parts]
            maps[m].append((d,s,r))
            l += 1
        l += 2
    return seeds, maps

def intersect(s1, l1, s2, l2):
    if s2 < s1: return intersect(s2, l2, s1, l1)
    if s1 + l1 <= s2: return None, None
    else: return s2, min(s1+l1-s2, l2)

def minus(s1,l1,s2,l2):
    if s1 + l1 <= s2 or s2 + l2 <= s1: return [(s1, l1)]
    result = []
    if s1 < s2: result.append((s1, s2-s1))
    if s2 + l2 < s1 + l1: result.append((s2+l2, (s1+l1) - (s2+l2)))
    return result

def union_minus(intervals,s1,l1):
    result = []
    for (s0,l0) in intervals:
        result += minus(s0,l0,s1,l1)
    return result

def apply_map(ranges,d,s,r):
    result = []
    for (b,l) in ranges:
        inters, interl = intersect(b,l,s,r)
        if inters is not None:
            newdest = inters + (d-s)
            result.append((newdest,interl))
    return result

def plant(ranges, maps):
    for m in range(0, 7):
        newranges = []
        remaining = ranges
        for (d, s, r) in maps[m]:
            newranges += apply_map(ranges, d, s, r)
            remaining = union_minus(remaining, s, r)
        ranges = newranges + remaining
    return ranges

def solve1(seeds, maps):
    ranges = [(seeds[i],1) for i in range(len(seeds))]
    locations = plant(ranges, maps)
    return min(i[0] for i in locations)

def solve2(seeds, maps):
    ranges = [(seeds[i], seeds[i+1]) for i in range(0,len(seeds),2)]
    locations = plant(ranges, maps)
    return min(i[0] for i in locations)

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    seeds, maps = parse(ls)
    s = [solve1(seeds, maps), solve2(seeds, maps)]
    report(filename, s, expected)

if __name__ == "__main__":
    solve("test.txt", [35,46])
    solve("input.txt")
