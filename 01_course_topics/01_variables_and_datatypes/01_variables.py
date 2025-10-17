# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x1 = 4       # x1 is of type int
x1 = "Sally" # x1 is now of type str
print(x1)


# If you want to specify the data type of a variable, this can be done with casting.
x11 = str(3)    # x11 will be '3'
y11 = int(3)    # y11 will be 3
z11 = float(3)  # z11 will be 3.0


# You can get the data type of a variable with the type() function.
print(type(x11))
print(type(z11))

# String variables can be declared either by using single or double quotes:


"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""


# Python allows you to assign values to multiple variables in one line:
x111, y111, z111 = "Orange", "Banana", "Cherry"
print(f"x: {x111} y: {y111} z: {z111}")


# And you can assign the same value to multiple variables in one line:
fname = lname = name = "Shamas"

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
a1, b1, c1 = fruits
print(a1)
print(b1)
print(c1)


# The Python print() function is often used to output variables.


# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
# If you use the global keyword, the variable belongs to the global scope
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.
# Global variables can be used by everyone, both inside of functions and outside.

g = "shamas"
h = "imran"

def myfunc():
  g = "Irfan"
  i = "Khan"
  global j
  j = "Muhammad"
  print("Inside Function ==> g: " + g, "h: " + h, "i: " + i)

myfunc()
print("After Function ==> g: " + g, "h: " + h, "j: " + j) # i is not available outside function (local to func)



