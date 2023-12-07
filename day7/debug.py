
names = {0: "high card", 1: "one pair", 2: "two pairs", 3: "three of a kind", 4: "full house", 5: "four of a kind", 6: "five of a kind"}

def debug(ys):
    currscore = 0
    print(names[currscore])
    for y, _ in ys:
        if score2(y) > currscore:
            print("\n\n")
            print(names[currscore+1])
            print("---\n")
            currscore = score2(y)
        print(y, end=", ")
    print()