from dataclasses import dataclass
from functools import reduce
from typing import Dict, List


@dataclass
class Module:
    ty: str
    name: str
    ds: List[str]
    ins : List[str]
    mem : Dict[str,bool]
    state : bool

    def handle(self, p):
        assert self.name == p.tow
        newps = []
        if self.ty == "b":
            sendval = p.value
            
        if self.ty == "%":
            if p.value == False:
                self.state = not self.state
                sendval = self.state
        
        if self.ty == "&":
            self.mem[p.cur] = p.value
            sendval = not all(self.mem[n] for n in self.ins)

        if not(self.ty == "%" and p.value == True):
            for d in self.ds:
                newp = Pulse(sendval, self.name, d)
                newps.append(newp)
                if D: print(f"{self.name} sends {WORD[newp.value]} to {newp.tow}")

        return newps


class Pulse:
    n: int
    value: bool
    cur: str
    tow: str
    n_low = 0
    n_high = 0
    n_pulses = 0

    def __init__(self, value=False, cur="button", tow="roadcaster"):
        if value == True:
            Pulse.n_high += 1
        else:
            Pulse.n_low += 1
        Pulse.n_pulses += 1
        self.n = Pulse.n_pulses
        self.value = value
        self.cur = cur
        self.tow = tow

module = dict()

filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

WORD = {False: "low", True: "high"}

for l in ls:
    iden, dest = l.split(" -> ")
    ty, name = iden[0], iden[1:]
    ds = dest.split(", ")
    if name not in module.keys():
        module[name] = Module(ty,name,ds,[],{},False)
    else:
        module[name].ty = ty
        module[name].ds = ds
    for d in ds:
        if d not in module.keys():
            module[d] = Module(".",d,[],[],{},False)

for n in module.keys():
    for d in module[n].ds:
        module[d].ins.append(n)
        module[d].mem[n] = False


D = False
D2 = False

part2 = True
ddins = module["dd"].ins
firsttime = {d: None for d in ddins}

done = False
n_presses = 0
while not done:
    if D: print(f"------\npress button {n_presses+1}\n-----")
    n_presses += 1
    p = Pulse()
    stack = [p]

    while len(stack) > 0:
        p = stack.pop(0)
        handler = module[p.tow]
        newps = handler.handle(p)
        for q in newps:
            if q.tow == "dd" and q.value == True and firsttime[q.cur] is None:
                firsttime[q.cur] = n_presses
        stack += newps
    if part2:
        done = all(firsttime[d] is not None for d in firsttime.keys())
    else:
        done = n_presses == 1000

if part2: 
    print(firsttime)
    print(reduce(lambda x,y: x*y,firsttime.values()))
else:
    print(Pulse.n_low * Pulse.n_high)