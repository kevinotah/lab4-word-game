from main import update_game_state

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