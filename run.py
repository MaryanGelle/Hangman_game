import random
score = {} # Store scores
play = True  # Declare the global variable 'play'



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
    global play  # Declare 'play' as global to modify its value inside the function.  Use the global 'play' variable in the loop condition.

    # Ask for the player's username only once at the beginning of the first game
    if "username" not in globals():
        username = input("Enter your username: ")
        
    level = input("Choose a word level (easy/intermediate/difficult): ").lower()
        
    # Dictionary to hold word choices for each category
    word_choices = {
        "easy": ["food", "down", "happy", "eat", "run", "west", "money", "sweet", "mango"],
        "intermediate": ["Internet", "Dangerous", "connection", "worldwide", "Assumption", "Pandemic", "switch", "colonial"],
        "difficult": ["appraise", "ambiguous", "nauseous", "Indict", "Sherbet", "Ingenious"]
    }

    # Select a random word from the chosen level
    chosen_word = random.choice(word_choices.get(level, []))

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
    play_again_input = input("Do you want to play again? Type 'y' for yes and 'n' for no. ").upper()
    return play_again_input == "y"



# Start the game loop
while play:
    hangman()

print("Thank you for taking your time playing our Hangman game!")
