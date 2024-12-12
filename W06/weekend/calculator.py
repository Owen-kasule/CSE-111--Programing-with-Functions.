import math
import statistics


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers with error handling for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculate_trig(function, value):
    """Calculate trigonometric functions."""
    functions = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan
    }
    if function not in functions:
        raise ValueError("Invalid trigonometric function. Choose from 'sin', 'cos', or 'tan'.")
    return round(functions[function](math.radians(value)), 6)


def logarithm(base, value):
    """Calculate logarithm of a number with a specified base."""
    if base <= 0 or value <= 0:
        raise ValueError("Base and value must be positive.")
    return round(math.log(value, base), 6)


def convert_units(value, unit_from, unit_to):
    """Convert units between metric and imperial systems."""
    conversions = {
        ("m", "ft"): lambda x: x * 3.28084,
        ("ft", "m"): lambda x: x / 3.28084,
        ("kg", "lb"): lambda x: x * 2.20462,
        ("lb", "kg"): lambda x: x / 2.20462,
    }
    if (unit_from, unit_to) not in conversions:
        raise ValueError("Unsupported unit conversion.")
    return round(conversions[(unit_from, unit_to)](value), 6)


def statistical_analysis(data_list):
    """Perform statistical analysis: mean, median, and mode."""
    if not data_list:
        raise ValueError("Data list cannot be empty.")
    return {
        "mean": round(statistics.mean(data_list), 6),
        "median": round(statistics.median(data_list), 6),
        "mode": statistics.mode(data_list)
    }


def get_user_input():
    """Retrieve user input and provide an interactive menu."""
    print("\nWelcome to the Advanced Calculator!")
    print("Select an operation:")
    print("1. Basic Operations (add, subtract, multiply, divide)")
    print("2. Trigonometric Functions (sin, cos, tan)")
    print("3. Logarithmic Calculations")
    print("4. Unit Conversion")
    print("5. Statistical Analysis")
    print("6. Exit")
    return input("\nEnter your choice (1-6): ").strip()


def main():
    """Orchestrate the program workflow."""
    while True:
        try:
            choice = get_user_input()
            if choice == "1":
                print("\n--- Basic Operations ---")
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
                if operation == "add":
                    print(f"Result: {add(a, b)}")
                elif operation == "subtract":
                    print(f"Result: {subtract(a, b)}")
                elif operation == "multiply":
                    print(f"Result: {multiply(a, b)}")
                elif operation == "divide":
                    print(f"Result: {divide(a, b)}")
                else:
                    print("Invalid operation selected.")

            elif choice == "2":
                print("\n--- Trigonometric Functions ---")
                function = input("Enter function (sin, cos, tan): ").strip().lower()
                value = float(input("Enter value in degrees: "))
                print(f"Result: {calculate_trig(function, value)}")

            elif choice == "3":
                print("\n--- Logarithmic Calculations ---")
                base = float(input("Enter base: "))
                value = float(input("Enter value: "))
                print(f"Result: {logarithm(base, value)}")

            elif choice == "4":
                print("\n--- Unit Conversion ---")
                value = float(input("Enter value: "))
                unit_from = input("Enter unit to convert from (m, ft, kg, lb): ").strip().lower()
                unit_to = input("Enter unit to convert to (m, ft, kg, lb): ").strip().lower()
                print(f"Converted Value: {convert_units(value, unit_from, unit_to)}")

            elif choice == "5":
                print("\n--- Statistical Analysis ---")
                data = list(map(float, input("Enter data separated by spaces: ").split()))
                stats = statistical_analysis(data)
                print(f"Mean: {stats['mean']}, Median: {stats['median']}, Mode: {stats['mode']}")

            elif choice == "6":
                print("Thank you for using the Advanced Calculator. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
