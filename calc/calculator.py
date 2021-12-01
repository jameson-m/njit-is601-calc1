"""
Class representing a calculator.
"""
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction
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
        addition = Addition(args)
        Calculations.add_calculation_to_history(addition)
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
        subtraction = Subtraction(args)
        Calculations.add_calculation_to_history(subtraction)
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
        multiplication = Multiplication(args)
        Calculations.add_calculation_to_history(multiplication)
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
        division = Division(args)
        Calculations.add_calculation_to_history(division)
        return Calculations.get_last_calculation()
