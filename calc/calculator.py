"""
Class representing a calculator.
"""
from calc.history.calculations import Calculations

class Calculator:
    """Calculator class"""
    @staticmethod
    def add(*args):
        """
        Adds two numbers together.

        Args:
            value_a (int): First value
            value_b (int): Second value to be added to first

        Returns:
            Calculation: The created addition calculation object
        """
        Calculations.add_addition_calculation(args)
        return Calculations.get_last_calculation()

    @staticmethod
    def subtract(*args):
        """
        Subtracts one number from another.

        Args:
            value_a (int): First value
            value_b (int): Second value subtracted from first

        Returns:
            Calculation: The created subtraction calculation object
        """
        Calculations.add_subtraction_calculation(args)
        return Calculations.get_last_calculation()

    @staticmethod
    def multiply(*args):
        """
        Multiplies two numbers together.

        Args:
            value_a (int): First value
            value_b (int): Second value to be multiplied on the second

        Returns:
            Calculation: The created multiplication calculation object
        """
        Calculations.add_multiplication_calculation(args)
        return Calculations.get_last_calculation()

    @staticmethod
    def divide(*args):
        """
        Divides two numbers together.
        If dividing by zero the result is 0.

        Args:
            value_a (int): Numerator
            value_b (int): Divisor

        Returns:
            float: Result of division of two given numbers
        """
        Calculations.add_division_calculation(args)
        return Calculations.get_last_calculation()
