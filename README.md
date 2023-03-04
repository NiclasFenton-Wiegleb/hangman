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

## Milestone 3

Building on the above, a class function is added in mileston_4.py, initialising its attributes and the check_guess as well as the ask_for_input methods are moved into the class. This updated code can keep track of previous guesses, number of lives and reveal where letters are in the word following a correct guess.
Please see the code below:

```
import random

fruit_lst = ['apple', 'banana', 'orange', 'lemon', 'lime', 'melon', 'watermelon', 'grape', 'grapefruit', 'plum', 'mango', 'pineapple', 
                'kiwi', 'peach', 'avocado', 'coconut', 'apricot', 'blueberry', 'blackberry', 'strawberry', 'raspberry', 'cherry', 'pear', 
                'mandarin', 'durian', 'passion fruit', 'persimmon', 'papaya', 'pomegranate']

class Hangman:
    def __init__(self,word_list, num_lives = 5) -> None:
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_guessed = []
        for letter in self.word:
                self.word_guessed.append('_')
        self.num_letters = len(set([letter for letter in self.word if letter not in self.list_of_guesses]))
        self.num_lives = num_lives
        self.word_list = word_list

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! "+guess+" is in the word.")
            indices = []
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print("Sorry, "+guess+" is not in the word.")
            print("You have "+str(self.num_lives)+" lives left.")
        

            
    def ask_for_input(self):
        while True:
            guess = input("Guess a single letter:\n")
            if len(guess) != 1 and guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

x = Hangman(fruit_lst)

x.ask_for_input()
```