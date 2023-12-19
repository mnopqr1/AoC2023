from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

s = ls.index("")
ws_raw = ls[:s]
ms_raw = ls[s+1:]
ws = dict()
start = -1
for j, w in enumerate(ws_raw):
    name, rest = w.split("{")
    insts_raw = rest[:-1].split(",")
    insts = []
    for k, i in enumerate(insts_raw):
        if k == len(insts_raw) - 1:
            insts.append(("catch",i))
        else:
            comp, dest = i.split(":")
            var, op, val = comp[0], comp[1], comp[2:]
            val = int(val)
            insts.append((var,op,val,dest))
    ws[name] = insts

ms = []
for m in ms_raw:
    xs = []
    vals = m[1:-1].split(",")
    for v in vals:
        xs.append(int(v[2:]))
    ms.append(xs)

varname = {"x" : 0, "m": 1, "a": 2, "s": 3}

answer = 0

for m in ms:
    p = "in"
    while p not in ["A","R"]:
        prog = ws[p]
        c = 0
        found = False
        while c < len(prog) - 1 and not found:
            var, op, val, dest = prog[c]
            assert op == ">" or op == "<"
            if op == ">":
                if m[varname[var]] > val:
                    found = True
                    p = dest
            if op == "<":
                if m[varname[var]] < val:
                    found = True
                    p = dest
            c += 1
        if not found:
            assert prog[c][0] == "catch"
            p = prog[c][1]
    if p == "A":
        answer += sum(m)

print(answer)