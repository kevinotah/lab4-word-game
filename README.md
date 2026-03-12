# Lab 4 — Hangman Word Game

A fully tested, pure-function implementation of the classic Hangman word-guessing game written in Python. Built as part of the AI4SE (AI for Software Engineering) course at EPITA, this project demonstrates functional programming principles, clean code design, pytest-based testing, and the use of GitHub Copilot as a Socratic AI tutor.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Game Rules](#game-rules)
4. [How the Code Works](#how-the-code-works)
   - [Core Game Logic](#core-game-logic)
   - [I/O & Display Layer](#io--display-layer)
   - [Game Loop](#game-loop)
5. [Prerequisites](#prerequisites)
6. [Setup & Installation](#setup--installation)
7. [How to Run the Game](#how-to-run-the-game)
8. [How to Run the Tests](#how-to-run-the-tests)
   - [Test Coverage Overview](#test-coverage-overview)
9. [Design Decisions](#design-decisions)
10. [Known Limitations](#known-limitations)

---

## Project Overview

This project implements a terminal-based Hangman game. The player is given a secret word chosen at random from a built-in word list. They must guess the word one letter at a time within a limited number of lives (default: 6). Each incorrect guess costs one life. The player wins by revealing all letters before running out of lives.

The codebase is organised around **pure functions**: each core logic function takes its inputs as arguments and returns new values without mutating state or producing side effects. I/O (printing and input prompts) is isolated to dedicated display/input functions, keeping the game logic independently testable.

---

## Project Structure

```
lab4-word-game/
├── main.py           # All game logic, I/O helpers, and the main game loop
├── test_main.py      # 37 pytest tests covering all core functions
├── MY_NOTES.md       # Developer notes: app states, variables, rules, and edge cases
├── REPORT.md         # Project reflection: learnings, AI experience, testing notes
├── JOURNAL.md        # Auto-generated interaction log (maintained by the journal-logger agent)
└── README.md         # This file
```

---

## Game Rules

| Rule | Detail |
|------|--------|
| Secret word | Randomly chosen from the built-in word list |
| Input | One alphabetic letter per turn |
| Correct guess | All matching letters are revealed in the word |
| Incorrect guess | Player loses one life |
| Repeated guess | Flagged with a message; does **not** cost a life |
| Invalid input | Flagged with a message; does **not** cost a life |
| Win condition | All unique letters of the secret word have been guessed |
| Lose condition | Lives reach zero |
| Default lives | 6 |
| Case sensitivity | All input is normalised to lowercase internally |

---

## How the Code Works

### Core Game Logic

All functions below are **pure** — they produce no side effects and can be tested in full isolation.

#### `choose_secret_word(word_list)`
Randomly selects one word from the provided list and returns it in lowercase. Raises `ValueError` if the list is empty.

#### `update_game_state(secret_word, guessed_letters, guess, lives)`
The central state-transition function. Given the current game state and a new guess, it returns a tuple of `(updated_guessed_letters, updated_lives, message)`:

- If `lives <= 0` → returns immediately with a game-over message.
- If `guess` is not a single alpha character → invalid input, no state change.
- If `guess` already in `guessed_letters` → repeated guess, no state change.
- If `guess` is in `secret_word` → appends guess, keeps lives.
- Otherwise → keeps letters, decrements lives by 1 (minimum 0).

#### `render_masked_word(secret_word, guessed_letters)`
Returns a space-separated string displaying guessed letters in their correct positions and `_` for every unrevealed letter. Example:
```
render_masked_word("python", ["p", "y"])  →  "p y _ _ _ _"
```

#### `is_win(secret_word, guessed_letters)`
Returns `True` if every unique alphabetic character in `secret_word` is present in `guessed_letters`. Extra wrong guesses do not prevent a win.

#### `is_lose(lives)`
Returns `True` if `lives <= 0`.

#### `get_incorrect_guesses(secret_word, guessed_letters)`
Returns a list of every letter in `guessed_letters` that does **not** appear in `secret_word`, preserving the order they were guessed.

#### `render_state(secret_word, guessed_letters, lives)`
Convenience aggregator. Returns a tuple of `(masked_word, incorrect_guesses, lives)` by combining `render_masked_word` and `get_incorrect_guesses`.

---

### I/O & Display Layer

These functions handle all terminal interaction and are **not** covered by unit tests (they require live input/output).

#### `prompt_guess(guessed_letters)`
Loops until the player enters a valid, un-guessed single letter. Returns the normalised lowercase letter.

#### `display_state(masked_word, guessed_letters, incorrect_guesses, lives, message)`
Prints the current game board to the terminal: the masked word, all guessed letters, incorrect guesses, remaining lives, and any feedback message.

#### `prompt_replay()`
Asks the player if they want to play again (`y`/`n`). Loops on invalid input. Returns `True` for yes, `False` for no.

---

### Game Loop

#### `play_round(secret_word, max_lives=6)`
Runs one complete round for a given secret word. At the start of each turn it renders state, checks win/lose conditions, prompts for a guess, and calls `update_game_state`. Returns `(guessed_letters, lives)` when the round ends.

#### `play_game(word_list, max_lives=6)`
The top-level entry point. Picks a secret word, calls `play_round`, then asks the player via `prompt_replay` whether to play again. Continues until the player declines.

---

## Prerequisites

- **Python 3.10+** (uses `list[str]` and `tuple[...]` built-in generics introduced in 3.9+)
- **pytest** (for running tests)

---

## Setup & Installation

```bash
# 1. Clone or navigate to the project folder
cd lab4-word-game

# 2. (Recommended) Create and activate a virtual environment
python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate

# 3. Install test dependencies
pip install pytest
```

> If the project ships with a `requirements.txt`, run `pip install -r requirements.txt` instead of step 3.

---

## How to Run the Game

```bash
python main.py
```

You will see output like:

```
Word: _ _ _ _ _ _
Guessed letters: None
Incorrect guesses: None
Lives remaining: 6

Enter a letter: p

Word: p _ _ _ _ _
Guessed letters: p
Incorrect guesses: None
Lives remaining: 6
Correct guess!

Enter a letter: ...
```

The game loops until you either win, lose, or choose not to play again.

---

## How to Run the Tests

```bash
# Run all tests with verbose output
pytest test_main.py -v

# Run with a short summary of results
pytest test_main.py

# Run a specific test by name
pytest test_main.py::test_is_win_all_letters_guessed -v
```

Expected output (all passing):

```
============================= test session starts ==============================
collected 37 items

test_main.py::test_game_over                              PASSED
test_main.py::test_invalid_input                          PASSED
test_main.py::test_repeated_guess                         PASSED
...
test_main.py::test_choose_secret_word_empty_list_raises   PASSED

============================== 37 passed in 0.XXs ===============================
```

### Test Coverage Overview

| Function | # Tests | Edge Cases Covered |
|---|---|---|
| `update_game_state` | 10 | Game over at 0 lives, invalid input, repeated guess, correct/wrong guess, lives never go negative, case-insensitive input, negative lives, empty string input |
| `render_masked_word` | 7 | No guesses, partial guesses, all revealed, repeated letters, case-insensitive, length preserved |
| `is_win` | 6 | All letters guessed, partial guesses, extra wrong guesses, empty guesses, repeated letters, case-insensitive |
| `is_lose` | 4 | Zero lives, negative lives, lives remaining, one life left |
| `get_incorrect_guesses` | 5 | No wrong guesses, some wrong, order preserved, all wrong, case-insensitive |
| `render_state` | 2 | Returns correct tuple, lives passthrough |
| `choose_secret_word` | 3 | Result in list, result is lowercase, empty list raises `ValueError` |
| **Total** | **37** | |

---

## Design Decisions

- **Pure functions for game logic:** All state transitions are handled by functions that return new values rather than mutating variables. This makes each function individually testable without needing a running game instance.

- **Separation of concerns:** Game logic (`update_game_state`, `is_win`, etc.) is completely separated from I/O (`display_state`, `prompt_guess`). This follows the principle that functions should do one thing.

- **No global mutable state:** The game state (`guessed_letters`, `lives`) is passed explicitly through function arguments and return values, avoiding hidden dependencies.

- **Case normalisation at the boundary:** Both `secret_word` and `guess` inputs are lowercased at the start of each function, ensuring consistent comparisons throughout without requiring callers to pre-normalise.

- **Lives floor at zero:** `update_game_state` uses `max(lives - 1, 0)` to prevent lives from going negative, maintaining an invariant that `is_lose` can rely on a clean `<= 0` check.

---

## Known Limitations

- The built-in word list is short (6 words). In a production version this would be loaded from an external file or API.
- The game has no ASCII art hangman diagram — it is purely text-based.
- `prompt_guess`, `display_state`, `prompt_replay`, `play_round`, and `play_game` are not covered by automated tests because they depend on `input()` / `print()`. Mocking these with `unittest.mock` would be a natural next step.
- There is no persistence — scores and history are not saved between sessions.
