def extract_vowels(text):
    vowels = "aeiouAEIOU"
    return [char for char in text if char in vowels]

if __name__ == "__main__":
    print(extract_vowels("Data Engineering with Python"))
