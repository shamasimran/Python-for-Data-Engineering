def word_frequency(text):
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}

if __name__ == "__main__":
    print(word_frequency("Data Engineering with Python Python"))
