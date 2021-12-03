"""Data Manager"""
from typing import List
from pathlib import Path
import pandas as pd
from pandas.core.frame import DataFrame
import numpy

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
        """Read in a given CSV file and return a DataFrame object.

        Args:
            file_path (str): Absolute path to CSV file.

        Returns:
            DataFrame: DataFrame representing the CSV data.
        """
        df = pd.read_csv(file_path, header=0)
        return df

    @staticmethod
    def get_csv_headers(df: DataFrame) -> List[str]:
        """Gets a list of the headers from first row in CSV file (ordered).

        Args:
            df (DataFrame): DataFrame representing CSV file.

        Returns:
            List[str]: List of headers.
        """
        headers = list(df.columns.values)
        return headers

    @staticmethod
    def get_addition_results(df: DataFrame) -> List[float]:
        """Get a list of values from the addition_result column.

        Args:
            df (DataFrame): DataFrame representing CSV file.

        Returns:
            List[float]: List of addition result values.
        """
        addition_results = list(df["addition_result"].values)
        return addition_results

    @staticmethod
    def get_subtraction_results(df: DataFrame) -> List[float]:
        """Get a list of values from the subtraction_result column.

        Args:
            df (DataFrame): DataFrame representing CSV file.

        Returns:
            List[float]: List of subtraction result values.
        """
        subtraction_results = list(df["subtraction_result"].values)
        return subtraction_results

    @staticmethod
    def get_multiplication_results(df: DataFrame) -> List[float]:
        """Get a list of values from the multiplication_result column.

        Args:
            df (DataFrame): DataFrame representing CSV file.

        Returns:
            List[float]: List of multiplication result values.
        """
        multiplication_results = list(df["multiplication_result"].values)
        return multiplication_results

    @staticmethod
    def get_division_results(df: DataFrame) -> List[float]:
        """Get a list of values from the division_result column.

        Args:
            df (DataFrame): DataFrame representing CSV file.

        Returns:
            List[float]: List of division result values.
        """
        division_results = list(df["division_result"].values)
        return division_results

    @staticmethod
    def get_list_of_values(df: DataFrame) -> List[List[float]]:
        """Gets a list of all value columns represented as a 2D array.
        If a cell has no value, a value of None is entered.

        Args:
            df (DataFrame): DataFrame representing CSV file.

        Returns:
            List[List[float]]: List of value column values.
        """
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
