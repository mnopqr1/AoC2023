from collections import Counter
from utils import *

filename = "input.txt"


def shift(s):
    blocks = s.split("#")
    for i,b in enumerate(blocks):
        cts = Counter(b)
        blocks[i] = "O" * cts["O"] + "." * cts["."]
    r = "#".join(blocks)
    return r


def score(s):
    total = 0
    c = 0
    for c in range(len(s[0])):
        for r in range(len(s)):
            if s[r][c] == "O":
                total += len(s) - r
    return total


def tilt(grid,direction):
    if direction == "N":
        cols = ["".join(grid[i][j] for i in range(h)) for j in range(w)]
        cols_s = [shift(cols[i]) for i in range(len(grid))]
        return ["".join(cols_s[i][j] for i in range(h)) for j in range(w)]
    if direction == "W":
        return [shift(grid[i]) for i in range(len(grid))]
    if direction == "E":
        return [shift(grid[i][::-1])[::-1] for i in range(len(grid))]
    if direction == "S":
        cols = ["".join(grid[i][j] for i in range(h)) for j in range(w)]
        cols_s = [shift(cols[i][::-1]) for i in range(len(grid))]
        return ["".join(cols_s[i][w-1-j] for i in range(h)) for j in range(w)]


if __name__ == "__main__":
    with open(filename) as f:
        ls = [l.rstrip() for l in f.readlines()]
    h, w = len(ls), len(ls[0])
    grid = ls
    Nreal = 1_000_000_000
    N = 200 # enough to get a loop in the scores

    DIRS = ["N","W","S","E"]
    scores = []
    k = 0
    while k < 4 * N:
        d = DIRS[k % 4]
        grid = tilt(grid,d)
        if k % 4 == 3:
            s = score(grid)
            scores.append(s)
        k += 1

    # find beginning of loop
    b = [i for i in range(N) if scores[i] == scores[-1]][-2]
    modulus = N - b - 1
    r = (Nreal - b - 1)%modulus
    print(scores[b+r])
