# Hangman Game

The Hangman game is a simple word-guessing game where the player needs to guess the letters of a secret word. The player has a limited number of attempts to guess the correct word, and for each incorrect guess, a part of a hangman is drawn. The game ends when the player either guesses the word correctly or the hangman is completed.

## How to Play

1. Run the Hangman game by executing the `hangman.py` script using Python.
2. Choose a word level (easy/intermediate/difficult) to get started.
3. You have six chances to guess the letters of the secret word.
4. Enter a single letter as your guess.
5. If the letter is part of the secret word, it will be revealed. Otherwise, a part of the hangman is drawn.
6. Continue guessing letters until you either guess the complete word or the hangman is completed.
7. If you run out of attempts, the game ends, and the hangman is fully drawn, resulting in a loss.
8. After each game, you will be asked if you want to play again.

## Play the Game Online

You can play the Hangman game online by visiting the live app deployed on Heroku:

**Play Here:** [https://thehangman-game-c4850bfdcf57.herokuapp.com/](https://thehangman-game-c4850bfdcf57.herokuapp.com/)

Please ensure you have JavaScript enabled in your browser for the best experience.

## Word Levels

The Hangman game offers three levels of difficulty:
- Easy: Words related to common objects and everyday life.
- Intermediate: Words with a moderate level of difficulty.
- Difficult: More challenging words for advanced players.

## Dependencies

The Hangman game is implemented using Python and Flask as the web framework. Ensure you have the following dependencies installed:

- Python 3.x
- Flask (can be installed using `pip`)

```bash
pip install Flask
