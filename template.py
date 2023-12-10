from utils import *
from itertools import product

filename = "input.txt"
with open(filename) as f:
    ls = f.readlines()

answer = 0
expected = 0
report(filename, answer, expected)
