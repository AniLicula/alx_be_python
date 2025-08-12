class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        Doesn't need access to class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that prints a class-level attribute and
        returns the product of two numbers.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
