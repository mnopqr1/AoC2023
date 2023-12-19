from itertools import product

filename = "test.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
cx, cy = 0, 0
pts = [(0,0)]
down = set()
up = set()
for l in ls:
    _, _, code = l.rstrip().split(" ")
    d = int(code[-2])
    s = int(code[2:-2],16)
    assert s >= 4
    dx,dy = DIRS[d]
    ex = cx + s * dx
    ey = cy + s * dy
    if d == 1:
        down.add((cx,cy,ex,ey))
    if d == 3:
        up.add((cx,cy,ex,ey))
    pts.append((ex,ey))
    cx, cy = ex, ey

# xmin = min(p[0] for p in grid)-1
# xmax = max(p[0] for p in grid)+1
# ymin = min(p[1] for p in grid)-1
# ymax = max(p[1] for p in grid)+1

xs = list(set(p[0] for p in pts))
ys = list(set(p[1] for p in pts))
xs.sort()
ys.sort()

# for x in xs:
#     print(x)
# for y in ys:
#     print(y)
exit()
inner = 0
# filled_grid = set()
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
                # filled_grid.add((x,y))
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
                # filled_grid.add((x,y))
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