

def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

def my_county(country = "nowhere"):
  print("I am from " + country)

# If the number of arguments is unknown, add a * before the parameter name:
def my_kids(*kids):
  print("The youngest child is " + kids[2])

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

############################################################################################

text = "one@two@three"
parts = text.split("@")
print(parts)

print(parts[-3])  # "one"
print(parts[0])  # "one"

# Indexing in Python lists
    # parts[0] → "one"
    # parts[1] → "two"
    # parts[2] → "three"

# Python also supports negative indexes (counting from the end):
    # parts[-1] → "three" (last element)
    # parts[-2] → "two"
    # parts[-3] → "one"

print("test@example.com [is_valid_email]: ", is_valid_email("test@example.com"))
print("example.com [is_valid_email]: ", is_valid_email("example.com"))

############################################################################################
my_county("Pakistan")
my_county()

############################################################################################
my_kids("Muhammad", "Abdul-Muqeet", "Musa")

############################################################################################
my_function(5, 6, c = 7, d = 8)