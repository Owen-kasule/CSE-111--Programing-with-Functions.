import pytest
from tkinter import Tk
from calculator_app import CalculatorApp

@pytest.fixture
def app():
    root = Tk()
    calculator = CalculatorApp(root)
    yield calculator
    root.destroy()

def test_addition(app):
    app.num1_entry.insert(0, "10")
    app.num2_entry.insert(0, "5")
    app.operation_var.set("Add")
    app.calculate()
    assert app.result_value.cget("text") == "15.00"

def test_subtraction(app):
    app.num1_entry.insert(0, "10")
    app.num2_entry.insert(0, "5")
    app.operation_var.set("Subtract")
    app.calculate()
    assert app.result_value.cget("text") == "5.00"

def test_multiplication(app):
    app.num1_entry.insert(0, "10")
    app.num2_entry.insert(0, "5")
    app.operation_var.set("Multiply")
    app.calculate()
    assert app.result_value.cget("text") == "50.00"

def test_division(app):
    app.num1_entry.insert(0, "10")
    app.num2_entry.insert(0, "2")
    app.operation_var.set("Divide")
    app.calculate()
    assert app.result_value.cget("text") == "5.00"

def test_sine(app):
    app.num1_entry.insert(0, "30")
    app.operation_var.set("Sine")
    app.calculate()
    assert round(float(app.result_value.cget("text")), 2) == 0.50

def test_clear_fields(app):
    app.num1_entry.insert(0, "10")
    app.num2_entry.insert(0, "5")
    app.result_value.config(text="Test")
    app.clear_fields()
    assert app.num1_entry.get() == ""
    assert app.result_value.cget("text") == ""
