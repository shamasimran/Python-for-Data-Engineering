import logging
from datetime import datetime

# -------------------------------
# 1. Division by Zero Handling
# -------------------------------
def divide_numbers(a, b):
    """Handle division by zero using try-except."""
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")

# Example
# divide_numbers(5, 0)


# -------------------------------
# 2. Handle Multiple Exceptions
# -------------------------------
def convert_and_divide(value):
    """Handle ValueError and ZeroDivisionError."""
    try:
        num = int(value)
        return 10 / num
    except ValueError:
        print("Invalid number format.")
    except ZeroDivisionError:
        print("Division by zero not allowed.")

# Example
# convert_and_divide("abc")


# -------------------------------
# 3. General Exception Example
# -------------------------------
def handle_general_exception():
    """Catch any exception and display the message."""
    try:
        x = 1 / 0
    except Exception as e:
        print("Error occurred:", e)

# Example
# handle_general_exception()


# -------------------------------
# 4. Try-Else-Finally Example
# -------------------------------
def safe_division(a, b):
    """Use else and finally with try-except."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Division successful:", result)
    finally:
        print("Execution completed.")

# Example
# safe_division(10, 2)


# -------------------------------
# 5. Custom Exception Example
# -------------------------------
def divide_with_validation(a, b):
    """Raise custom exception when input is invalid."""
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

def demo_custom_exception():
    try:
        print(divide_with_validation(10, 0))
    except ValueError as e:
        print("Custom Error:", e)

# Example
# demo_custom_exception()


if __name__ == "__main__":
    print(safe_division(10, 0))
