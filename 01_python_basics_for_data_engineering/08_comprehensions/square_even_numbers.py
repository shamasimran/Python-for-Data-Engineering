def square_even_numbers(nums):
    return [x**2 for x in nums if x % 2 == 0]

if __name__ == "__main__":
    print(square_even_numbers([1, 2, 3, 4, 5, 6]))
