import unittest
from faker import Faker
import calculator
import pytest
from commandManager import OperationManager
from calculation_history import CalculationHistoryManager

class TestCalculator(unittest.TestCase):
    """Test suite for the Calculator functions.

    This test suite contains unit tests for the add, subtract, multiply, and divide
    functions in the calculator module.

    Attributes:
        fake (Faker): A Faker instance for generating random test data.
    """

    def setUp(self):
        """Set up the test fixture."""
        self.fake = Faker()

    def test_addition(self):
        """Test the addition function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(OperationManager.compute_sum(num1, num2), num1 + num2)

    def test_subtraction(self):
        """Test the subtraction function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(OperationManager.compute_difference(num1, num2), num1 - num2)

    def test_multiplication(self):
        """Test the multiplication function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(OperationManager.compute_product(num1, num2), num1 * num2)

    def test_division(self):
        """Test the division function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(1, 100)  # Ensure num2 is not zero
            self.assertEqual(OperationManager.compute_quotient(num1, num2), num1 / num2)

@pytest.fixture
def history():
    return History()



def test_show_calculation_history(history, capsys):
    # Assuming the CSV file already exists with some saved calculations
    CalculationHistoryManager.display_calculation_history()
    captured = capsys.readouterr()
    # Assert that the captured output matches the expected output
    # You can use your own assertions here based on your specific requirements

if __name__ == '__main__':
    unittest.main()
