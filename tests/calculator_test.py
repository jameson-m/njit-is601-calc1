"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from data_manager.manager import DataManager

@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """Fixture that clears the calculator's history for the next test."""
    return Calculations.clear_history()

@pytest.fixture(name="df")
def fixture_get_df():
    """Fixture that gets the CSV file full of testing data"""
    file_path = DataManager.get_absolute_path_from_relative_path("tests/test_data/test_data.csv")
    return DataManager.read_csv_data(file_path)

def run_calc_comparison(results, values, callback):
    """Compares calculator's solution to results key."""
    for row_index, result in enumerate(results):
        row_values = []
        for val_column in values:
            if val_column[row_index] is not None:
                row_values.append(val_column[row_index])

        assert round(callback(*row_values).get_result(), 9) == result

def test_calculator_add(clear_history, df):
    """Tests the calculator's add method."""
    assert clear_history is True

    addition_results = DataManager.get_addition_results(df)
    values = DataManager.get_list_of_values(df)

    run_calc_comparison(addition_results, values, Calculator.add)

def test_calculator_subtract(clear_history, df):
    """Tests the calculator's subtract method."""
    assert clear_history is True

    subtraction_results = DataManager.get_subtraction_results(df)
    values = DataManager.get_list_of_values(df)

    run_calc_comparison(subtraction_results, values, Calculator.subtract)

def test_calculator_multiply(clear_history, df):
    """Tests the calculator's multiplication method."""
    assert clear_history is True

    multiplication_results = DataManager.get_multiplication_results(df)
    values = DataManager.get_list_of_values(df)

    run_calc_comparison(multiplication_results, values, Calculator.multiply)

def test_calculator_divide(clear_history, df):
    """Tests the calculator's division method."""
    assert clear_history is True

    division_results = DataManager.get_division_results(df)
    values = DataManager.get_list_of_values(df)

    run_calc_comparison(division_results, values, Calculator.divide)

def test_calculator_divide_by_zero(clear_history):
    """Tests the calculator's ability to handle division by zero."""
    assert clear_history is True
    assert Calculator.divide(8, 0).get_result() == "ZERO_DIVISION_ERROR"

def test_calculator_get_last_result_value(clear_history):
    """Tests the get_last_result_value method."""
    assert clear_history is True

    Calculator.add(1, 1)
    assert Calculator.get_last_result_value() == 2
    Calculator.subtract(3, 2)
    assert Calculator.get_last_result_value() == 1
    Calculator.multiply(2, 5)
    assert Calculator.get_last_result_value() == 10
    Calculator.divide(21, 7)
    assert Calculator.get_last_result_value() == 3
