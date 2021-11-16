"""
Class representing a calculator.
"""
from calc.addition import Addition
from calc.division import Division
from calc.multiplication import Multiplication
from calc.subtraction import Subtraction

class Calculator:
    """Calculator class"""
    history = []

    @staticmethod
    def get_history():
        """Get full calculator history.

        Returns:
            list: List of Calculation objects
        """
        return Calculator.history

    @staticmethod
    def get_last_calculation():
        """Get the last Calculation object in history (most recent).

        Returns:
            Calculation: Most recent Calculation
        """
        last_index = len(Calculator.history) - 1
        return Calculator.history[last_index]

    @staticmethod
    def get_first_calculation():
        """Get the first Calculation object in history.

        Returns:
            Calculation: First Calculation performed
        """
        return Calculator.history[0]

    @staticmethod
    def add_calculation_to_history(calculation):
        """Add a Calculation object to the calculator's history.

        Args:
            calculation (Calculation): Calculation object to add to history

        Returns:
            bool: Whether or not adding to history was success
        """
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_last_calculation_result():
        """Get the last Calculation object's result.

        Returns:
            int: Most recent Calculation's result
        """
        last_index = len(Calculator.history) - 1
        return Calculator.history[last_index].get_result()

    @staticmethod
    def clear_history():
        """Clears the calculator's history.

        Returns:
            bool: If calculator's history was successfully cleared
        """
        Calculator.history.clear()
        return True

    @staticmethod
    def count_history():
        """Counts the number of items in the calculator's history.

        Returns:
            int: Number of items in calculator's history
        """
        return len(Calculator.history)

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
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation()

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
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation()

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
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_last_calculation()

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
        Calculator.add_calculation_to_history(division)
        return Calculator.get_last_calculation()
