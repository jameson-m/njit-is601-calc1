"""
Class representing a calculator.
"""
from calc.addition import Addition
from calc.subtraction import Subtraction


class Calculator:
    """Calculator class
    """
    history = []

    # [x] get history
    # [x] get last calculation
    # [x] get first calculation
    # [x] add calculation to history
    # [x] get last calculation result
    # [x] get last calculation object
    # [x] clear history
    # [x] count history
    # [] addition
    # [] subtraction
    # [] multiplication
    # [] division

    @staticmethod
    def get_history():
        return Calculator.history

    @staticmethod
    def get_last_calculation():
        last_index = len(Calculator.history) - 1
        return Calculator.history[last_index]
    
    @staticmethod
    def get_first_calculation():
        return Calculator.history[0]
    
    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True
    
    @staticmethod
    def get_last_calculation_result():
        last_index = len(Calculator.history) - 1
        return Calculator.history[last_index].get_result()

    @staticmethod
    def get_last_calculation():
        last_index = len(Calculator.history) - 1
        return Calculator.history[last_index]
    
    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True
    
    @staticmethod
    def count_history():
        return len(Calculator.history)
    
    @staticmethod
    def add(value_a, value_b):
        """
        Adds two numbers together.

        Args:
            value_a (int): First value
            value_b (int): Second value to be added to first

        Returns:
            Calculation: The created addition calculation object
        """
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation()

    @staticmethod
    def subtract(value_a, value_b):
        """
        Subtracts one number from another.

        Args:
            value_a (int): First value
            value_b (int): Second value subtracted from first

        Returns:
            Calculation: The created subtraction calculation object
        """
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation()

    def multiply(self, value_a, value_b):
        """
        Multiplies two numbers together and stores the new value in result.

        Args:
            value_a (float): First value in multiplication
            value_b (float): Second value in multiplication

        Returns:
            float: Result of multiplication of two given numbers
        """
        self.result = value_a * value_b
        return self.result

    def divide(self, value_a, value_b):
        """
        Divides two numbers together and stores the new value in result.
        If dividing by zero the result is 0.

        Args:
            value_a (float): First value in division
            value_b (float): Second value in division

        Returns:
            float: Result of division of two given numbers
        """
        try:
            self.result = value_a / value_b
            return self.result
        except ZeroDivisionError:
            self.result = 0
            return self.result
