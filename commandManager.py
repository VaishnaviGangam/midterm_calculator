import logging

class OperationManager:
    @staticmethod
    def compute_sum(x, y):
        """Add two numbers."""
        result = x + y
        logging.info(f"Add: {x} + {y} = {result}")
        return result

    @staticmethod
    def compute_difference(x, y):
        """Subtract two numbers."""
        result = x - y
        logging.info(f"Subtract: {x} - {y} = {result}")
        return result

    @staticmethod
    def compute_product(x, y):
        """Multiply two numbers."""
        result = x * y
        logging.info(f"Multiply: {x} * {y} = {result}")
        return result

    @staticmethod
    def compute_quotient(x, y):
        """Divide two numbers."""
        if y == 0:
            logging.error("Division by zero!")
            raise ValueError("Cannot divide by zero!")
        result = x / y
        logging.info(f"Divide: {x} / {y} = {result}")
        return result
    @staticmethod
    def compute_square_root(num):
        """Calculate the square root of a number."""
        result = num ** 0.5
        logging.info(f"Square root of {num} = {result}")
        return result
    def convert_to_binary(num):
        """Convert a number to binary."""
        result = bin(num)
        result=result[2:]
        logging.info(f"Binary representation of {num} = {result}")
        return result

