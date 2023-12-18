from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

DIRS = {"R": (0,1), "D": (1,0), "L": (0,-1), "U": (-1,0) }
cx, cy = 0, 0
grid = set()
down = set()
up = set()
for l in ls:
    d, s, _ = l.rstrip().split(" ")
    s = int(s)
    dx,dy = DIRS[d]
    if d == "D":
        down.add((cx,cy))
    if d == "U":
        up.add((cx,cy))
    for i in range(s):
        cx += dx
        cy += dy
        grid.add((cx,cy))
        if d == "D":
            down.add((cx,cy))
        if d == "U":
            up.add((cx,cy))

xmin = min(p[0] for p in grid)-1
xmax = max(p[0] for p in grid)+1
ymin = min(p[1] for p in grid)-1
ymax = max(p[1] for p in grid)+1

inner = 0
filled_grid = set()
for x in range(xmin,xmax):
    # print(f"{x=}")
    s = 0
    y = ymin

    while y < ymax:
        if (x,y) in grid:
            cs = 0
            cs -= int((x,y) in down)
            cs += int((x,y) in up)
            while (x,y) in grid:
                inner += 1
                filled_grid.add((x,y))
                y += 1
                cs -= int((x,y) in down)
                cs += int((x,y) in up)
            if cs > 0:
                s += 1
            if cs < 0:
                s -= 1
        else:
            if s % 2 == 1:
                inner += 1
                filled_grid.add((x,y))
            y += 1  

def show(g,borders=False):
    for x in range(xmin,xmax):
        for y in range(ymin,ymax):
            if (x,y) in g:
                if borders:
                    if (x,y) in up:
                        print("+", end="")
                    elif (x,y) in down:
                        print("-", end="")
                    else:
                        print("#", end="")
                else:
                    print("#", end="")
            else:
                print(".", end="")
        print()

# show(grid,True)
# print()
# show(filled_grid)
print(inner)