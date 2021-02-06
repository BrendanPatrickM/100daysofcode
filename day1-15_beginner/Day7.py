#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
print(chosen_word)



guess = input('Guess a letter:\n').lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
  if guess == letter:
    print ('Right')
  else:
    print('Wrong')
