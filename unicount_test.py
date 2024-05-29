from hypothesis import given
import hypothesis.strategies as st
import unicount
import sys

@given(st.lists(st.integers(min_value=0, max_value=sys.maxsize), min_size=0),
       st.integers(min_value=1, max_value=sys.maxsize))
def test_generative(s, size):
    actual = unicount.actual(s)
    estimated = unicount.estimate(s, size)
    high = actual << ((len(s) // size) - 0)
    assert 0 <= estimated and estimated <= high

def test_hamlet():
    with open('hamlet.txt','r') as lines:
        s = ''.join(lines.readlines()).split()
        actual = unicount.actual(s)
        estimated = unicount.estimate(s, 10*1000)
        assert actual == estimated
