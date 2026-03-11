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


## App Variables


## App Rules and Invariants


## App Bugs
