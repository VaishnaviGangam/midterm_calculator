import pytest
from commandManager import OperationManager

def test_add():
    assert OperationManager.compute_sum(2, 3) == 5

def test_subtract():
    assert OperationManager.compute_difference(5, 2) == 3

def test_multiply():
    assert OperationManager.compute_product(4, 3) == 12

def test_divide():
    assert OperationManager.compute_quotient(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        OperationManager.compute_quotient(10, 0)

