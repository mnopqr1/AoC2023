from itertools import product

# for debugging
def showgrid(grid,h,w,hx=None,hy=None):
    for x,y in product(range(h), range(w)):
        if (x,y) == (hx,hy): print("!", end="")
        else: print(grid[(x,y)], end="")
        if y == w - 1: print()
