
# A comprehension is a concise way to create new lists, sets, or dictionaries from existing iterables (like lists, tuples, or strings) 
# — often replacing longer for loops with a single readable line.

def square_even_numbers(nums):
    return [x**2 for x in nums if x % 2 == 0]

if __name__ == "__main__":
    print(square_even_numbers([1, 2, 3, 4, 5, 6]))

numbers = [1, 2, 3, 4, 5]
squares_dict = {n: n**2 for n in numbers}
print(squares_dict)

marks = {"Alice": 85, "Bob": 70, "Carol": 92}
passed = {name: score for name, score in marks.items() if score >= 80}
print(passed)

matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)
