"""
12_regular_expressions.py

This script demonstrates how to use Python's built-in 're' module 
for working with Regular Expressions (Regex).

Regex is a pattern-matching language used for:
- Validating strings (e.g., emails, phone numbers)
- Extracting data from text (e.g., log parsing)
- Replacing or cleaning text (e.g., removing unwanted characters)

Common data engineering use cases:
- Parsing semi-structured logs
- Cleaning messy data before ETL
- Extracting metadata from text fields
"""

import re


# 1. Validate Email Address
def validate_email(email):
    """Check if the given email address is valid."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


# 2. Validate Phone Number
def validate_phone(phone):
    """
    Validate phone numbers of format:
    - 1234567890
    - +92-300-1234567
    - (021) 9876543
    """
    pattern = r"^(\+?\d{1,3}[-\s]?)?(\(?\d{2,4}\)?[-\s]?)?\d{6,10}$"
    return bool(re.match(pattern, phone))


# 3. Extract Dates from Text
def extract_dates(text):
    """
    Extract date patterns like:
    - 2025-10-21
    - 21/10/2025
    - 10-21-2025
    """
    pattern = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})\b"
    return re.findall(pattern, text)


# 4. Parse Log Lines (simulate reading a log file)
def parse_logs(log_text):
    """
    Extract timestamps and log levels from a log string.
    Example input:
        2025-10-21 12:00:05 | INFO | Process started
        2025-10-21 12:00:06 | ERROR | File not found
    """
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| (\w+) \| (.+)"
    matches = re.findall(pattern, log_text)
    return [{"timestamp": ts, "level": lvl, "message": msg} for ts, lvl, msg in matches]


# 5. Clean Text (remove special characters, extra spaces)
def clean_text(text):
    """Remove non-alphanumeric characters and multiple spaces."""
    cleaned = re.sub(r"[^A-Za-z0-9\s]", "", text)  # Remove punctuation/symbols
    cleaned = re.sub(r"\s+", " ", cleaned).strip()  # Normalize whitespace
    return cleaned


# 6. Demonstration block
if __name__ == "__main__":
    print("Regex Demonstration:\n")

    # Email validation
    emails = ["user@example.com", "invalid-email@", "data.engineer@company.org"]
    for e in emails:
        print(f"{e} -> Valid: {validate_email(e)}")

    print("\nPhone validation:")
    phones = ["+92-300-1234567", "0219876543", "invalid-number"]
    for p in phones:
        print(f"{p} -> Valid: {validate_phone(p)}")

    print("\nExtracting dates:")
    text = "Events: 2025-10-21, 21/11/2024, and 10-22-2023 are scheduled."
    print(extract_dates(text))

    print("\nParsing logs:")
    logs = """2025-10-21 12:00:05 | INFO | Process started
2025-10-21 12:00:06 | ERROR | File not found
2025-10-21 12:00:08 | WARNING | Low memory"""
    print(parse_logs(logs))

    print("\nCleaning text:")
    dirty_text = "Hello@@@  Data   Engineer!!!   Welcome..."
    print(f"Before: {dirty_text}")
    print(f"After: {clean_text(dirty_text)}")
