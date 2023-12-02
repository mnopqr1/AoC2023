def parse(l):
    name, content = l.split(":")
    i = int(name.split(" ")[1])
    g = []    
    for s in content.split(";"):
        v = {"red": 0, "green": 0, "blue": 0}
        for item in s.split(","):
            item = item[1:]
            n, col = item.split(" ")
            col = col.rstrip()
            assert v[col] == 0
            v[col] = int(n)
        g.append(v)
    return i, g

def possible(g):
    return all(v["red"]<=12 and v["green"]<=13 and v["blue"]<=14 for v in g)

def part1(gs):
    total = 0
    for i,g in gs:
        if possible(g):
            total += i
    return total

def part2(gs):
    total = 0
    for _, g in gs:
        p = max(v["red"] for v in g) * max(v["blue"] for v in g) * max(v["green"] for v in g)
        total += p
    return total

if __name__ == "__main__":
    with open("./day2/input.txt") as f:
        ls = f.readlines()
    gs = []
    for l in ls:
        i, g = parse(l)
        gs.append((i,g))
    print(part1(gs))
    print(part2(gs))