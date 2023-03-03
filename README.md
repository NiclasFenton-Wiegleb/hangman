# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 2

The file milestone_2.py contains code that randomly picks a word from a given list. The user is then asked to guess a single letter. The code also validates that the length of the input is 1 and that it is alphabetical. You can see the code below:

```
import random

word_list = ['Apple', 'Bannana', 'Mango', 'Pear', 'Grapes']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Guess a single letter:\n')

if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')

```


The random.choice() function assigns a random word from the list to the variable 'word', while the 'guess' variable asks for the user's input. This is then checked by an if statement to validate that the input has the correct format.

## Milestone 3

The file milestone_3.py is a python script that elaborates on the code above. It defines two functions: check_guess(x) and ask_for_input(). The first function uses the if statement from Milestone 2 to validate that a guess adheres to the right format. The ask_for_input() function asks for the user input, which is then past into the check_guess() function. Please see the code below:

```
import random

word_list = ['Apple', 'Bannana', 'Mango', 'Pear', 'Grapes']

word = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! "+guess+" is in the word.")
    else:
        print("Sorry, "+guess+" is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a single letter:\n")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
```