import pytest
from calculator import *


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5


def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)


def test_calculate_trig():
    assert calculate_trig('sin', 90) == pytest.approx(1)
    assert calculate_trig('cos', 0) == pytest.approx(1)


def test_logarithm():
    assert logarithm(10, 100) == 2
    with pytest.raises(ValueError):
        logarithm(0, 100)


def test_convert_units():
    assert convert_units(1, "m", "ft") == pytest.approx(3.28084)
    assert convert_units(2.20462, "lb", "kg") == pytest.approx(1)


def test_statistical_analysis():
    data = [1, 2, 2, 3]
    stats = statistical_analysis(data)
    assert stats["mean"] == 2
    assert stats["median"] == 2
    assert stats["mode"] == 2
