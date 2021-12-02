import pytest
from data_manager.manager import DataManager

def test_read_csv_data():
    file_path = DataManager.get_absolute_path_from_relative_path("tests/test_data/test_data.csv")
    df = DataManager.read_csv_data(file_path)
    return df
