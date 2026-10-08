# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that lets a player guess letters to reveal a hidden word before running out of attempts. This assignment reinforces string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Create the game setup

#### Description
Set up the game so it chooses a secret word, displays blanks for each letter, and prompts the player for guesses.

#### Requirements
Completed program should:

- Use a predefined list of words and randomly choose one for each round
- Display the hidden word as underscores or blanks, such as _ _ _ _ _
- Accept single-letter guesses from the user
- Update the displayed word after a correct guess
- Keep track of incorrect guesses and remaining attempts

### 🛠️ Add game logic and end conditions

#### Description
Implement the core game loop so the player can keep guessing until they either win or lose.

#### Requirements
Completed program should:

- Continue asking for guesses until the word is fully revealed or attempts run out
- Prevent repeated guesses from counting twice
- Show feedback after each guess, including correct or incorrect letters
- End the game with a clear win message when the word is solved
- End the game with a clear loss message when the player runs out of attempts
