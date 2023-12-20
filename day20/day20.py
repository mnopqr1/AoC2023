

from dataclasses import dataclass
from typing import Dict, List


filename = "input.txt"
with open(filename) as f:
    ls = [l.rstrip() for l in f.readlines()]

# False = low, True = high

@dataclass
class Module:
    ty: str
    name: str
    ds: List[str]
    ins : List[str]
    mem : Dict[str,bool]
    state : bool

    def handle(self, p):
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
        
        
        if tosend:
            for d in ds:
                newp = Pulse(sendval, d)
                newps.append(newp)


        return newps


class Pulse:
    n: int
    value: bool
    loc: str
    n_pulses = 0

    def __init__(self, value=False, loc="button"):
        Pulse.n_pulses += 1
        self.n = Pulse.n_pulses
        self.value = value
        self.loc = loc

    def __repr__(self):
        return f"({self.n}, {self.value})"


answer = 0
module = dict()

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
    print(name)
    p1 = Pulse()
    p2 = Pulse()

for n in module.keys():
    for d in module[n].ds:
        module[d].ins.append(n)
        module[d].mem[n] = False

for n in module.keys():
    print(module[n])
print(answer)