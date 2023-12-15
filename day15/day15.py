from utils import *

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

cs = "".join(ls).split(",")
answer = 0

def hash(c):
    r = 0
    for i in c:
        r += ord(i)
        r = r * 17 % 256
    return r

answer = sum(hash(c) for c in cs)

mem = {}
box = {p : [] for p in range(256)}
p = 0

def do(c):
    if "-" in c:
        label = c[:-1]
        h = hash(label)
        if label in box[h]:
            j = box[h].index(label)
            box[h] = box[h][:j] + box[h][j+1:]
    else:
        i = c.index("=")
        label, val = c[:i], c[i+1:]
        val = int(val)
        h = hash(label)
        mem[label] = val
        if label not in box[h]:
            box[h].append(label)
            
for c in cs:
    do(c)

answer = 0
for i in range(256):
    for j in range(len(box[i])):
        answer += (j+1) * (i+1) * mem[box[i][j]]
print(answer)