from typing import List, Dict, Tuple

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

s = ls.index("")
ws_raw = ls[:s]
ws = dict()

for w in ws_raw:
    name_end = w.find("{")
    name, rest = w[:name_end], w[name_end:]
    insts_raw = rest[1:-1].split(",")
    insts: List[Tuple[str,str,int,str]] = []
    for k, i in enumerate(insts_raw):
        if k == len(insts_raw) - 1:
            insts.append(("catch","", 0, i))
        else:
            comp, dest = i.split(":")
            var, op, val = comp[0], comp[1], comp[2:]
            ival: int = int(val)
            insts.append((var,op,ival,dest))
    ws[name] = insts

def ivsize(iv : Tuple[int,int]) -> int:
    return iv[1] - iv[0] + 1

def blocksize(b : List[Tuple[int,int]]) -> int:
    return ivsize(b[0]) * ivsize(b[1]) * ivsize(b[2]) * ivsize(b[3])

def rangesize(r : List[List[Tuple[int,int]]]) -> int:
    return sum(blocksize(b) for b in r)

def intersectiv(a: Tuple[int,int],b:Tuple[int,int]) -> Tuple[int,int]:
    return (max(a[0],b[0]), min(a[1],b[1]))

def intersectb_b(b: List[Tuple[int,int]], c: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    return [intersectiv(b[i], c[i]) for i in range(4)]  

def is_determined(n: str) -> bool:
    return all(i[3] in result.keys() for i in ws[n])

def cond_to_block(var, op, val):
    b = [(m,M) for _ in range(4)]
    b[varname[var]] = (m,val-1) if op == "<" else (val+1,M)
    return b

def neg_cond_to_block(var, op, val):
    b = [(m,M) for _ in range(4)]
    b[varname[var]] = (val,M) if op == "<" else (m,val)
    return b

def intersectr_b(ran: List[List[Tuple[int,int]]], bl: List[Tuple[int,int]]):
    return [intersectb_b(b,bl) for b in ran]

def intersectr_r(ran1: List[List[Tuple[int,int]]], ran2: List[List[Tuple[int,int]]]):
    return [b for c in ran2 for b in intersectr_b(ran1,c)]

def valid(b: List[Tuple[int,int]]) -> bool:
    return all(iv[0] <= iv[1] for iv in b)

def determine(n):    
    prog = ws[n]
    res = []
    remaining = [(m,M) for _ in range(4)]
    for inst in prog:
        var, op, val, dest = inst
        if var == "catch":
            if dest == "A":
                res += remaining
            elif dest != "R":
                res += intersectr_r(remaining, result[dest])
            continue
        block_c = cond_to_block(var, op, val)
        block_negc = neg_cond_to_block(var, op, val)
        rem_true = intersectr_r(result[dest],remaining)
        newblocks = intersectr_b(rem_true, block_c)
        res += newblocks
        remaining = intersectr_b(remaining, block_negc)
    result[n] = res
    return

m, M = 1, 4000
result : Dict[str,List[List[Tuple[int,int]]]] = dict()
result["A"] = [(m,M) for _ in range(4)]
result["R"] = []
varname = {"x" : 0, "m": 1, "a": 2, "s": 3}

while not "in" in result.keys():
    for name in ws.keys():
        if is_determined(name):
            determine(name) 

print(rangesize(result["in"]))

