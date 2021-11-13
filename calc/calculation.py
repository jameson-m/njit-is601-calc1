class Calculation:
    """
    Calculation base class.
    """
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
    
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a, value_b)