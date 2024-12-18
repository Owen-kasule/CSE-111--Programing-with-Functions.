import math
import pytest
from calculator import add, subtract, multiply, divide, calculate_trig, logarithm


def test_add():
    assert add(5, 3) == 8
    assert add(-5, 5) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, -1) == -5
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_calculate_trig():
    assert math.isclose(calculate_trig("sin", 90), 1.0, rel_tol=1e-5)
    assert math.isclose(calculate_trig("cos", 0), 1.0, rel_tol=1e-5)
    assert math.isclose(calculate_trig("tan", 45), 1.0, rel_tol=1e-5)
    with pytest.raises(ValueError):
        calculate_trig("invalid", 45)


def test_logarithm():
    assert math.isclose(logarithm(10, 100), 2.0, rel_tol=1e-5)
    assert math.isclose(logarithm(math.e, math.e ** 3), 3.0, rel_tol=1e-5)
    with pytest.raises(ValueError):
        logarithm(10, -1)
    with pytest.raises(ValueError):
        logarithm(-2, 100)


def test_edge_cases():
    assert add(1e10, 1e10) == 2e10
    assert multiply(1e-10, 1e10) == 1.0
    assert divide(1e-10, 1e-10) == 1.0


if __name__ == "__main__":
    pytest.main()
