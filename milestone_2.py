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