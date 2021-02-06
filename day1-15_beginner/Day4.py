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
if player <= 0 or player >=3 :
    print('You have made an invalid choice')
else:
    print(art[player])

    #computer chooses a random
    computer = random.randint(0,2)
    print('Computer chose:\n')
    print (art[computer])

    if player <= 0 or player >=3 :
        print('You have made an invalid choice')
    elif player == computer:
        print ('Draw')
    elif player == computer-1:
        print ('You lose')
    elif player == computer+1:
        print ('You win')
    elif player  == computer-2:
        print ('You win')
    elif player  == computer +2:
        print ('You lose')
