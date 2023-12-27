filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
cx, cy = 0, 0
perim, area = 0, 0

for l in ls:
    _, _, code = l.rstrip().split(" ")
    d = int(code[-2])
    s = int(code[2:-2],16)
    dx, dy = DIRS[d]
    ex = cx + s * dx
    ey = cy + s * dy
    perim += s
    area += cx * ey - ex * cy
    cx, cy = ex, ey

answer = abs(area//2) + (perim//2) + 1

assert answer == 71262565063800
