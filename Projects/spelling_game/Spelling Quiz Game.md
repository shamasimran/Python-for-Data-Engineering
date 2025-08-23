# Spelling Quiz Game

## Objective
Test and improve spelling skills using a fun, interactive quiz based on grade-level word banks.

## How It Works
- The game randomly selects words from a grade-specific word bank.
- Some letters in each word are hidden (replaced with underscores).
- A hint (word meaning) is provided for each question.
- The player types the correct spelling to score points.

## Features
- Supports grades 1–7, each with a unique set of words and hints.
- Console screen clears between rounds for a clean experience.
- Final score displayed at the end.

## Example
```
Q1: Complete the spelling → s_h__l
💡 Hint: a place where children learn
Your spelling: school
✅ Correct!
```

## How to Run
```bash
python spelling_quiz.py
```
Follow the prompt to enter your grade (1–7) and start playing!

## Requirements
- Python 3.x

## Files
- [`spelling_quiz.py`](spelling_quiz.py): Main game logic.
- [`word_bank.py`](word_bank.py): Word lists and hints for