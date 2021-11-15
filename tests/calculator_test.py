"""Testing the Calculator"""
import pytest
from calculator.main import Calculator
from calc.addition import Addition
from calc.calculation import Calculation

@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """Fixture that clears the calculator's history for the next test."""
    return Calculator.clear_history()

def test_calculator_add(clear_history):
    """Tests the calculator's add method."""
    assert clear_history is True
    assert Calculator.add(1, 2).get_result() == 3
    assert Calculator.add(2, 2).get_result() == 4
    assert Calculator.add(3, 2).get_result() == 5
    assert Calculator.add(3, 3).get_result() == 6
    assert Calculator.count_history() == 4
    assert Calculator.get_last_calculation_result() == 6

def test_calculator_subtract(clear_history):
    """Tests the calculator's subtract method."""
    assert clear_history is True
    assert Calculator.subtract(3, 1).get_result() == 2
    assert Calculator.subtract(9, 3).get_result() == 6
    assert Calculator.subtract(8, 4).get_result() == 4
    assert Calculator.subtract(6, 3).get_result() == 3
    assert Calculator.count_history() == 4
    assert Calculator.get_last_calculation_result() == 3

def test_calculator_multiply(clear_history):
    """Tests the calculator's multiplication method."""
    assert clear_history is True
    assert Calculator.multiply(3, 1).get_result() == 3
    assert Calculator.multiply(9, 3).get_result() == 27
    assert Calculator.multiply(8, 4).get_result() == 32
    assert Calculator.multiply(6, 3).get_result() == 18
    assert Calculator.multiply(2, 2).get_result() == 4
    assert Calculator.count_history() == 5
    assert Calculator.get_last_calculation_result() == 4

def test_calculator_divide(clear_history):
    """Tests the calculator's division method."""
    assert clear_history is True
    assert Calculator.divide(3, 1).get_result() == 3
    assert Calculator.divide(9, 3).get_result() == 3
    assert Calculator.divide(27, 9).get_result() == 3
    assert Calculator.divide(15, 3).get_result() == 5
    assert Calculator.divide(2, 2).get_result() == 1
    assert Calculator.count_history() == 5
    assert Calculator.get_last_calculation_result() == 1

def test_calculator_divide_by_zero(clear_history):
    """Tests the calculator's ability to handle division by zero."""
    assert clear_history is True
    assert Calculator.divide(8, 0).get_result() == 0

def test_calculator_get_history(clear_history):
    """Tests the calculator's get_history method."""
    assert clear_history is True
    Calculator.add(2, 2)
    assert len(Calculator.get_history()) == 1
    Calculator.add(2, 2)
    Calculator.add(2, 2)
    assert len(Calculator.get_history()) == 3
    Calculator.clear_history()
    Calculator.add(2, 2)
    Calculator.add(2, 2)
    assert len(Calculator.get_history()) == 2


def test_calculator_get_last_calculation(clear_history):
    """Tests the calculator's get_last_calculation method."""
    assert clear_history is True
    Calculator.add(2, 2)
    Calculator.add(3, 1)
    last_calculation = Calculator.get_last_calculation()
    assert last_calculation.get_result() == 4

def test_calculator_get_first_calculation(clear_history):
    """Tests the calculator's get_first_calculation method."""
    assert clear_history is True
    Calculator.add(3, 1)
    Calculator.add(2, 1)
    Calculator.add(5, 3)
    first_calculation = Calculator.get_first_calculation()
    assert first_calculation.get_result() == 4

def test_calculator_add_calculation_to_history(clear_history):
    """Tests the calculator's add_calculation_to_history method."""
    assert clear_history is True
    assert Calculator.add_calculation_to_history(Addition.create(3, 2)) is True

def test_calculator_get_last_calculation_result(clear_history):
    """Tests the calculator's get_last_calculation_result method."""
    assert clear_history is True
    Calculator.add(2, 2)
    Calculator.add(9, 3)
    Calculator.subtract(3, 1)
    assert Calculator.get_last_calculation_result() == 2

def test_calculator_clear_history(clear_history):
    """Tests the calculator's clear_history method."""
    assert clear_history is True
    Calculator.add(2, 2)
    assert Calculator.count_history() == 1
    assert Calculator.clear_history() is True
    assert Calculator.count_history() == 0

def test_calculator_count_history(clear_history):
    """Tests the calculator's count_history method."""
    assert clear_history is True
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    assert Calculator.count_history() == 5

def test_calculation_speak(clear_history):
    """Tests the calculation speak method."""
    assert clear_history is True
    assert Calculation.speak() == "Hello from your calculator!"
