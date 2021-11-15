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
        return self.value_a * self.value_b
