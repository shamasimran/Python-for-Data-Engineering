"""
string_utils.py
A simple utility module for string operations.
"""

class StringHandler:
    """
    A utility class for common string handling operations.
    """

    def to_upper(self, text: str) -> str:
        """Convert string to uppercase."""
        return text.upper() if text else text

    def to_lower(self, text: str) -> str:
        """Convert string to lowercase."""
        return text.lower() if text else text
    
    def capitalize_words(self, text: str) -> str:
        """Capitalize the first letter of each word."""
        return text.title() if text else text

    def remove_whitespace(self, text: str) -> str:
        """Remove leading and trailing whitespace."""
        return text.strip() if text else text

    def remove_extra_spaces(self, text: str) -> str:
        """Remove multiple spaces and keep only single spaces."""
        return " ".join(text.split()) if text else text

    def replace_substring(self, text: str, old: str, new: str) -> str:
        """Replace a substring with another."""
        return text.replace(old, new) if text else text

    def extract_digits(self, text: str) -> str:
        """Extract only digits from a string."""
        return "".join(ch for ch in text if ch.isdigit()) if text else text

    def extract_letters(self, text: str) -> str:
        """Extract only letters from a string."""
        return "".join(ch for ch in text if ch.isalpha()) if text else text

    def is_palindrome(self, text: str) -> bool:
        """Check if a string is a palindrome."""
        if not text:
            return False
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]
    
    def count_vowels(self, text: str) -> int:
        """Count number of vowels in a string."""
        vowels = "aeiouAEIOU"
        return sum(1 for ch in text if ch in vowels) if text else 0

    def reverse_string(self, text: str) -> str:
        """Reverse the string."""
        return text[::-1] if text else text

    def remove_special_characters(self, text: str) -> str:
        """Remove special characters, keeping letters, numbers, and spaces."""
        import re
        return re.sub(r"[^a-zA-Z0-9\s]", "", text) if text else text
