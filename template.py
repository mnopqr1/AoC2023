from utils import *

def parse(ls):
    pass

def solve1(xs):
    pass

def solve2(xs):
    pass

def solve(filename, expected=None):
    with open(filename) as f:
        ls = f.readlines()
    xs = parse(ls)
    s = [solve1(xs), solve2(xs)]
    
    report(filename, s, expected)
    
if __name__ == "__main__":
    solve("test.txt", [None,None])
    solve("input.txt")