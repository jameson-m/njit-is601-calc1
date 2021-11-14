from calc.calculation import Calculation

class Division(Calculation):
    def get_result(self):
        """Divides one number from another and returns result. First number is numerator, second number is denominator.

        Returns:
            float: Result of division of two given numbers
        """
        try:
            return self.value_a / self.value_b
        except ZeroDivisionError:
            return 0