"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """Fixture that clears the calculator's history for the next test."""
    return Calculations.clear_history()

def test_calculator_add(clear_history):
    """Tests the calculator's add method."""
    assert clear_history is True
    assert Calculator.add(1, 2).get_result() == 3
    assert Calculator.add(2, 2).get_result() == 4
    assert Calculator.add(3, 2).get_result() == 5
    assert Calculator.add(3, 3).get_result() == 6

    # test more than 2 numbers
    assert Calculator.add(1, 2, 3).get_result() == 6
    assert Calculator.add(1, 1, 1, 1, 1, 1, 1, 1).get_result() == 8

def test_calculator_subtract(clear_history):
    """Tests the calculator's subtract method."""
    assert clear_history is True
    assert Calculator.subtract(3, 1).get_result() == 2
    assert Calculator.subtract(9, 3).get_result() == 6
    assert Calculator.subtract(8, 4).get_result() == 4
    assert Calculator.subtract(6, 3).get_result() == 3

    # test more than 2 numbers
    assert Calculator.subtract(8, 3, 1).get_result() == 4
    assert Calculator.subtract(16, 8, 1, 2).get_result() == 5

def test_calculator_multiply(clear_history):
    """Tests the calculator's multiplication method."""
    assert clear_history is True
    assert Calculator.multiply(3, 1).get_result() == 3
    assert Calculator.multiply(9, 3).get_result() == 27
    assert Calculator.multiply(8, 4).get_result() == 32
    assert Calculator.multiply(6, 3).get_result() == 18
    assert Calculator.multiply(2, 2).get_result() == 4

    # test more than 2 numbers
    assert Calculator.multiply(2, 2, 2, 2).get_result() == 16
    assert Calculator.multiply(1, 1, 1, 1, 1).get_result() == 1
    assert Calculator.multiply(1, 2, 3).get_result() == 6

def test_calculator_divide(clear_history):
    """Tests the calculator's division method."""
    assert clear_history is True
    assert Calculator.divide(3, 1).get_result() == 3
    assert Calculator.divide(9, 3).get_result() == 3
    assert Calculator.divide(27, 9).get_result() == 3
    assert Calculator.divide(15, 3).get_result() == 5
    assert Calculator.divide(2, 2).get_result() == 1

    # test more than 2 numbers
    assert Calculator.divide(16, 2, 2).get_result() == 4
    assert Calculator.divide(1, 1, 1, 1, 1, 1, 1, 1).get_result() == 1
    assert Calculator.divide(8, 3, 1, 0).get_result() == 0

def test_calculator_divide_by_zero(clear_history):
    """Tests the calculator's ability to handle division by zero."""
    assert clear_history is True
    assert Calculator.divide(8, 0).get_result() == 0
