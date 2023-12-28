from dataclasses import dataclass

# this solution closely follows
# https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kersplf/

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

@dataclass
class Vec:
    x: int
    y: int
    z: int

def dot(v,w):
    return v.x * w.x + v.y * w.y + v.z * w.z

def independent(v,w):
    return dot(v,w) != 0 

def cross(v,w):
    return Vec(v.y*w.z - w.y*v.z, -v.x*w.z + v.z*w.x, v.x*w.y - v.y*w.x)

def minus(v,w):
    return Vec(v.x-w.x,v.y-w.y,v.z-w.z)

def plane(p1,v1,p2,v2):
    a = minus(p1,p2)
    b = minus(v1,v2)
    return (cross(a,b),dot(a,cross(v1,v2)))

def scale(r, v):
    return Vec(r * v.x, r * v.y, r * v.z)

def invscale(r, v):
    assert v.x % r == 0 and v.y % r == 0 and v.z % r == 0
    return Vec(v.x // r, v.y // r, v.z // r)

def add2(v1,v2):
    return Vec(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

def add3(v1,v2,v3):
    return add2(add2(v1, v2), v3)

def intersect(p,u,q,v):
    w = cross(u,v)
    a = dot(w,cross(q,v))
    b = -dot(w,cross(p,u))
    c = dot(p,w)
    return invscale(dot(w,w), add3(scale(a,u),scale(b,v),scale(c,w)))

def main():
    stones = []
    for l in ls:
        p,v = l.split(" @ ")    
        x,y,z = map(int,p.split(", "))
        dx,dy,dz = map(int,v.split(", "))
        stones.append((Vec(x,y,z),Vec(dx,dy,dz)))

    # we only use the first three stones
    p1,v1 = stones[0]
    p2,v2 = stones[1]
    p3,v3 = stones[2]

    # we check that they are giving new information
    assert independent(p1,p2) and independent(p1,p3) and independent(p2,p3)
    assert independent(v1,v2) and independent(v1,v3) and independent(v2,v3)

    # we find the velocity vector w by intersecting three planes
    a, A = plane(p1,v1,p2,v2)
    b, B = plane(p1,v1,p3,v3)
    c, C = plane(p2,v2,p3,v3)

    v = add3(scale(A,cross(b,c)),scale(B,cross(c,a)),scale(C,cross(a,b)))
    w = invscale(dot(a, cross(b,c)), v)

    # we now find the starting point by finding the intersection of the lines
    # p1 + (v1-w) t and p2 + (v2-w) t

    w1 = minus(v1,w)
    w2 = minus(v2,w)
    p = intersect(p1,w1,p2,w2)

    print(p.x+p.y+p.z)

if __name__ == "__main__":
    main()