
import random
from os import system
from game_data import data
import art

def ask_question(choice_a, choice_b):

  print_question(choice_a ,'a' )
  print(art.vs)
  print_question(choice_b ,'b')
  player_choice = input("\nWho has more followers? Type 'A' or 'B': " ).lower()
  if player_choice == "a":
    return choice_a
  else:
    return choice_b
def print_question(person,a_or_b):
  a_or_b = a_or_b.upper()
  name = person['name']
  description = person['description']
  country = person['country']
  print(f"Compare {a_or_b}: {name}, a {description}, from {country}.")


game_over = False
iterations = 0


while not game_over:
  if iterations == 0:
    choice_a = (random.choice(data))
    choice_b = (random.choice(data))
  elif winner == choice_b:
      choice_a = choice_b
      choice_b = (random.choice(data))
  else:
       choice_b = (random.choice(data))

  a_followers = choice_a['follower_count']
  b_followers = choice_b['follower_count']
  if a_followers > b_followers:
    winner = choice_a
  else:
    winner = choice_b
  print(art.logo)
  if iterations > 0:
    print(f"You're right! Current score: {iterations}.")
  chosen_by_player = (ask_question(choice_a, choice_b))
  if chosen_by_player == winner:
    iterations +=1
    system('clear')
  else:
    game_over = True
    print (f"Sorry, that's wrong. Final score: {iterations}")
