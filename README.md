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
```

## Milestone 4

Building on the above, a class function is added in mileston_4.py, initialising its attributes and the check_guess as well as the ask_for_input methods are moved into the class. This updated code can keep track of previous guesses, number of lives and reveal where letters are in the word following a correct guess.
Please see the code below:

```
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
```

## Milestone 5

Finally, milestone_5.py brings the whole hangman game together. The play_game function takes a list of words as a parameter and creates a Hangman class object. It then checks whether num_lives has dropped to zero or the word has been guessed. If neither of the conditions are met, it will continue running the ask_for_input function. See the function below:

```
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!\nThe word was '+game.word+'.')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
```

The ask_for _input function of the Hangman class is also modified to allow players to guess the whole word at once:

```
def ask_for_input(self):
        while True:
            print(self.word_guessed)
            guess = input("Guess a single letter or the whole word:\n")
        *** if guess == self.word:
                self.num_letters = 0
                break ***
            elif len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
```