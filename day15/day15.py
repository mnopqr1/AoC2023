filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

cs = "".join(ls).split(",")

def hash(c):
    r = 0
    for i in c:
        r += ord(i)
        r = r * 17 % 256
    return r

answer1 = sum(hash(c) for c in cs)    

mem = {}
box = {p : [] for p in range(256)} 
for c in cs:
    if "-" in c:
        label = c[:-1]
        h = hash(label)
        if label in box[h]:
            j = box[h].index(label)
            box[h] = box[h][:j] + box[h][j+1:]
    else:
        label, val = c.split("=")
        h = hash(label)
        mem[label] = int(val)
        if label not in box[h]:
            box[h].append(label)

answer2 = sum((j+1)*(i+1)*mem[box[i][j]] for i in range(256) for j in range(len(box[i])))

print(answer1, answer2)