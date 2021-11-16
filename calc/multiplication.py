"""Multiplication subclass"""
from calc.calculation import Calculation

class Multiplication(Calculation):
    """Multiplication class.
    """

    def get_result(self):
        """Multiplies two numbers and returns result.

        Returns:
            int: result of multiplying two numbers
        """
        result = self.values[0]
        for value in self.values[1:]:
            result = result * value
        return result
