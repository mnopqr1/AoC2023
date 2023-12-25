from functools import cache
from itertools import product

filename = "test.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]


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


# p + tv has to intersect with (pi + tvi) for all i, at t >= 0
# (a + td, b + te, c + tf) = (x + tdx, y + tdy, z + tdz) has to have a solution in t
# all to one side
# a - x + t(d-dx) = 0
# b - y + t(e-dy) = 0
# c - z + t(f-dz) = 0
# if there is a solution t then, for every (x,y,z,dx,dy,dz) stone:
# (a-x)(e-dy)(f-dz) = (b-y)(d-dx)(f-dz) = (c-z)(d-dx)(e-dy)
# (a-x')(e-dy')(f-dz') = (b-y')(d-dx')(f-dz')=(c-z')(d-dx')(e-dy')

# there has to exist t >= 0 such that
# a + d t = x + dx t
# the solution of this equation is
# t = (x-a) / (d - dx) IF d != dx (otherwise no solution)
# this is > 0 iff x - a and d - dx have the same sign.
# but we want to simultaenously satisfy the y and z equations.

# imagine one of the stones is (0,0,0,0,0,1)
# so at time t it's at (0,0,t)
# this means that the rock we throw must cross the (0,0,z) plane at time t.
# our rock crosses the (0,0,z) plane when? a + td = 0 and b + te = 0 so t = -a/d = -b/e
# it only crosses that plane IF ae - bd = 0, otherwise it just doesn't. And we want -a/d >= 0 so
# a/d <= 0.
# for example if we start at (-1,-2,z) and v = (3,6,vz) then the rock is at (-1 + 3t, -2 + 6t, z+vz t)
# at time t so at t = 1/3 we're in z + 1/3 vz and this should be equal to 1/3.



# if one stone is (x,y,z,dx,dy,dz)
# then at time t it's at (x + dx t, y + dy t, z + dz t).
# the rock we throw is (a,b,c,d,e,f)
# we want that x + dx t = a + d t and y + dy t = b + e t have a simultaneous solution of t.
# for this, we need that t0 = (x - a)/(d - dx) = (y - b)/(e - dy) >= 0, giving some constraints
# on a,b,d,e
# given these constraints we want that c + t0 f = z + dz t also giving some constraints on c and f.

def show_constraint(x,y,z,dx,dy,dz):
    print(f"({x} - rx)(rdy - {dy}) = ({y} - ry)(rdx - {dx})")
    print(f"rx = {x} - ({y} - ry)(rdx - {dx})/(rdy - {dy})")

    print(f"({x} - rx)(rdx - {dx}) >= 0")

for (p,v) in stones:
    x,y,z = p
    dx,dy,dz = v
    show_constraint(x,y,z,dx,dy,dz)
answer = 0


print(answer)

# if we throw the rock in direction (0,0,1) from point (0,0,0)
# then at time t >= 0 it's at (0,0,t)
# so we need that all other rocks have a positive t-solution to
# x + dx t = 0
# y + dy t = 0
# z + dz t = t
#
# so t = -x / dx = -y / dy
# and z -(x dz)/dx = -x / dx => z dx - x (dz - 1) = 0

# if we throw the rock in direction (da,db,dc) from point (a,b,c)
# then at time t >= 0 it's at (a,b,c+t)
# so we need that all other rocks have a positive t-solution to
# (dx - da) t + (x-a) = 0
# (dy - db) t + (y-b) = 0
# (dz - dc) t + (z-c) = 0
#
# this means that the determinant of each of the matrices is zero
# 

