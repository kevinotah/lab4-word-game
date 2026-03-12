def update_game_state(
    secret_word: str,
    guessed_letters: list[str],
    guess: str,
    lives: int) -> tuple[list[str], int, str]:
    
    if lives <= 0:
        lives = 0
        return guessed_letters, lives, "Game over. No more guesses allowed."
    
    guess = guess.lower()
    secret_word = secret_word.lower()
    
    if len(guess) != 1 or not guess.isalpha():
        return guessed_letters, lives, "Invalid input. Please enter a single letter."
    
    normalized_guessed_letters = [letter.lower() for letter in guessed_letters]
    
    if guess in normalized_guessed_letters:
        return guessed_letters, lives, "You have already guessed that letter. Try again."
    
    if guess in secret_word:
        new_guessed_letters = guessed_letters + [guess]
        return new_guessed_letters, lives, "Correct guess!"
    else:
        new_lives = max(lives - 1, 0)
        return guessed_letters, new_lives, "Wrong guess. You lost a life."
    
