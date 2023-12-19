filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

s = ls.index("")
ws_raw = ls[:s]
ms_raw = ls[s+1:]
ws = dict()

for w in ws_raw:
    name_end = w.find("{")
    name, rest = w[:name_end], w[name_end:]
    ws[name] = rest

def unfold_once(s):
    p = 0
    res = ""
    while (p < len(s)):
        res += s[p]
        if s[p] == ":" and s[p+1] != "{":
            n = ""
            p += 1
            while p < len(s) and (s[p] != ","):
                n += s[p]
                p += 1
            if n in ["A","R"]:
                res += n
            else:
                res += ws[n]
            if p < len(s) - 1:
                res += ","
        if s[p] == "}":
            n = ""
            while s[p] != ",":
                p -= 1
                n = s[p] + n
            res = res[:-len(n)]
            n = n[1:]
            if n in ["A","R"]:
                res += n
            else:
                res += ws[n]
            p += len(n)+1
        p += 1
    return res
            

max_level = 2
res = ws["in"]
for _ in range(max_level):
    print(len(res))
    res = unfold_once(res)
print(res)

exit()
vals = {"x": set(), "m": set(), "a": set(), "s": set()}
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
            vals[var].add(val)
    ws[name] = insts

varname = {"x" : 0, "m": 1, "a": 2, "s": 3}

answer = 0

n = 1
for v in "xmas":
    n *= (len(vals[v]))
print(n)

# for m in ms:
#     p = "in"
#     while p not in ["A","R"]:
#         prog = ws[p]
#         c = 0
#         found = False
#         while c < len(prog) - 1 and not found:
#             var, op, val, dest = prog[c]
#             assert op == ">" or op == "<"
#             if op == ">":
#                 if m[varname[var]] > val:
#                     found = True
#                     p = dest
#             if op == "<":
#                 if m[varname[var]] < val:
#                     found = True
#                     p = dest
#             c += 1
#         if not found:
#             assert prog[c][0] == "catch"
#             p = prog[c][1]
#     if p == "A":
#         answer += sum(m)

print(answer)