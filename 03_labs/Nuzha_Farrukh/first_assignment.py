# First Python Assignment
# Author: Your Name
# Date: YYYY-MM-DD

# This program takes a user's name and age, then prints a personalized message.

# Step 1: Take input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")

# Step 2: Convert age to an integer (optional)
try:
    age = int(age)
except ValueError:
    print("Please enter a valid number for age.")
    exit()

# Step 3: Print a friendly message
print(f"\nHello, {name}! You are {age} years old.")

# Step 4: Simple logic demonstration
if age < 18:
    print("You're still young — enjoy learning Python!")
elif age < 60:
    print("Keep going strong — learning never stops!")
else:
    print("It's wonderful to see lifelong learners like you!")
