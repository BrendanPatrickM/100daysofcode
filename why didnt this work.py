import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#user choice
art = [rock,paper,scissors]
print('What do you choose?')
player = int(input('Type 0 for rock, 1 for paper, 2 for scissors\n'))
print (f'{art[player]}\n')

#computer chooses a random
computer = random.randint(0,2)
print('Computer chose:\n')
print (f'{art[computer]}\n')

if player == computer:
  print ('Draw')
else:
  if player == computer-1:
    print ('You lose')
  if player == computer+1:
    print ('You win')
  if player  == computer-2:
    print ('You win')
  if player  == computer +2:
    print ('You lose')
  
