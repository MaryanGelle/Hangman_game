import random


print("Welcome to Hangman Game")

wordChoice = ("noise", "ears", "skin", "5", "25", "egypt", "up", "oxygen", "food", "summer")
chosen_word = random.choice(wordChoice)
print(chosen_word)

display = ""
for letter in chosen_word:
    display += '_'


print(display)
guessed_letter=input("guess a letter: ")


# choose a random word



def print_hangman(guesses):
    if guesses == 0:
        print("________    ")
        print("|      |    ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif guesses == 1:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif guesses == 2:
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
    elif guesses == 4:
        print("________    ")
        print("|      |    ")
        print("|      0    ")
        print("|     /|\   ")
        print("|           ")
        print("|           ")
    elif guesses == 5:
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

