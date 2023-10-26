import pytest 
from funciones import *

@pytest.mark.parametrize("x,res"[
    (123,6)
])
def test_sumatoria(x,res):
    assert sumatoria(x) == res