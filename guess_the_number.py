#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program gets the user to guess a number correctly or incorrectly

import constants


def main():
    # this function checks if the guess is correct

    # input
    user_guess = int(input("Enter a number between 0-9: "))
    print("")

    # process & output
    if user_guess != constants.GUESSING_NUMBER:
        print("Your guess is incorrect. Try again!")

    if user_guess == constants.GUESSING_NUMBER:
        print("Your guess is correct!")

        print("\nDone.")


if __name__ == "__main__":
    main()
