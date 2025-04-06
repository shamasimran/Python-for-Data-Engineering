# Validate Email Address

## Objective:
The goal of this exercise is to validate whether a given email address has a valid format.

## Approach:
- We define a function `is_valid_email()` that accepts an email address as input.
- The function checks whether the email contains an "@" symbol and a "." symbol in the domain part.
- It returns `True` if the email is valid, otherwise `False`.

### Example:
Input: `"test@example.com"`

Output: `True`

## How to Run:
```bash
python functions/validate_email.py
```
