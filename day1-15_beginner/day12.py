
import random

print ('Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100')
number_to_guess = random.randint(1,100)
print(f'testing code -- {NUMBER_TO_GUESS}')
difficulty = input("Choose a difficulty: 'easy' or 'hard: '").lower()

if difficulty == 'easy':
    lives= 10
else:
    lives = 5

def guess_number(lives,correct_number):
    while lives > 0 :
        pass
        user_guess = int(input('Guess a number: ').lower())
        if user_guess == correct_number:
            print('CORRECT, YOU WIN!!')
            lives = 0
        elif user_guess > correct_number:
            print('too high')
            lives -= 1
        elif user_guess < correct_number:
            print('too low')
            lives -= 1
        if lives > 0:
            print(f'guess again.\nYou have {lives} remaining.')
        else:
            print('You have run out of guesses, you lose!')

guess_number(lives,number_to_guess)
