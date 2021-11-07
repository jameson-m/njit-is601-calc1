"""
Testing the Calculator
"""
from calculator.main import Calculator

def test_calculator_result():
    """
    Tests to make sure calculator gives stored result.
    """
    calc = Calculator()
    assert calc.result == 0

def test_calculator_get_result():
    """
    Tests the calculator's get_result method.
    """
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_add():
    """
    Tests calculator's add method.
    """
    calc = Calculator()
    calc.add(5)
    assert calc.get_result() == 5

def test_calculator_subtract():
    """
    Tests calculator's subtract method.
    """
    calc = Calculator()
    calc.subtract(4)
    assert calc.get_result() == -4

def test_calculator_multiply():
    """
    Tests calculator's multiplication method.
    """
    calc = Calculator()
    calc.multiply(2, 2)
    assert calc.get_result() == 4

def test_calculator_division():
    """
    Tests calculator's division method.
    """
    calc = Calculator()
    calc.divide(4, 2)
    assert calc.get_result() == 2

def test_calculator_division_by_zero():
    """
    Tests calculator's division method if 0 in denominator.
    """
    calc = Calculator()
    calc.divide(4, 0)
    assert calc.get_result() == 0
