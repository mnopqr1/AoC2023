

from dataclasses import dataclass
from typing import Dict, List


filename = "test.txt"
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
        assert self.name == p.tow
        print(f"{self.name} handles {p}")
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
            print(f"Preparing to send to {self.ds}")
            for d in self.ds:
                newp = Pulse(sendval, self.name, d)
                newps.append(newp)
                print(f"{self.name} sends {newp}")

        return newps


class Pulse:
    n: int
    value: bool
    cur: str
    tow: str
    n_pulses = 0

    def __init__(self, value=False, cur="button", tow="roadcaster"):
        Pulse.n_pulses += 1
        self.n = Pulse.n_pulses
        self.value = value
        self.cur = cur
        self.tow = tow

    def __repr__(self):
        return f"({self.n=}, {self.value=}, {self.cur=}, {self.tow=})"


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
    # print(name)    

for n in module.keys():
    for d in module[n].ds:
        module[d].ins.append(n)
        module[d].mem[n] = False

# for n in module.keys():
#     print(module[n])

p = Pulse()
stack = [p]

while len(stack) > 0:
    p = stack.pop()
    print(f"Current pulse: {p}")
    handler = module[p.tow]
    print(f"Current handler: {handler}")
    newps = handler.handle(p)
    stack += newps
    print(stack)
    input()

print(answer)