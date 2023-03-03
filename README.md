# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 2

The file milestone_2.py contains code that randomly picks a word from a given list. The user is then asked to guess a single letter. The code also validates that the length of the input is 1 and that it is alphabetical. You can see the code below:

**import random

word_list = ['Apple', 'Bannana', 'Mango', 'Pear', 'Grapes']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Guess a single letter:\n')

if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')**

## Milestone 3

