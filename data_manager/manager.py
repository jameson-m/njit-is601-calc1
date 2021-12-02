"""Data Manager"""
from typing import List
import pandas as pd
from pandas.core.frame import DataFrame
import numpy
from pathlib import Path

class DataManager:
    """Data manager class using pandas to read CSV files.
    """
    @staticmethod
    def get_absolute_path_from_relative_path(file_path: str) -> str:
        """Converts a relative path to absolute path.

        Args:
            path_name (str): relative path

        Returns:
            str: absolute path
        """
        relative = Path(file_path)
        return relative.absolute()

    @staticmethod
    def read_csv_data(file_path: str) -> DataFrame:
        df = pd.read_csv(file_path, header=0)
        return df

    @staticmethod
    def get_csv_headers(df: DataFrame) -> List[str]:
        headers = list(df.columns.values)
        return headers
    
    @staticmethod
    def get_addition_results(df: DataFrame) -> List[float]:
        addition_results = list(df["addition_result"].values)
        return addition_results

    @staticmethod
    def get_subtraction_results(df: DataFrame) -> List[float]:
        subtraction_results = list(df["subtraction_result"].values)
        return subtraction_results

    @staticmethod
    def get_multiplication_results(df: DataFrame) -> List[float]:
        multiplication_results = list(df["multiplication_result"].values)
        return multiplication_results

    @staticmethod
    def get_division_results(df: DataFrame) -> List[float]:
        division_results = list(df["division_result"].values)
        return division_results
    
    @staticmethod
    def get_list_of_values(df: DataFrame) -> List[List[float]]:
        values_list = []
        headers = DataManager.get_csv_headers(df)
        value_headers = filter(lambda header: "value" in header, headers)

        for header in value_headers:
            values = list(df[header].values)
            for index, value in enumerate(values):
                if numpy.isnan(value):
                    values[index] = None
                else:
                    values[index] = value
            values_list.append(values)
        
        return values_list
