import random


def print_hangman(guesses):
    if guesses == 6:
        print("________    ")
        print("|      |    ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif guesses == 5:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif guesses == 4:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|      |    ")
        print("|           ")
        print("|           ")
    elif guesses == 3:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|     /|    ")
        print("|           ")
        print("|           ")
    elif guesses == 2:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|     /|\   ")
        print("|           ")
        print("|           ")
    elif guesses == 1:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|     /|\   ")
        print("|     /     ")
        print("|           ")
    else:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|     /|\   ")
        print("|     / \   ")
        print("|           ")
        print("Wrong answer hanged the man")
        print("Game over!")
     # Add the unit information for incorrect guesses
    print(f"You have {guesses} {'tries' if guesses > 1 else 'try'} left.")
def guesses_left(guesses):
    return guesses

def hangman():
    # List of words to choose from 
    wordChoice = ["noise", "ears", "skin", "sick", "happy", "egypt", "up", "oxygen", "food", "summer"]

    # Select a random word from the list 
    chosen_word = random.choice(wordChoice)

    # Game state
    guesses = 6
    guessed_letters = []

    while guesses > 0:
        # Print hangman
        print_hangman(guesses)

        # Print the currently guessed word with underscores for missing letters
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        # Prompt the user for a letter guess
        guess = input("Guess a letter: ")
        
        # Check if the input is a valid single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        # Check if the guessed letter is correct
        if guess in chosen_word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            guesses -= 1
        
        # Add the guessed letter to the list of guessed_letters
        guessed_letters.append(guess)


        # Check if the player has won
        if all(letter in guessed_letters for letter in chosen_word):
            print("Congratulations! You won! The word was correct")
            break
    
    # If the player ran out of guesses, they lose the game
    if guesses == 0:
        print("Sorry, you lost the game.")

    # Ask the user if they want to play again
    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    if play_again_input == "yes":
        # Clear the guessed_letters list for the next game
         guessed_letters.clear()
         
    else:
        print("Thank you for taking your time playing our Hangman game!")

hangman()
