"""Testing the DataManager class."""
import pytest
from data_manager.manager import DataManager

@pytest.fixture(name="df")
def fixture_get_df():
    """Fixture that gets the CSV file full of testing data"""
    file_path = DataManager.get_absolute_path_from_relative_path("tests/test_data/test_data.csv")
    return DataManager.read_csv_data(file_path)

def test_read_csv_data(df):
    """Tests to make sure the DataManager is able to read a CSV file.

    Args:
        df (DataManager): DataManager representing CSV file.
    """
    assert df is not None
