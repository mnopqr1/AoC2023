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
    return g

def has_symbol_around(ls, i, j):
    L = len(ls)
    neighbors = [(i+di,j+dj) for di in [-1,0,1] for dj in [-1,0,1] 
                 if (di!=0 or dj!=0) and (0 <= i + di < L) and (0 <= j + dj < L)]
    for (x,y) in neighbors:
        if issymbol(ls[x][y]):
            return True
    # print(f"No symbol around found at ({i},{j})")
    return False

def solve1(ls):
    s = 0
    L = len(ls)
    g = parse(ls)
    i = 0
    while i < L:
        j = 0
        while j < L:
            if g[i][j] != 0 and has_symbol_around(ls, i, j):
                s += g[i][j]
                while ls[i][j].isdigit():
                    j += 1
            else:
                j += 1
        i += 1
    return s

def numbers_around(g, i, j):
    ns = []
    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            if (di != 0 or dj != 0) and (0 <= i + di < len(g)) and (0 <= j + dj < len(g)):
                if g[i+di][j+dj] != 0:
                    if g[i+di][j+dj] not in ns:
                        ns.append(g[i+di][j+dj])
    return ns

def solve2(ls):
    s = 0
    L = len(ls)
    g = parse(ls)
    for i in range(L):
        for j in range(L):
            if ls[i][j] == "*":
                ns = numbers_around(g, i,j)
                if len(ns) == 2:
                    s += ns[0] * ns[1]
    return s
    
def solve(filename, part, expected=None):
    with open(filename) as f:
        ls = f.readlines()

    if part == 1:    
        s = solve1(ls)
    if part == 2:
        s = solve2(ls)

    if expected is not None:
        assert s == expected, f"File {filename}, part {part}, found {s}, expected {expected}"
    else:
        print(f"File {filename}, part {part}, answer: {s}")
    

if __name__ == "__main__":
    solve("./day3/test.txt", 1, 4361)
    solve("./day3/test.txt", 2, 467835)
    solve("./day3/input.txt", 1)
    solve("./day3/input.txt", 2)