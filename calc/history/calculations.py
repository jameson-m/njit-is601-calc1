"""Calculation history class"""
class Calculations:
    """Calculation history class"""
    history = []

    @staticmethod
    def get_history():
        """Get full calculator history.

        Returns:
            list: List of Calculation objects
        """
        return Calculations.history

    @staticmethod
    def get_last_calculation():
        """Get the last Calculation object in history (most recent).

        Returns:
            Calculation: Most recent Calculation
        """
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """Get the first Calculation object in history.

        Returns:
            Calculation: First Calculation performed
        """
        return Calculations.history[0]

    @staticmethod
    def add_calculation_to_history(calculation):
        """Add a Calculation object to the calculator's history.

        Args:
            calculation (Calculation): Calculation object to add to history

        Returns:
            bool: Whether or not adding to history was success
        """
        Calculations.history.append(calculation)
        return True

    @staticmethod
    def get_last_calculation_result():
        """Get the last Calculation object's result.

        Returns:
            int: Most recent Calculation's result
        """
        last_index = len(Calculations.history) - 1
        return Calculations.history[last_index].get_result()

    @staticmethod
    def clear_history():
        """Clears the calculator's history.

        Returns:
            bool: If calculator's history was successfully cleared
        """
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """Counts the number of items in the calculator's history.

        Returns:
            int: Number of items in calculator's history
        """
        return len(Calculations.history)
