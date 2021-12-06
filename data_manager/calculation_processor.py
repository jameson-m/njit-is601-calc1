"""Calculation Processor class"""

from typing import List

from calc.calculator import Calculator
from logger.logger import Logger

# pylint: disable=too-few-public-methods
class CalculationProcessor:
    """Calculation Processor class"""

    @staticmethod
    # pylint: disable=line-too-long
    def process_csv_calculations(input_file_name: str, calculation_types: List[str], values: List[List[float]]):
        """Process CSV calculations based by type.

        Args:
            input_file_name (str): Name of input file.
            calculation_types (List[str]): List of calculation types.
            values (List[List[float]]): List of columns of values.
        """
        Logger.set_input_file_name(input_file_name)
        for index, calculation_type in enumerate(calculation_types):
            calc_values = [value[index] for value in values if value[index] is not None]
            if calculation_type == "addition":
                Calculator.add(*calc_values)
            elif calculation_type == "subtraction":
                Calculator.subtract(*calc_values)
            elif calculation_type == "multiplication":
                Calculator.multiply(*calc_values)
            elif calculation_type == "division":
                Calculator.divide(*calc_values)
