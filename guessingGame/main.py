import random
import json
import os

"""
the player starts with a random word from the words json file and the letter the word starts with if they type hint.
the player can guess the word by guessing letters, kinda like hangman or wheel of fortune.
"""

with open('5_letter_words.json','r') as dataFile: # loads the json data containing all the words
	words = json.load(dataFile) # stores those words to a variable

# starting variables
answer = ''
flag = True

words_list = []
word_letters = []
letters_guessed = ['', '', '', '', '']

# parse the words to a python list
for w in words['wordsList']:
	words_list.append(w['word'])

answer = random.choice(words_list)
word_letters = list((answer.strip().lower()))

first_letter = word_letters[0]

print("Type 'hint' to get the first letter | type 'quit' to quit.")
print("Guess the word by guessing letters.")

# game list
while flag:
	# start the game
	print(f"{letters_guessed}")
	
	inp = input("Enter a Letter: ").lower().strip()
	if inp == 'quit':
		flag = False
		break
	elif inp == 'hint':
		letters_guessed[0] = first_letter
	elif inp in word_letters[0]:
		letters_guessed[0] = inp
	elif inp in word_letters[1]:
		letters_guessed[1] = inp
	elif inp in word_letters[2]:
		letters_guessed[2] = inp
	elif inp in word_letters[3]:
		letters_guessed[3] = inp
	elif inp in word_letters[4]:
		letters_guessed[4] = inp
	else:
		print("Opps! That letter is not in the word. Try again.")

	if letters_guessed == word_letters:
		print("Congratulations! You guessed the word!")
		flag = False
		break




		
		