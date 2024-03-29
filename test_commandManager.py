import logging
import pytest
from commandManager import OperationManager

class TestOperationManager:
    def test_perform_addition(self):
        assert OperationManager.compute_sum(2, 3) == 5

    def test_perform_subtraction(self):
        assert OperationManager.compute_difference(5, 3) == 2

    def test_perform_multiplication(self):
        assert OperationManager.compute_product(2, 3) == 6

    def test_perform_division(self):
        assert OperationManager.compute_quotient(6, 3) == 2

    def test_perform_division_by_zero(self):
        with pytest.raises(ValueError):
            OperationManager.compute_quotient(6, 0)


if __name__ == '__main__':
    pytest.main()
