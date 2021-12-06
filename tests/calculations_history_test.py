"""Testing the Calculator history"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculator import Calculator

@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """Fixture that clears the calculator's history for the next test."""
    return Calculations.clear_history()

@pytest.fixture(name="setup_addition_calculation")
def fixture_setup_addition_calculation():
    """create addition calculation in history"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation_to_history(addition, " + ")

def test_add_calculation_to_history(clear_history, setup_addition_calculation):
    """Testing that calculations are added to history"""
    # pylint: disable=unused-argument
    assert Calculations.count_history() == 1

def test_calculator_get_history(clear_history):
    """Tests the calculator's get_history method."""
    assert clear_history is True
    Calculator.add(2, 2)
    assert Calculations.count_history() == 1
    current_calculations = Calculations.get_history()
    assert Calculations.count_history() == len(current_calculations)
    Calculator.add(2, 2)
    Calculator.add(2, 2)
    assert Calculations.count_history() == 3
    Calculations.clear_history()
    Calculator.add(2, 2)
    Calculator.add(2, 2)
    assert Calculations.count_history() == 2


def test_calculator_get_last_calculation(clear_history):
    """Tests the calculator's get_last_calculation method."""
    assert clear_history is True
    Calculator.add(2, 2)
    Calculator.add(3, 1)
    last_calculation = Calculations.get_last_calculation()
    assert last_calculation.get_result() == 4

def test_calculator_get_first_calculation(clear_history):
    """Tests the calculator's get_first_calculation method."""
    assert clear_history is True
    Calculator.add(3, 1)
    Calculator.add(2, 1)
    Calculator.add(5, 3)
    first_calculation = Calculations.get_first_calculation()
    assert first_calculation.get_result() == 4

def test_calculator_get_last_calculation_result(clear_history):
    """Tests the calculator's get_last_calculation_result method."""
    assert clear_history is True
    Calculator.add(2, 2)
    Calculator.add(9, 3)
    Calculator.subtract(3, 1)
    assert Calculations.get_last_calculation_result() == 2

def test_calculator_clear_history(clear_history):
    """Tests the calculator's clear_history method."""
    assert clear_history is True
    Calculator.add(2, 2)
    assert Calculations.count_history() == 1
    assert Calculations.clear_history() is True
    assert Calculations.count_history() == 0

def test_calculator_count_history(clear_history):
    """Tests the calculator's count_history method."""
    assert clear_history is True
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    Calculator.add(3, 2)
    assert Calculations.count_history() == 5

def test_add_addition_calculation(clear_history):
    """Tests the calculator history's add addition calculation method."""
    assert clear_history is True

    calculation_added = Calculations.add_addition_calculation((1, 2, 3, 4))
    assert calculation_added is True
    assert Calculations.count_history() == 1

def test_add_subtraction_calculation(clear_history):
    """Tests the calculator history's add subtraction calculation method."""
    assert clear_history is True

    calculation_added = Calculations.add_subtraction_calculation((1, 2, 3, 4))
    assert calculation_added is True
    assert Calculations.count_history() == 1

def test_add_multiplication_calculation(clear_history):
    """Tests the calculator history's add multiplication calculation method."""
    assert clear_history is True

    calculation_added = Calculations.add_multiplication_calculation((1, 2, 3, 4))
    assert calculation_added is True
    assert Calculations.count_history() == 1

def test_add_division_calculation(clear_history):
    """Tests the calculator history's add division calculation method."""
    assert clear_history is True

    calculation_added = Calculations.add_division_calculation((1, 2, 3, 4))
    assert calculation_added is True
    assert Calculations.count_history() == 1
