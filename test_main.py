from main import (
    update_game_state,
    render_masked_word,
    is_win,
    is_lose,
    get_incorrect_guesses,
    render_state,
    choose_secret_word,
)

def test_game_over():
    letters, lives, message = update_game_state("python", ["p"], "y", 0)

    assert letters == ["p"]
    assert lives == 0
    assert message == "Game over. No more guesses allowed."
    
def test_invalid_input():
    letters, lives, message = update_game_state("python", [], "12", 5)

    assert letters == []
    assert lives == 5
    assert message == "Invalid input. Please enter a single letter."
    
def test_repeated_guess():
    letters, lives, message = update_game_state("python", ["p"], "p", 5)

    assert letters == ["p"]
    assert lives == 5
    assert message == "You have already guessed that letter. Try again."
    
def test_correct_guess():
    letters, lives, message = update_game_state("python", ["p"], "y", 5)

    assert letters == ["p", "y"]
    assert lives == 5
    assert message == "Correct guess!"
    
def test_wrong_guess():
    letters, lives, message = update_game_state("python", ["p"], "z", 5)

    assert letters == ["p"]
    assert lives == 4
    assert message == "Wrong guess. You lost a life."

def test_lives_never_negative():
    letters, lives, message = update_game_state("python", ["p"], "z", 1)

    assert lives == 0
    
def test_repeated_wrong_guess_no_life_loss():
    letters, lives, message = update_game_state(
        "python",
        ["p", "z"],  # z already guessed
        "z",
        5
    )

    assert letters == ["p", "z"]
    assert lives == 5
    assert message == "You have already guessed that letter. Try again."
    
def test_case_insensitive_guess():
    letters, lives, message = update_game_state(
        "Python",
        ["p"],
        "Y",
        5
    )

    assert letters == ["p", "y"]
    assert lives == 5
    assert message == "Correct guess!"
    
def test_negative_lives_game_over():
    letters, lives, message = update_game_state(
        "python",
        ["p"],
        "y",
        -3
    )

    assert letters == ["p"]
    assert lives == 0
    assert message == "Game over. No more guesses allowed."
    
def test_empty_string_input():
    letters, lives, message = update_game_state(
        "python",
        ["p"],
        "",
        5
    )

    assert letters == ["p"]
    assert lives == 5
    assert message == "Invalid input. Please enter a single letter."


# --- render_masked_word ---

def test_masked_word_no_guesses():
    assert render_masked_word("python", []) == "_ _ _ _ _ _"

def test_masked_word_some_guesses():
    assert render_masked_word("python", ["p", "y"]) == "p y _ _ _ _"

def test_masked_word_all_guesses():
    assert render_masked_word("python", ["p", "y", "t", "h", "o", "n"]) == "p y t h o n"

def test_masked_word_repeated_letters_all_revealed():
    # 'l' appears twice in 'letter'; both positions should reveal
    assert render_masked_word("letter", ["l"]) == "l _ _ _ _ _"

def test_masked_word_repeated_letter_fully_revealed():
    assert render_masked_word("letter", ["l", "e", "t", "r"]) == "l e t t e r"

def test_masked_word_case_insensitive():
    assert render_masked_word("Python", ["p", "y"]) == "p y _ _ _ _"

def test_masked_word_length_preserved():
    result = render_masked_word("python", [])
    tokens = result.split(" ")
    assert len(tokens) == len("python")


# --- is_win ---

def test_is_win_all_letters_guessed():
    assert is_win("python", ["p", "y", "t", "h", "o", "n"]) is True

def test_is_win_not_all_letters_guessed():
    assert is_win("python", ["p", "y", "t"]) is False

def test_is_win_extra_wrong_guesses_irrelevant():
    assert is_win("cat", ["c", "a", "t", "z", "x"]) is True

def test_is_win_empty_guesses():
    assert is_win("python", []) is False

def test_is_win_repeated_letters_satisfied_once():
    # 'letter' has repeated t and e; guessing each letter once should win
    assert is_win("letter", ["l", "e", "t", "r"]) is True

def test_is_win_case_insensitive():
    assert is_win("Python", ["p", "y", "t", "h", "o", "n"]) is True


# --- is_lose ---

def test_is_lose_at_zero():
    assert is_lose(0) is True

def test_is_lose_negative():
    assert is_lose(-2) is True

def test_is_lose_with_lives_remaining():
    assert is_lose(3) is False

def test_is_lose_one_life_left():
    assert is_lose(1) is False


# --- get_incorrect_guesses ---

def test_get_incorrect_guesses_none_wrong():
    assert get_incorrect_guesses("python", ["p", "y"]) == []

def test_get_incorrect_guesses_some_wrong():
    result = get_incorrect_guesses("python", ["p", "z", "q"])
    assert result == ["z", "q"]

def test_get_incorrect_guesses_order_preserved():
    result = get_incorrect_guesses("python", ["z", "p", "x"])
    assert result == ["z", "x"]

def test_get_incorrect_guesses_all_wrong():
    result = get_incorrect_guesses("python", ["a", "b", "c"])
    assert result == ["a", "b", "c"]

def test_get_incorrect_guesses_case_insensitive():
    result = get_incorrect_guesses("Python", ["Z", "P"])
    assert result == ["Z"]


# --- render_state ---

def test_render_state_returns_tuple():
    masked, incorrect, lives = render_state("python", ["p", "z"], 5)
    assert masked == "p _ _ _ _ _"
    assert incorrect == ["z"]
    assert lives == 5

def test_render_state_lives_passthrough():
    _, _, lives = render_state("python", [], 3)
    assert lives == 3


# --- choose_secret_word ---

def test_choose_secret_word_from_list():
    words = ["alpha", "bravo", "charlie"]
    result = choose_secret_word(words)
    assert result in words

def test_choose_secret_word_is_lowercase():
    result = choose_secret_word(["Python", "HANGMAN"])
    assert result == result.lower()

def test_choose_secret_word_empty_list_raises():
    import pytest
    with pytest.raises(ValueError):
        choose_secret_word([])