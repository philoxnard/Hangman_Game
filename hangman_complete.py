# A program to emulate the game "Hangman"

###################################################################

# The program will determine a word for the user to guess
# The user will then, letter by letter, try to guess the word
# If the user guesses the word in the alloted number of lives, she wins
# If the user fails to guess the word and exhausts her life total, she loses
# The user can then play the game again or exit the program

###################################################################

# Imports for the game

import random

# Functions for the game

def welcome():
    # Displays a happy welcome message to explain the game to the user
    print("Welcome to peeup's hangman!")
    print("The program will generate a word for you to guess.")
    print("It will then ask you how many lives you want to have.")
    print("You must then, letter by letter, guess the mystery word.")
    print("If you guess the word, you win!")
    print("If you run out of lives, you lose :(")
    print("Good luck!")

def get_guess_list():
    # Generates an empty list that will store all of the user's guesses
    guess_list = []
    return guess_list

def get_magic_word():
    # Function to get the magic word for the game
    # Generates it from this prexisting list of random words
    # Could be changed to pull from a separate document, website, etc.
    magic_word_list = [
        "bigger", "duckling", "bog", "egress", "wick", "lynx", "candle",
        "maroon", "frigate", "moose", "dodge", "robust", "terror", "grapefruit",
        "gentleman", "trebuchet", "order", "challenge", "igloo", "monster"]
    magic_word_list_max = len(magic_word_list) - 1
    random_number = random.randint(0, magic_word_list_max)
    magic_word = magic_word_list[random_number]
    return magic_word

def get_lives():
    # Function to prompt the user for how many lives they want to have
    # Gives the user error messages until a proper number has been given
    lives_check = 0
    while lives_check == 0:
        lives = input("\nHow many lives would you like to play with? ")
        if lives.isdigit() == False:
            print("Error: Please input only positive integers.")
        elif int(lives) < 1:
            print("Error: You must have at least 1 life.")
        elif int(lives) > 10:
            print("Error: Don't be a weenie, no more than 10 lives.")
        else:
            lives_check = 1
    print("Great, I'll give you " + str(lives) + " lives.")
    return int(lives)

def get_hidden_word(magic_word):
    # Function to copy the magic word into another variable called hidden word
    # The magic word will remain the same throughout the game
    # The hidden word will be maniupulated as the user guesses letters
    hidden_word = []
    for i in magic_word:
        hidden_word.append("_")
    return hidden_word

def get_guess(guess_list):
    # Function to get the user's guess
    # Repeats the question until user gives an appropriate guess
    guess_check = 0
    while guess_check == 0:
        guess = input("\nWhat letter do you guess? ")
        if guess.isalpha() == False:
            print("Error: Please input only letters.")
        elif len(guess) > 1:
            print("Error: Please only input one letter.")
        elif guess in guess_list:
            print("Error: You've already guessed that letter.")
        else:
            guess_check = 1
            print("\n.........")
            guess_list.append(guess)
    return guess.lower(), guess_list


def check_guess(guess, hidden_word, magic_word):
    # Function to see if the user's guess is in the magic word
    # If it is, it replaces the appropriate underscore in the hidden word
    index = 0
    while index < len(hidden_word):
        for i in hidden_word:
            if guess == magic_word[index]:
                hidden_word[index] = guess
            index += 1

def reduce_lives(guess, lives):
    # Function to check if the guess was correct
    # If not, reduce lives by one
    # If it is, give a congratulations message
    if guess not in magic_word:
        lives -= 1
        print("\nI'm sorry, there is no '" + guess + "' in the mystery word.")
    else:
        print("\nCorrect! '" + guess + "' appears in the mystery word!")
    return lives

def show_lives(lives):
    # Function to show the user how many lives they have left
    print("\nLives remaining: " + str(lives))
    print_line()

def show_hidden_word(hidden_word, magic_word):
    # Function to display the correctly guessed letters to the user
    # Takes the list hidden_word and converts it to a nicely formatted string
    print("\nThe mystery word: ")
    hidden_word_string = ""
    for i in hidden_word:
        hidden_word_string += i.upper() + " "
    win = check_win(hidden_word_string, magic_word)    
    print(hidden_word_string)
    return win

def check_win(hidden_word_string, magic_word):
    # Function to check if the player has won
    # Checks by seeing if there are any more underscores in the hidden word
    if "_" not in hidden_word_string:
        return True

def play_again():
    # Function to ask the player if they want to replay or play again
    # Prompts the user until they give an appropriate answer
    play_again_check = 0
    while play_again_check == 0:
        print("Would you like to play again?")
        play_again = input("Type 'y' to play again or 'n' to quit. ")
        if play_again.lower() == "n":
            play_again_check = 1
            print("Thanks for playing!")
            answer = 0
        elif play_again.lower() == "y":
            play_again_check = 1
            answer = 1
            print_line()
        else:
            print("\nError: Please input 'y' or 'n'.")
    return answer
    

def end_game_message(win, magic_word):
    # Function to print the appropriate message when the game is over
    if win == True:
        print("\nGood game! You win!")
    else:
        print("\nThe mystery word was: " + magic_word.upper())
        print("you lose!")
        print("idiot!")

def print_line():
    # Function to print a line of uniform length
    print("_______________________________________________")


###################################################################

# Set win condition to False
# Will become true if they correctly guess the magic word
win = False

# Repeat is 1 so that they have the option to play again
# If they complete the game and opt to not play again, repeat becomes 0 and game ends
repeat = 1

# Plays a welcome message to the user, explaining the rules
welcome()

# Greater loop of the game

while repeat == 1:

    # Functions to initialize the game
    # Generates an empty list that will fill up as user guesses letters
    # Gets the magic word from a list
    # Gets the lives from user input
    # Then generates the hidden word as a blank copy of the magic word
    
    guess_list = get_guess_list()
    magic_word = get_magic_word()
    lives = get_lives()
    hidden_word = get_hidden_word(magic_word)
    show_hidden_word(hidden_word, magic_word)

    # Main loop of the game:
        # Take the player's guess
        # Check to see if the guess is in the magic word
        # If it is, replace its respective spot in the hidden word
        # If not, reduce lives by one
        # Check to see if the game has been won
        # If so, break out of the main loop and back out to the greater loop
    
    while lives > 0:
        guess, guess_list = get_guess(guess_list)
        check_guess(guess, hidden_word, magic_word)
        lives = reduce_lives(guess, lives)
        show_lives(lives)
        win = show_hidden_word(hidden_word, magic_word)
        if win == True:
            break

    # Prints a game over message depending on if the user won or lost
    # Asks the player if they would like to play again
    # If yes, it starts back at the top of the greater loop
    # If not, it ends the program
    
    end_game_message(win, magic_word)
    repeat = play_again()

# End of program
