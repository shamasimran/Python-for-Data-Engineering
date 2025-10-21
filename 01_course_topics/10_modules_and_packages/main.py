"""
main.py
Demonstrates how to use custom modules and built-in packages in Python.
"""

# Importing our custom modules
import math_utils
import string_utils

# Importing a built-in package
import math

def main():
    # --- Using math_utils module ---
    print("Math Utilities Demo:")
    print(f"Add: 5 + 3 = {math_utils.add(5, 3)}")
    print(f"Subtract: 10 - 4 = {math_utils.subtract(10, 4)}")
    print(f"Multiply: 6 * 7 = {math_utils.multiply(6, 7)}")
    print(f"Divide: 8 / 2 = {math_utils.divide(8, 2)}")

    # --- Using string_utils module ---
    print("\nString Utilities Demo:")
    text = "Data Engineering"
    print(f"Original Text: {text}")
    print(f"Uppercase: {string_utils.to_uppercase(text)}")
    print(f"Lowercase: {string_utils.to_lowercase(text)}")
    print(f"Vowel Count: {string_utils.count_vowels(text)}")

    # --- Using built-in math module ---
    print("\nBuilt-in Math Module Demo:")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Pi constant: {math.pi}")
    print(f"Power: 2^3 = {math.pow(2, 3)}")

if __name__ == "__main__":
    main()
