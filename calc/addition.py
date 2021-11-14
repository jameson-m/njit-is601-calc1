from calc.calculation import Calculation

class Addition(Calculation):
    """Addition class.
    """
    
    def get_result(self):
        """Adds two numbers together and returns result.

        Returns:
            int: result of two numbers added
        """
        return self.value_a + self.value_b