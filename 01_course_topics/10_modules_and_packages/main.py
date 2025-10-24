"""
main.py
Demonstrates how to use custom modules and built-in packages in Python.
"""

# built-in packages
import os
import math

# custom modules
import math_utils as mth
from string_utils import StringHandler

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # --- Using math_utils module ---
    print("Math Utilities Demo:")
    print(f"Add: 5 + 3 = {mth.add(5, 3)}")
    print(f"Subtract: 10 - 4 = {mth.subtract(10, 4)}")
    print(f"Multiply: 6 * 7 = {mth.multiply(6, 7)}")
    print(f"Divide: 8 / 2 = {mth.divide(8, 2)}")

    # --- Using string_utils module ---
    print("\nString Utilities Demo:")
    text = "Data Engineering"
    print(f"Original Text: {text}")
    
    str_util = StringHandler()
    print(f"Uppercase: {str_util.to_upper(text)}")
    print(f"Lowercase: {str_util.to_lower(text)}")
    print(f"Vowel Count: {str_util.count_vowels(text)}")

    # --- Using built-in math module ---
    print("\nBuilt-in Math Module Demo:")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Pi constant: {math.pi}")
    print(f"Power: 2^3 = {math.pow(2, 3)}")

def main_package():
    from dateutil import format_date
    from dateutil.calculator import DateCalculator
    from datetime import datetime

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Custom Package Demo:")

    # Using format_date function
    date_obj = datetime(2024, 6, 15)
    formatted_date = format_date(date_obj, "%B %d, %Y")
    print(f"Formatted Date: {formatted_date}")

    # Using DateCalculator class
    date_calc = DateCalculator()
    date1 = datetime(2024, 1, 1)
    date2 = datetime(2024, 6, 15)
    days_diff = date_calc.days_between(date1, date2)
    print(f"Days between {date1.date()} and {date2.date()}: {days_diff} days")
    
if __name__ == "__main__":
    # main()
    main_package()