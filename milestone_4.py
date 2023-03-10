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
print(x.word_guessed)
