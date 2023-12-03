
def numbers_around(ls, g, i, j):
    ns = []
    L = len(ls)
    if j > 1 and ls[i][j-1].isdigit(): 
        assert g[i][j-1] != 0
        ns.append(g[i][j-1])
    if j < len(ls) - 1 and ls[i][j+1].isdigit():
        assert g[i][j+1] != 0
        ns.append(g[i][j+1])
    otherrows = [x for x in [i-1,i+1] if x >= 0 and x < L]
    for x in otherrows:
        cols = [y for y in [j-1,j,j+1] if y >= 0 and y < L]
        ndigits = len([ls[x][y] for y in cols if ls[x][y].isdigit()])
        if ndigits == 3 or ndigits == 1:
            num = [g[x][y] for y in cols if g[x][y] != 0]

            # assert(len(num) == 1), f"i,j:{i},{j},num:{num}"
            ns.append(num[0])
        if ndigits == 2:
            if not ls[x][j].isdigit():
                ns.append(g[x][j-1])
                ns.append(g[x][j+1])
            else:
                ns.append(g[x][j])
    return ns


def printparsed(g,ls):
    L = len(ls)
    i = 0
    while i < L:
        j = 0
        while j < L:
            if g[i][j] != 0:
                print(g[i][j], end="")
                j += len(str(g[i][j]))
            else:
                print(ls[i][j], end="")
                j += 1
        print()
        i += 1