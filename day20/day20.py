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
        # print(f"{self.name} handles {p}")
        newps = []
        tosend = False
        if self.ty == "b":
            sendval = p.value
            tosend = True
            
        if self.ty == "%":
            if p.value == False:
                self.state = not self.state
                sendval = self.state
                tosend = True
        
        if self.ty == "&":
            self.mem[p.cur] = p.value
            sendval = not all(self.mem[n] for n in self.ins)
            tosend = True

        if tosend:
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

    def __repr__(self):
        return f"({self.n=}, {self.value=}, {self.cur=}, {self.tow=})"


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
    # print(name)    

for n in module.keys():
    for d in module[n].ds:
        module[d].ins.append(n)
        module[d].mem[n] = False

done = False
n_presses = 0

D = False
D2 = False

ddins = module["dd"].ins
firsttime = {d: None for d in ddins}
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
            # if q.tow == "rx" and q.value == False:
            #     done = True
            # if D2:
            if q.tow == "dd" and q.value == True and firsttime[q.cur] is None:
                # print(f"{q.cur} sends high to dd at button press {n_presses}")
                firsttime[q.cur] = n_presses
        stack += newps
    done = all(firsttime[d] is not None for d in firsttime.keys())

# print(Pulse.n_low * Pulse.n_high)
print(reduce(lambda x,y: x*y,firsttime.values()))