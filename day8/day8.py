from collections import defaultdict
from math import lcm
from utils import *

def parse_rule(l):
    return (l[0:3], l[7:10], l[12:15])

def parse(ls):
    w = ls[0].rstrip()
    left = defaultdict()
    right = defaultdict()
    for l in ls[2:]:
        s, c1, c2 = parse_rule(l)
        left[s] = c1
        right[s] = c2
    return w, left, right

def solve1(w,left,right):
    nodes = left.keys()
    step = {n : n for n in nodes}
    for i in range(len(w)):
        for n in left.keys():
            if w[i] == "L":
                step[n] = left[step[n]]
            if w[i] == "R":
                step[n] = right[step[n]]
            assert w[i] == "L" or w[i] == "R"
    
    c = 0
    reached = "AAA"
    while reached != "ZZZ":
        reached = step[reached]
        # print(reached)
        c += 1
    return c * len(w)


def step(a,c, left, right):
    assert a == "L" or a == "R"
    if a == "L":
        return left[c]
    if a == "R":
        return right[c]

def solve2(w, left, right):
    nodes = left.keys()

    # after[i][n] is where n is after reading i characters of w
    after = [{n : n for n in nodes}]
    
    # in_end_node = {n : [] for n in nodes}
    # for n in nodes:
    #     if n[-2] == "Z":
    #         in_end_node[n].append(0)
    
    # in_end_node[n] is the list of times where you're in an end node 
    # if you started reading from n
    for i in range(0, len(w)):
        new = dict()
        for n in nodes:
            new[n] = step(w[i], after[i][n], left, right)
            # if new[n][-1] == "Z":
            #     in_end_node[n].append(i+1)
        after.append(new)

    times = {n : [0] for n in nodes if n[-1] == "Z"}
    t = 0
    curr = {n : n for n in nodes}
    while not all(n in times.keys() for n in nodes if n[-1] == "A"):
        for n in nodes:
            curr[n] = after[len(w)][curr[n]]
            if curr[n][-1] == "Z":
                if n not in times.keys():
                    times[n] = [t+1]
        t += 1
    
    r = 1
    for n in nodes:
        if n[-1] == "A":
            s = times[n][0]
            r = lcm(r,s)
            print(n, s)
    print(r*len(w))

    # for n in nodes:
    #     print(n)
    #     print(after[1][n])
    #     assert(in_end_node[n] == [] or in_end_node[n] == [307] or in_end_node[n] == [0]), f"{in_end_node[n]}"
    # we only ever end up in an end node after reading entire copies of w!!
    

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    w, left,right = parse(ls)
    # print(w,left,right)
    s = [solve2(w,left,right)]
    
    report(filename, s, expected)
    
if __name__ == "__main__":
    # solve("test3.txt", [6])
    solve("input.txt")


# we have two functions L : X -> X and R : X -> X
# we have a word w like LRLLLRLLLLLRRRLRLRLRRRL
# we read the word simultaneously from a set S of start nodes
# and we want to end up at the same time in a set F of end nodes
# 
# to know what w^k u with u a prefix of w does, we can just 
# compute the result of doing a prefix of w and then do w in batches
#
# we want to know, for every node x, how long it takes to 
# get to the same node with the reading head at the same position
# x w