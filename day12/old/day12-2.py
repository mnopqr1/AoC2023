import os
from utils import *
from itertools import product

filename = "test.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

DEBUG = True

def nmatches(w, goal, p, q):
    if DEBUG:
        os.system("clear")
        print(f"{w}")
        print(" " * p + "^")
        print(f"{goal}")
        print(" " * q + "^")
        print(p, q)
        input()
    if p == len(w):
        if q == len(goal):
            if DEBUG: input("SUCCESS")
            return 1
        if goal[q] == "$":
            if DEBUG: input("SUCCESS")
            return 1
        else:
            return 0
    elif q == len(goal):
        return 0
    
    if goal[q] == "^":
        while p < len(w) and w[p] == ".":
            p += 1
        return nmatches(w,goal,p,q+1)
    if goal[q] == "$":
        while p < len(w) and w[p] == ".":
            p += 1
        if p == len(w):
            if DEBUG: input("SUCCESS")
            return 1
        else:
            return 0
    if goal[q] == "#":
        if w[p] == "#":
            return nmatches(w,goal,p+1,q+1)
        elif w[p] == "?":
            new1 = w[:p] + "#" + w[p+1:]
            r1 = nmatches(new1,goal,p+1,q+1)
            new2 = w[:p] + "." + w[p+1:]
            r2 = nmatches(new2, goal,p+1,q)
            return r1+r2
        else:
            return 0
    if goal[q] == "+":
        if w[p] == "#":
            return 0
        else:
            st = p
            while p < len(w) and w[p] == ".":
                p += 1
            new = w[:st] + "." * (p-st)
            if w[p] == "#":
                new = new + w[p:]
                return nmatches(new,goal,p+1,q+1)
            elif w[p] == "?":
                new1 = new + "#" + w[p+1:]
                r1 = nmatches(new1,goal,p+1,q+1)
                new2 = new + "." + w[p+1:]
                r2 = nmatches(new2, goal,p+1,q)
            return r1+r2
def arrangements(w, cts):
    print(w,cts)
    goal = "^"
    for i in range(len(cts)):
        goal += "#" * cts[i]
        if i != len(cts) - 1:
            goal += "+"
    goal += "$"
    return nmatches(w,goal,0,0)

def solve(ls):
    answer = 0
    for i, l in enumerate(ls):
        w, ctsraw = l.split(" ")
        cts = [int(n) for n in ctsraw.split(",")]
        wexp = w + "?" + w + "?" + w + "?" + w + "?" + w
        ctsexp = []
        for _ in range(5):
            for x in cts:
                ctsexp.append(x)
        r = arrangements(w,cts)
        answer += r
        print(r)
    return answer


# assert arrangements(".#..?#?.###", [1,2,3]) == 2

answer = 0
# answer = solve(ls)

# print(arrangements("?#?#?#?#?#?#?#?", [1,3,1,6]))
print(arrangements("????.######..#####.", [1, 6, 5]))

expected = None
report(filename, [answer], [expected])
