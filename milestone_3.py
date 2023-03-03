import random

word_list = ['Apple', 'Bannana', 'Mango', 'Pear', 'Grapes']

word = random.choice(word_list)

while True:
    guess = input("Guess a single letter:\n")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print("Good guess! "+guess+" is in the word.")
else:
    print("Sorry, "+guess+" is not in the word. Try again.")