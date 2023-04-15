
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
print("Welcome to Temple Island.")
print("Your mission is to find the treasure.") 


decision1 = input("Do you want to walk forward or go back? \n'Forward' or 'Back' ")
decision1 = decision1.lower()

if decision1 == "forward":
  decision2 = input("You keep walking for hours till you see a lake.\nDo you want to swim accross or wait for a boat? \n'Swim' or 'Boat'")
  decision2.lower()
  
  if decision2 == "boat":
    print("You keep wating for the boat... Eventually it comes and it takes you accross the lake.")
    decision3 = input("You see a temple on the shore where the boat drops you off. Enter or just leave? \n'Enter' or 'Leave'")
    decision3.lower()
    if decision3 == "enter":
      decision4 = input("You find 3 doors. A Gold door, a blue door, and a red door. \n'Gold' 'Blue' 'Red'")
      decision4.lower()
      if decision4 == "gold":
          print("You open the door and look inside... YOU FOUND IT THE TREASURE!")
      elif decision4 == "red":
            print("A floor trap opens and you fall to your death! !!GAME OVER!!")
      else:
        print("You find waldo! GGG")
    else:
        print("You never find the Treasure! !!")
  else:
      print("A shark eats you! !!GAME OVER!!")
else: 
  print("you fall off a cliff!! !!GAME OVER!!")

x = input('''
  ,:\      /:.
 //  \_()_/  \\
||   |    |   ||
||   |    |   ||
||   |____|   ||
 \\  / || \  //
  `:/  ||  \;'
       ||
       ||
       XX
       XX
       XX
       XX
       OO
       `'
''')
