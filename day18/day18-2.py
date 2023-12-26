filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
cx, cy = 0, 0
pts = [(0,0)]

for l in ls:
    _, _, code = l.rstrip().split(" ")
    d = int(code[-2])
    s = int(code[2:-2],16)
    dx, dy = DIRS[d]
    ex = cx + s * dx
    ey = cy + s * dy
    pts.append((ex,ey))
    cx, cy = ex, ey

assert pts[0] == pts[-1]

# https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon
def area(pts):
    n = len(pts)
    res = 0
    for i in range(n-1):
        x0, y0 = pts[i]
        x1, y1 = pts[i+1]
        res += x0 * y1 - x1 * y0
    return abs(res) // 2

def perimeter(pts):
    res = 0
    n = len(pts)
    for i in range(n-1):
        x0, y0 = pts[i]
        x1, y1 = pts[i+1]
        if x0 == x1:
            res += abs(y1 - y0) 
        elif y0 == y1:
            res += abs(x1 - x0) 
        else:
            assert False, "line segment not straight"
    return res

a = area(pts)
p = perimeter(pts)

# obtained the following by experimenting with the test input...
answer = a + (p//2) + 1

assert answer == 71262565063800
