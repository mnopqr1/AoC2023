from typing import Dict, Tuple

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
DIRNAMES = "RDLU"
SYMBOL = {0: ".", 1: "#"}
cx, cy = 0, 0
pts = [(0,0)]
down = set()
up = set()
for l in ls:
    _, _, code = l.rstrip().split(" ")
    d = int(code[-2])
    s = int(code[2:-2],16)
    # assert s >= 4
    # print(DIRNAMES[d], s)
    dx, dy = DIRS[d]
    ex = cx + s * dx
    ey = cy + s * dy
    pts.append((ex,ey))
    cx, cy = ex, ey

class Picture:
    h: int
    w: int
    grid: Dict[int,Dict[int,int]]

    def __init__(self,h:int,w:int):
        self.h = h
        self.w = w
        self.grid = {x: {y: 0 for y in range(w)} for x in range(h)}

    def addpt(self, pt: Tuple[int,int]):
        x,y = pt
        if 0 <= x < self.h and 0 <= y < self.w:
            self.grid[x][y] = 1
        else:
            assert False, f"tried to add {x,y} but outside grid of size {self.h,self.w}"

    def addline(self, pt1, pt2):
        x1,y1 = pt1
        x2,y2 = pt2
        if x1 == x2:
            if y2 < y1: self.addline(pt2,pt1)
            else:
                for y in range(y1,y2+1):
                    self.addpt((x1,y))
        elif y1 == y2:
            if x2 < x1: self.addline(pt2,pt1)
            else:
                for x in range(x1,x2+1):
                    self.addpt((x,y1))
        else:
            assert False, f"tried to add diagonal line from {pt1} to {pt2}"
    def __repr__(self) -> str:
        return "\n".join("".join(SYMBOL[self.grid[x][y]] for y in range(self.w)) 
                         for x in range(self.h))


# draw the picture
res = 200

xmin, xmax = min(pt[0] for pt in pts), max(pt[0] for pt in pts)
ymin, ymax = min(pt[1] for pt in pts), max(pt[1] for pt in pts)
h = xmax - xmin
w = ymax - ymin
scale = max(h//res,w//res) + 1

xoff = -xmin 
yoff = -ymin 
pic = Picture(res,res)


def transx(x):
    return (x + xoff) // scale
def transy(y):
    return (y + yoff) // scale
scaledpts = [(transx(x),transy(y)) for (x,y) in pts]
for i in range(len(scaledpts)-1):
    p1 = scaledpts[i]
    p2 = scaledpts[i+1]
    pic.addline(p1,p2)

# cut up shape in rectangles
hlines = [pt[0] for pt in pts]
hlines.sort()
vlines = [pt[1] for pt in pts]
vlines.sort()

scaledhlines = [((transx(x),0), (transx(x),res-1)) for x in hlines]

scaledvlines = [((0,transy(y)), (res-1,transy(y))) for y in vlines]

# for l in scaledhlines:
#     pic.addline(*l)
# for l in scaledvlines:
#     pic.addline(*l)

# print(pic)

print(pic)

def area(pts):
    assert pts[0] == pts[-1]
    n = len(pts)
    res = 0
    for i in range(n-1):
        x0,y0 = pts[i]
        x1,y1 = pts[i+1]
        res += x0 * y1 - x1 * y0
    return 0.5 * abs(res)

def perimeter(pts):
    assert pts[0] == pts[-1]
    res = 0
    n = len(pts)
    for i in range(n-1):
        x0,y0 = pts[i]
        x1,y1 = pts[i+1]
        if x0 == x1:
            res += abs(y1-y0) 
        elif y0 == y1:
            res += abs(x1-x0) 
        else:
            assert False, "line segment not straight"
    return res
a = area(pts)
p = perimeter(pts)
print(a, p)
print(a+(p/2)+1)
