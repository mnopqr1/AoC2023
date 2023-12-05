from day5 import *

def test_intersect():
    assert intersect(0,3,4,7) == (None,None)
    assert intersect(4,7,0,3) == (None,None)
    assert intersect(0,7,3,3) == (3,3)
    assert intersect(0,7,3,8) == (3,4)

def test_minus():
    assert minus(0,10,3,4) == [(0,3), (7,3)]
    assert minus(0,10,11,3) == [(0,10)]
    assert minus(0,10,-2,5) == [(3,7)]
    assert minus(0,10,-1,11) == []
    assert minus(0,10,7,5) == [(0,7)]
    assert minus(5,10,0,3) == [(5,10)]
