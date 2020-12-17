print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n --------")
print('\n\nYou are standing on a cliff edge.\nThe wind blows against your right cheek\n\n ')

direction = input ("-- Which direction would you like to go: LEFT or RIGHT?--\n")
if direction.lower() != "left":
  print('\nyou fall into the sea and die. \nGAME OVER')
else:
  print('\n\n\nyou find yourself at a wide river, a boat might come along later.\n')
  print('Would you like to wait for a boat to cross, or attempt to swim--\n')
  wait = input ('--WAIT or SWIM?--\n')
  if wait.lower() != "wait" :
    print ('\nYou drown and die. \nGAME OVER ')
  else:
    print ('\n You cross without incident.\n\nYou stand before a tower with three doors;\n RED, BLUE, or YELLOW')
    door = input ('-- Which door would would you like to choose? --\n')
    if door.lower() =="red":
      print('\nThe room is filled with fire.')
      print('\nYou die.\nGAME OVER')
    elif door.lower() =="blue":
      print('\nThe room is filled with beasts.')
      print('\nYou die.\nGAME OVER')
    elif door.lower() =="yellow":
      print ('\nYOU WIN, YOU FOUND THE TREASURE')
    else:
      print('GAME OVER')
