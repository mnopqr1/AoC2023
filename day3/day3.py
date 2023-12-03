from itertools import product

def issymbol(x):
    return x != '.' and not x.isdigit()

def parse(ls):
    L = len(ls)
    i = 0
    g = [[0 for _ in range(L)] for _ in range(L)]
    while i < L:
        j = 0
        while j < L:
            if ls[i][j].isdigit():
                n = ""
                j0 = j
                while j < L and ls[i][j].isdigit():
                    n += ls[i][j]
                    j += 1
                for y in range(j0,j):
                    g[i][y] = int(n)
            else:
                j += 1
        i += 1
    return g, L

def has_symbol_around(ls, L, i, j):
    for di, dj in product([-1,0,1], [-1,0,1]):
        if (di,dj) != (0,0) and (0 <= i + di < L) and (0 <= j + dj < L):
            if issymbol(ls[i+di][j+dj]):
                return True
    return False

def solve1(ls,g,L):
    s = 0
    i = 0
    while i < L:
        j = 0
        while j < L:
            if g[i][j] != 0 and has_symbol_around(ls, L, i, j):
                s += g[i][j]
                while ls[i][j].isdigit():
                    j += 1
            else:
                j += 1
        i += 1
    return s

def numbers_around(g, L, i, j):
    ns = []
    for di, dj in product([-1,0,1], [-1,0,1]):
        if (di,dj) != (0,0) and (0 <= i + di < L) and (0 <= j + dj < L):
        # NB: this only works because we never have the same number around * in two different spots
            if g[i+di][j+dj] != 0 and g[i+di][j+dj] not in ns:
                ns.append(g[i+di][j+dj])
    return ns

def solve2(ls,g,L):
    s = 0
    for i, j in product(range(L),range(L)):
        if ls[i][j] == "*":
            ns = numbers_around(g, L, i, j)
            if len(ns) == 2:
                s += ns[0] * ns[1]
    return s

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()

    g, L = parse(ls)
    s = [solve1(ls, g, L), solve2(ls, g, L)]

    for p, x in enumerate(s):
        print(f"File {filename}, part {p+1}, answer: {x}", end="")
        if expected is not None:
            print(f", expected answer: {expected[p]}, ", end="")
            if expected[p] == x: print("CORRECT")
            else: print("WRONG")
        else:
            print()


if __name__ == "__main__":
    solve("test.txt", [4361,467835])
    solve("input.txt")
