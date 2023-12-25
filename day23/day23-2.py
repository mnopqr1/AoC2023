from itertools import product

filename = "test.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

H, W = len(ls), len(ls[0])
grid = {(x,y) : ls[x][y] for (x,y) in product(range(H),range(W))}
neighbors = dict()

for (x,y) in product(range(H),range(W)):
    if grid[(x,y)] == "#":
        neighbors[(x,y)] = []
        continue

    neighbors[(x,y)] = []

    for (dx,dy) in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if grid[(nx,ny)] != "#":
                neighbors[(x,y)].append((nx,ny))


def show(c,h):
    cx,cy = c
    for (x,y) in product(range(H),range(W)):
        if (x,y) in h:
            print("X", end="")
        elif (x,y) == (cx,cy):
            print("!", end="")
        else:
            print(grid[(x,y)], end="")
        if y == W-1:
            print()



sx = 0
sy = ls[0].find(".")
ex = H-1
ey = ls[H-1].find(".")


# can_reach_end = {(ex,ey)}
# done = False
# queue = [(ex,ey)]
# while len(queue) > 0:
#     n = queue.pop(0)
#     for p in neighbors[n]:
#         if p not in can_reach_end:
#             queue.append(p)
#             can_reach_end.add(p)

# print(len(can_reach_end)) # 9406
# #how many have more than 2 neighbors? 34
# print(len([(x,y) for (x,y) in can_reach_end if len(neighbors[(x,y)]) > 2]))

# walk backwards from end, every time I see a node that has more than two
# neighbors, record length of best path

longest_to_end = {(ex,ey) : 0}
crucial = []
queue = [(ex-1,ey)]
prev = (ex,ey)
while len(queue) > 0:
    n = queue.pop(0)
    if n == (sx,sy):
        longest_to_end[n] = longest_to_end[(sx+1,sy)] + 1
        break
    while len(neighbors[n]) == 2:
        p, q = neighbors[n]
        if p in longest_to_end:
            q,p = p,q
        longest_to_end[n] = longest_to_end[q] + 1
        prev = n
        n = p
    longest_to_end[n] = longest_to_end[prev] + 1
    crucial.append(n)
    queue += neighbors[n]
    print(longest_to_end)
    print(queue)
    show(n,longest_to_end.keys())
    input()

# print(longest_to_end[(sx,sy)])
# answer = longest()
# if part1:
    # assert answer == 2438
# print(answer)