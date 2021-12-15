"""Testing the DataManager class."""
import os
import pytest
from data_manager.manager import DataManager
from calc.calculator import Calculator

@pytest.fixture(name="df")
def fixture_get_df():
    """Fixture that gets the CSV file full of testing data"""
    file_path = DataManager.get_absolute_path_from_relative_path("tests/test_data/test_data.csv")
    return DataManager.read_csv_data(file_path)

@pytest.fixture(name="df_calc_types")
def fixture_get_df_calc_types():
    """Fixture that gets the CSV file full of testing data"""
    file_path = DataManager.get_absolute_path_from_relative_path("tests/test_data/calc_types.csv")
    return DataManager.read_csv_data(file_path)

def test_read_csv_data(df):
    """Tests to make sure the DataManager is able to read a CSV file.

    Args:
        df (DataManager): DataManager representing CSV file.
    """
    assert df is not None

def test_write_csv_data():
    """Tests writing to CSV file.
    """
    data = {"column1": "value1", "column2": "value2", "column3": "value3"}
    columns = ("column1", "column2", "column3")
    output_file_path_str = "tests/test_output/calculations_output.csv"
    output_file_path = DataManager.get_absolute_path_from_relative_path(output_file_path_str)

    # Write new file with data
    data_written = DataManager.write_csv_data(data, columns, output_file_path)
    assert data_written is True

    # Append file with more data
    data_written = DataManager.write_csv_data(data, columns, output_file_path)

    # Clean up
    os.remove(output_file_path)

def test_get_calculation_types(df_calc_types):
    """Tests getting the calculation types column values.

    Args:
        df (DataFrame): DataFrame from pandas.
    """
    calculation_types = DataManager.get_calculation_types(df_calc_types)
    assert calculation_types[0] == "addition"
    assert calculation_types[1] == "subtraction"
    assert calculation_types[2] == "multiplication"
    assert calculation_types[3] == "division"

def test_get_results_csv():
    """Tests to make sure that the results CSV can be loaded."""
    results_values = DataManager.get_results_csv()
    Calculator.add(1, 2)
    assert len(results_values) > 0
