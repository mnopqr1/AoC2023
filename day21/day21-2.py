# based on solution linked here
# https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keao4q8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

h,w = len(ls), len(ls[0])
grid = {(i,j) : ls[i][j] for (i,j) in product(range(h),range(w))}

DIRS = [(1,0),(-1,0),(0,1),(0,-1)] 

def experiment(m, N):
    visited = {p for p in grid if grid[p] == "S"}
    results = []
    for i in range(m + 2 * N + 1):
        if i % N == m: 
            results.append(len(visited))
        newvisited = set()
        for p in visited:
            x,y = p
            for (dx,dy) in DIRS:
                newp = (x+dx, y+dy)
                newpmod = ((x+dx) % N, (y+dy) % N)
                if grid[newpmod] == "#": continue
                newvisited.add(newp)
        visited = newvisited
    return results

def quadratic_interp(x, y1, y2, y3):
    # given the values of a quadratic function at m, m + N, m + 2N,
    # compute its value at m + x * N
    return y1 + x * (y2 - y1) + x * (x-1) * (y3 - 2 * y2 + y1) // 2

r = 26501365
N = 131
q = r // N
m = r % N

results = experiment(m, N)
assert results == [3877, 34674, 96159]
answer = quadratic_interp(q, *results)
assert answer == 627960775905777
print(answer)
