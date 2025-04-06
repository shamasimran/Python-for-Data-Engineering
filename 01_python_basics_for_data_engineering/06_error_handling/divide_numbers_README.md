# Safe Division with Error Handling

## Objective:
The goal of this exercise is to safely handle **division by zero errors**.

## Approach:
- We define a function `safe_divide()` that accepts two numbers, `a` and `b`.
- It attempts to divide `a` by `b`. If `b` is zero, a `ZeroDivisionError` is caught, and a message `"Cannot divide by zero"` is returned instead.

### Example:
Input: `10 / 0`

Output: `"Cannot divide by zero"`

## How to Run:
```bash
python error_handling/divide_numbers.py
```
