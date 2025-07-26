# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:01:48 2025

@author: reddy
"""

import random

def hangman():
    words = ["python", "hangman", "programming", "computer", "developer"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    display_word = ["_" for _ in secret_word]
    print("Welcome to Hangman!")
    print(" ".join(display_word))

    while "_" in display_word and incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        print(" ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    if "_" not in display_word:
        print(f"\nCongratulations! You guessed the word: '{secret_word}'")
    else:
        print(f"\nGame Over! You ran out of guesses. The word was: '{secret_word}'")


hangman()