def extract_vowels(text):
    vowels = "aeiouAEIOU"
    return [char for char in text if char in vowels]
# This is a list comprehension that extracts vowels from the input text.

"""
result = []
for char in text:
    if char in vowels:
        result.append(char)
"""

if __name__ == "__main__":
    print(extract_vowels("Data Engineering with Python"))
