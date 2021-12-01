"""Calculation base class."""

class Calculation:
    """Calculation base class."""
    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple):
        self.values = Calculation.convert_args_to_list_float(values)

    @classmethod
    def create(cls, values: tuple):
        """Class factory method."""
        return cls(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """Standardize values to list of floats"""
        list_values = []
        for item in values:
            list_values.append(float(item))
        return list_values
