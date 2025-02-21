import pytest
from app import add, subtract, multiply, divide, degree, maximum, minimum

NUMBER_1 = 3.0
NUMBER_2 = 2.0

def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0

def test_subtract():
    value = subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0

def test_multiply():
    value = multiply(NUMBER_1, NUMBER_2)
    assert value == 6.0

def test_divide():
    value = divide(NUMBER_1, NUMBER_2)
    assert value == 1.5
    
def test_degree():
    value = degree(NUMBER_1, NUMBER_2)
    assert value == 9.0  

def test_maximum():
    value = maximum(NUMBER_1, NUMBER_2)
    assert value == 3.0

def test_minimum():
    value = minimum(NUMBER_1, NUMBER_2)
    assert value == 2.0