from functools import cache
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

# m, M = 7, 27
m = 200000000000000
M = 400000000000000

stones = []
for l in ls:
    p,v = l.split(" @ ")    
    x,y,z = map(int,p.split(", "))
    dx,dy,dz = map(int,v.split(", "))
    stones.append(((x,y,z),(dx,dy,dz)))

@cache
def slope_offset(x,y,dx,dy):
    assert dx != 0
    slope = dy/dx
    offset = y - slope * x
    return (slope, offset)

def future(x,y,dx,dy,ix,iy):
    t = (ix - x) / dx
    # assert round(y + dy * t,5) == iy
    return t >= 0

def intersect(a, b):
    ((xa,ya,_),(dxa,dya,_)) = a
    ((xb,yb,_),(dxb,dyb,_)) = b

    assert xa != xb or ya != yb
    print(f"Hailstone A: {xa}, {ya} @ {dxa}, {dya}")
    print(f"Hailstone B: {xb}, {yb} @ {dxb}, {dyb}")

    sa, oa = slope_offset(xa,ya,dxa,dya)
    sb, ob = slope_offset(xb,yb,dxb,dyb)

    if sa != sb:
        ix = round((ob-oa) / (sa-sb),5)
        iy = round(sa * ix + oa,5)
        # assert iy == round(sb * ix + ob,5), f"{iy=} is not {sb *ix + ob=}"
        
        if future(xa,ya,dxa,dya,ix,iy) and future(xb,yb,dxb,dyb,ix,iy):
            # print(f"Intersection in future of both points.")
            print(f"Intersection at ({ix}, {iy})")
            return (ix,iy)
        else:
            print(f"Intersection not in future of both.")
    else:
        print(f"Parallel, never intersect.")
    return None, None

n = len(stones)

def in_region(x,y,m,M):
    return m <= x <= M and m <= y <= M

answer = 0
for i in range(n):
    for j in range(i+1,n):
        (x,y) = intersect(stones[i],stones[j])
        if x is not None and in_region(x, y, m, M):
            print(f"In test region.")
            answer += 1

print(answer)