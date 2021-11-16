"""Subtraction subclass"""
from calc.calculation import Calculation

class Subtraction(Calculation):
    """Subtraction class.
    """

    def get_result(self):
        """Subtracts two numbers together and returns result.

        Returns:
            int: result of subtracting one number from another
        """
        result = self.values[0]
        for value in self.values[1:]:
            result = result - value
        return result
