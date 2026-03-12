# My Original Thinking

## App States
- In a game like Hangman, there should an initial state where the program shows a word with several letters hidden. Then, it should be able to show that word again but with any letters the user guessed revealed. Perhaps a while loop can be employed to track the number of turns and also the number of letters left to complete the word. There should also exist a state where the game ends and the user loses (ie doesn't guess all the letters correctly). The final state, if all goes well, shoould be when the user guesses all the letters and the full word is revealed.

## App Variables
Variables required include but are most likely not limited to:
- words = [**list, of, words**]
- number_of_turns = 6 (default)
- perhaps a flag? like win = False (stays False until user wins, then changes to True)
- for each word, maybe a dictionary of the missing letters and their indices within the word to be guessed. (I don't know how to actually implement this but it seems like a possible way to do it)
- We should also keep track of the guessed letters and remove them from the dictionary

## App Rules and Invariants
- Can't go more than 6 tries/turns
- Have to guess all the letters within the number of turns

## App Bugs and Edge Cases
- There could be a problem where a letter appears more than once and the program only uncovers it once
- The program could penalise a user for a guessing an already guessed letter and count it as a turn instead of just informing the user that the letter has already been guessed.


# CoPilot Suggestions

## App States
- Setup: pick random word, reset all variables.
- Input: Prompt the user for a letter.
- Process Guess: Check if letter is in the word and update variables like revealed letters, turns, guessed letters etc depending on whether or not the letter is in the word.
- Check end condition: Check number of turns or if word has been guessed.
- Win/Lose: Reveal full word and either congratulate player or tell him/her how close they came to figuring out the word.
- Replay/Exit: Prompt the user on whether to play again or exit the program.

## App Variables
- the secret word
- the current revealed version of the word
- the set/list of guessed words
- number of remaining turns
- perhaps the wrong guesses as well

## App Rules and Invariants
Rules:
- The player guesses one letter at a time.
- The input must be a single alphabetic character.
- A correct guess reveals every occurrence of that letter in the word.
- An incorrect new guess reduces the remaining turns by 1.
- A repeated guess should not reduce turns; it should just inform the player.
- The player wins when all letters in the word are revealed.
- The player loses when remaining turns reaches 0.

Invariants:
- Remaining turns is always between 0 and the maximum allowed turns.
- The revealed word always has the same length as the secret word.
- A revealed position must always match the corresponding letter in the secret word.
- Hidden positions stay hidden until their letter has been guessed.
- Guessed letters should not contain duplicates.
- If a letter has been guessed correctly, all matching positions in the word should be revealed, not just one.
- The game cannot be both won and lost at the same time.
- Both uppercase and lowercase guesses count the same, but the stored guesses are normalised to lowercase.

## App Bugs
- Input bugs: What happens when the user input is not a letter or is more than one letter?
- Repeated guess bugs: What if the player guesses a right (or wrong) letter twice? Does the program remove a turn?
- Word reveal bugs: A correct guess could get hidden again. The wrong letter might get revealed. A repeated letter might only be revealed once
- Turn count bugs: Game could continue even if there are no turns left. Turns could go negative. Game could remove a turn for a correct guess
- Win/lose bugs: Player could "win" when some letters are still hidden. Win and lose conditions might be true at the same time.
- State tracking bugs: Does the guessed letters variable allow duplicates? Guessed letters and wrong guesses may not be tracked consistently.
- Word selection bugs: There could be problems with the word list. It could be empty, for instance. The word itself could contain spaces or punctuation when the game expects letters.