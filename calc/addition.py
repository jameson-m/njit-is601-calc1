"""Addition subclass"""
from calc.calculation import Calculation

class Addition(Calculation):
    """Addition class.
    """

    def get_result(self):
        """Adds two numbers together and returns result.

        Returns:
            int: result of two numbers added
        """
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
