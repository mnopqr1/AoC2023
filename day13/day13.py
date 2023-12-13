from utils import *
from itertools import product

filename = "input.txt"

def reflection(p):
    for i in range(1,len(p)):
        l,r = i-1,i
        while l >= 0 and r < len(p):
            if p[l] != p[r]:
                break
            l -= 1
            r += 1
        if l == -1 or r == len(p):
            return i
    return -1

def reflection2(p):
    for i in range(1,len(p)):
        l,r = i-1,i
        err = 0
        while l >= 0 and r < len(p):
            if p[l] != p[r]:
                if err > 0:
                    break
                else:
                    diff = len([i for i in range(len(p[l])) if p[l][i] != p[r][i]])
                    if diff == 1:
                        err = 1
                    else:
                        break
            l -= 1
            r += 1
        if (l == -1 or r == len(p)) and err == 1:
            return i
    return -1

def score(p,part2=False):
    h,w = len(p), len(p[0])
    
    r = reflection2(p) if part2 else reflection(p)
    if r != -1:
        return 100 * r
    cols = ["" for _ in range(w)]
    for i in range(h):
        for j in range(w):
            cols[j] += p[i][j]
    r = reflection2(cols) if part2 else reflection(cols)

    return r

if __name__ == "__main__":
    with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]

    i = 0
    c = 0
    answer = 0
    part2 = True
    while i < len(ls):
        p = []
        while i < len(ls) and ls[i] != "":
            p.append(ls[i])
            i += 1
        s = score(p,part2)
        if s == -1:
            print("error, did not find reflection for #", c, ":", p)
            exit()
        answer += s
        i += 1
        c += 1

    print(answer)
