import random

word_list = ['apple', 'banana', 'orange', 'lemon', 'lime', 'melon', 'watermelon', 'grape', 'grapefruit', 'plum', 'mango', 'pineapple', 
                          'kiwi', 'peach', 'avocado', 'coconut', 'apricot', 'blueberry', 'blackberry', 'strawberry', 'raspberry', 'cherry', 'pear', 
                          'mandarin', 'durian', 'passion fruit', 'persimmon', 'dragon fruit', 'papaya', 'pomegranate']

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

class hangman:
    def __init__(self,word_list, num_lives) -> None:
        self.num_lives = 5
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = [letter if letter in self.list_of_guesses else '_' for letter in self.word]
        self.num_letters = len(set([letter for letter in self.word if letter not in self.list_of_guesses]))
        self.word_list = word_list
        


#for letter in self.word:
    #if letter in self.list_of_guesses:
        #letter
    #else:
        #'_'



x = hangman(word_list,5)

print(x.word)