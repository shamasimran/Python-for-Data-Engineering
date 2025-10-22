import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
        
# The tri_recursion(k) function recursively sums all numbers from 1 to k and prints the cumulative total at each step.
# Output: 1, 3, 6, 10, 15, 21
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
  else:
    result = 0
  return result


# The factorial_recursive(n) function calculates the factorial of a number n using recursion.
# 5!=5×4×3×2×1=120
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

os.system('cls' if os.name == 'nt' else 'clear')
number = 5      
output = tri_recursion(number)
print(f"cumulative total of {number}: {output}" )
output = factorial_recursive(number)
print(f"factorial of {number}: {output}" )