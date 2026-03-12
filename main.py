import random


WORD_LIST = [
    "python",
    "hangman",
    "variable",
    "function",
    "testing",
    "epita",
]


def choose_secret_word(word_list: list[str]) -> str:
    if not word_list:
        raise ValueError("Word list must not be empty.")
    return random.choice(word_list).lower()


def update_game_state(
    secret_word: str,
    guessed_letters: list[str],
    guess: str,
    lives: int,
) -> tuple[list[str], int, str]:
    if lives <= 0:
        return guessed_letters, 0, "Game over. No more guesses allowed."

    guess = guess.lower()
    secret_word = secret_word.lower()

    if len(guess) != 1 or not guess.isalpha():
        return guessed_letters, lives, "Invalid input. Please enter a single letter."

    normalized_guessed_letters = [letter.lower() for letter in guessed_letters]
    if guess in normalized_guessed_letters:
        return guessed_letters, lives, "You have already guessed that letter. Try again."

    if guess in secret_word:
        return guessed_letters + [guess], lives, "Correct guess!"

    return guessed_letters, max(lives - 1, 0), "Wrong guess. You lost a life."


def render_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    secret_word = secret_word.lower()
    guessed_letters = [g.lower() for g in guessed_letters]

    masked: list[str] = []
    for char in secret_word:
        if char in guessed_letters:
            masked.append(char)
        elif char.isalpha():
            masked.append("_")
        else:
            masked.append(char)

    return " ".join(masked)


def is_win(secret_word: str, guessed_letters: list[str]) -> bool:
    secret_word = secret_word.lower()
    guessed_letters = [g.lower() for g in guessed_letters]
    unique_letters = {char for char in secret_word if char.isalpha()}
    return unique_letters.issubset(set(guessed_letters))


def is_lose(lives: int) -> bool:
    return lives <= 0


def get_incorrect_guesses(secret_word: str, guessed_letters: list[str]) -> list[str]:
    secret_word_lower = secret_word.lower()
    incorrect: list[str] = []

    for guess in guessed_letters:
        if guess.lower() not in secret_word_lower:
            incorrect.append(guess)

    return incorrect


def render_state(
    secret_word: str,
    guessed_letters: list[str],
    lives: int,
) -> tuple[str, list[str], int]:
    masked_word = render_masked_word(secret_word, guessed_letters)
    incorrect_guesses = get_incorrect_guesses(secret_word, guessed_letters)
    return masked_word, incorrect_guesses, lives


def prompt_guess(guessed_letters: list[str]) -> str:
    guess = ""
    is_valid = False

    while not is_valid:
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        normalized_guessed = [letter.lower() for letter in guessed_letters]
        if guess in normalized_guessed:
            print("You already guessed that letter. Try another one.")
            continue

        is_valid = True

    return guess


def display_state(
    masked_word: str,
    guessed_letters: list[str],
    incorrect_guesses: list[str],
    lives: int,
    message: str,
) -> None:
    print("\nWord:", masked_word)
    print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
    print(
        "Incorrect guesses:",
        ", ".join(incorrect_guesses) if incorrect_guesses else "None",
    )
    print("Lives remaining:", lives)
    if message:
        print(message)


def prompt_replay() -> bool:
    answer = ""
    is_valid = False

    while not is_valid:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ["y", "yes"]:
            return True
        if answer in ["n", "no"]:
            return False
        print("Please enter y or n.")

    return False


def play_round(secret_word: str, max_lives: int = 6) -> tuple[list[str], int]:
    guessed_letters: list[str] = []
    lives = max_lives
    turn_message = ""
    round_active = True

    while round_active:
        masked_word, incorrect_guesses, current_lives = render_state(
            secret_word,
            guessed_letters,
            lives,
        )
        display_state(masked_word, guessed_letters, incorrect_guesses, current_lives, turn_message)

        if is_win(secret_word, guessed_letters):
            print("\nYou win! The word was:", secret_word)
            break

        if is_lose(lives):
            print("\nYou lose! The word was:", secret_word)
            break

        guess = prompt_guess(guessed_letters)
        guessed_letters, lives, turn_message = update_game_state(
            secret_word,
            guessed_letters,
            guess,
            lives,
        )

        round_active = not is_win(secret_word, guessed_letters) and not is_lose(lives)

    if is_win(secret_word, guessed_letters):
        return guessed_letters, lives

    print("\nFinal state:")
    masked_word, incorrect_guesses, current_lives = render_state(
        secret_word,
        guessed_letters,
        lives,
    )
    display_state(masked_word, guessed_letters, incorrect_guesses, current_lives, "")
    return guessed_letters, lives


def play_game(word_list: list[str], max_lives: int = 6) -> None:
    play_again = True

    while play_again:
        secret_word = choose_secret_word(word_list)
        play_round(secret_word, max_lives)
        play_again = prompt_replay()

    print("Thanks for playing!")


if __name__ == "__main__":
    play_game(WORD_LIST)
    
