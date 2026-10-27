# Python Quiz Engine

A console-based multiple-choice quiz application written in Python. The user answers each question by entering `a`, `b`, `c`, or `d`.

## Features

- Stores questions, options, answer keys, and hints using lists and dictionaries.
- Accepts answers without regard to letter case and ignores surrounding whitespace.
- Rejects invalid choices and asks the user to try again.
- Tracks correct and incorrect answers.
- Calculates the final score and percentage after a normally completed quiz.
- Uses a configurable passing threshold (`pass_percent`, currently 70%).
- Reviews missed questions and displays the correct answer and hint.
- Handles `Ctrl+C` by marking the quiz as incomplete and listing unanswered questions.
- Handles an empty question bank without attempting to divide by zero.

## Requirements

- Python 3 installed on your computer.

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python quiz.py
   ```

   On some Windows installations, use `py quiz.py` instead.
4. Enter one of the options `a`, `b`, `c`, or `d` when prompted.

## Question format

Each question is a dictionary containing the question text, an options dictionary, the correct answer key, and a hint. Add or edit questions in the `questions` list in `quiz.py`.

## Passing score

The passing percentage is configured by `pass_percent`. It is currently set to `70`, meaning the quiz passes when the final percentage is at least 70%.

## Project files

- `quiz.py` — Python source code for the quiz engine.
- `ALGORITHM.md` — algorithm and pseudocode.
- `TEST_CASES.md` — manual test cases and expected results.

## Notes

`TEST_CASES.md` describes tests to run manually. Mark a test as passed only after running it and confirming the observed result matches the expected result.
