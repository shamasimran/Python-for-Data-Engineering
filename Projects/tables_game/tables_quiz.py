import random
import threading
import queue
import os

def timed_input(prompt, timeout):
    """Get user input with timeout. Returns None if time runs out."""
    q = queue.Queue()

    def read_input():
        try:
            q.put(input(prompt))
        except EOFError:
            q.put(None)

    t = threading.Thread(target=read_input)
    t.daemon = True
    t.start()

    try:
        return q.get(timeout=timeout)
    except queue.Empty:
        return None

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Mac

def math_quiz(start, end, total_questions=10, time_limit=30):
    score = 0

    for i in range(1, total_questions + 1):
        a = random.randint(start, end)
        b = random.randint(1, 10)
        correct_answer = a * b

        print(f"\nQ{i}: {a} x {b} = ? (You have {time_limit} seconds)")

        user_input = timed_input("Your answer: ", time_limit)

        if user_input is None:  # Timeout
            print(f"⏰ Time’s up! Correct answer is {correct_answer}")
        elif user_input.isdigit() and int(user_input) == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {correct_answer}")

    print(f"\nFinal Score: {score}/{total_questions}")

if __name__ == "__main__":
    clear_screen()
    start = int(input("Enter start of table range: "))
    end = int(input("Enter end of table range: "))

    while True:  # keep restarting until N is pressed
        clear_screen()
        math_quiz(start, end)

        choice = input("\nDo you want to continue? (Y/N): ").strip().lower()
        if choice == 'n':
            print("👋 Thanks for playing! Goodbye.")
            break
        # if choice == 'y' → loop continues automatically
