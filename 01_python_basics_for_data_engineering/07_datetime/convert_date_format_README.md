# Convert Date Format

## Objective:
The goal of this exercise is to convert a date from one format to another.

## Approach:
- We define a function `convert_date_format()` that accepts a date string, the original format, and the target format.
- The function uses Python's `datetime` module to parse the input string into a `datetime` object and then formats it to the desired output.

### Example:
Input: `"2025-04-06"` (original format `%Y-%m-%d`)

Output: `"06/04/2025"` (new format `%d/%m/%Y`)

## How to Run:
```bash
python datetime/convert_date_format.py
```
