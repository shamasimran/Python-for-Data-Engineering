import random
import os
from word_bank import word_bank   # ✅ Import word_bank dictionary from separate file

# -------------------------------
# Function to clear the console screen
# Works for both Windows (cls) and Linux/Mac (clear)
# -------------------------------
def clear_screen():
    if os.name == 'nt':   # Windows
        os.system('cls')
    else:                 # Mac/Linux
        os.system('clear')

# -------------------------------
# Function to hide some letters in a word
# Example: "school" -> "s_h__l"
# hide_ratio controls how much of the word is hidden (default = 50%)
# -------------------------------
def hide_letters(word, hide_ratio=0.5):
    letters = list(word)  # Convert word into list of characters
    total_to_hide = max(1, int(len(word) * hide_ratio))  # At least 1 letter hidden
    hide_positions = random.sample(range(len(word)), total_to_hide)  # Pick positions to hide

    for pos in hide_positions:
        letters[pos] = "_"   # Replace with underscore
    return "".join(letters)  # Rebuild the word with blanks

# -------------------------------
# Main spelling game logic
# grade: selects word list by grade
# total_questions: how many questions to ask (default = 25)
# -------------------------------
def spelling_game(grade, total_questions=25):
    if grade not in word_bank:
        print("❌ Sorry, this grade is not available yet.")
        return

    # Convert dictionary {word: meaning} into list of tuples [(word, meaning), ...]
    words = list(word_bank[grade].items())
    random.shuffle(words)  # Shuffle words for randomness
    score = 0

    # Ask 'total_questions' number of spelling questions
    for i in range(total_questions):
        if not words:
            break   # If no more words available, stop

        word, meaning = words.pop()  # Get one word and its meaning
        masked = hide_letters(word)  # Mask some letters

        # Display question with hint
        print(f"\nQ{i+1}: Complete the spelling → {masked}")
        print(f"💡 Hint: {meaning}")

        # Take user input and check answer
        answer = input("Your spelling: ").strip().lower()
        if answer == word:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct spelling is: {word}")

    # Final result after all questions
    print(f"\nFinal Score: {score}/{total_questions}")

# -------------------------------
# Entry point of the program
# Clears screen, asks for grade, and starts the game
# -------------------------------
if __name__ == "__main__":
    clear_screen()
    grade = int(input("Enter your grade (1-7): "))
    spelling_game(grade)
