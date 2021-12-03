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

def test_calculator_add(clear_history, df):
    """Tests the calculator's add method."""
    assert clear_history is True

    addition_results_key = DataManager.get_addition_results(df)
    values = DataManager.get_list_of_values(df)

    for row_index, result_key in enumerate(addition_results_key):
        row_values = []
        for val_column in values:
            if val_column[row_index] is not None:
                row_values.append(val_column[row_index])

        assert Calculator.add(*row_values).get_result() == result_key

def test_calculator_subtract(clear_history, df):
    """Tests the calculator's subtract method."""
    assert clear_history is True

    subtraction_results_key = DataManager.get_subtraction_results(df)
    values = DataManager.get_list_of_values(df)

    for row_index, result_key in enumerate(subtraction_results_key):
        row_values = []
        for val_column in values:
            if val_column[row_index] is not None:
                row_values.append(val_column[row_index])

        assert Calculator.subtract(*row_values).get_result() == result_key

def test_calculator_multiply(clear_history, df):
    """Tests the calculator's multiplication method."""
    assert clear_history is True

    multiplication_results_key = DataManager.get_multiplication_results(df)
    values = DataManager.get_list_of_values(df)

    for row_index, result_key in enumerate(multiplication_results_key):
        row_values = []
        for val_column in values:
            if val_column[row_index] is not None:
                row_values.append(val_column[row_index])

        assert Calculator.multiply(*row_values).get_result() == result_key

def test_calculator_divide(clear_history, df):
    """Tests the calculator's division method."""
    assert clear_history is True

    division_results_key = DataManager.get_division_results(df)
    values = DataManager.get_list_of_values(df)

    for row_index, result_key in enumerate(division_results_key):
        row_values = []
        for val_column in values:
            if val_column[row_index] is not None:
                row_values.append(val_column[row_index])

        assert round(Calculator.divide(*row_values).get_result(), 9) == result_key

def test_calculator_divide_by_zero(clear_history):
    """Tests the calculator's ability to handle division by zero."""
    assert clear_history is True
    assert Calculator.divide(8, 0).get_result() == 0
