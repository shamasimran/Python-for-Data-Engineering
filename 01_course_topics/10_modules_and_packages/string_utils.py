"""
string_utils.py
A simple utility module for string operations.
"""

def to_uppercase(text):
    """Convert a string to uppercase."""
    return text.upper()

def to_lowercase(text):
    """Convert a string to lowercase."""
    return text.lower()

def count_vowels(text):
    """
    Count the number of vowels in a given string.
    """
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)
