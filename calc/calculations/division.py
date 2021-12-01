"""Division subclass"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Division class"""
    def get_result(self):
        """Divides one number from another and returns result.
        First number is numerator, second number is denominator.

        Returns:
            float: Result of division of two given numbers
        """
        try:
            result = self.values[0]
            for value in self.values[1:]:
                result = result / value
            return result
        except ZeroDivisionError:
            return 0
