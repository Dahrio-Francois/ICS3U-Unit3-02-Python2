#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets you play a number guessing game
#   with user input


import constants


def numberGuess():
    # this program starts the game

    # process
    print("Enter your guess between 0 & 9")
    guessed = 0
    while guessed != constants.NUMBER:
        guessed = int(input("\nTry to guess it: "))
        if guessed == constants.NUMBER:

            # output
            print("\nCorrect! You guessed the right number!")
            print("\nDone")

        elif guessed != constants.NUMBER:
            print("\nIncorrect! Try again?")


if __name__ == "__numberGuess__":
    numberGuess()
