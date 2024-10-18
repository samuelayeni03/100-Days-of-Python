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
/______/______/______/______/______/______/______/______/______/______/[Samuel]
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

print("You are at a cross road. Where do you want to go? Type 'left' or 'right'.")
choice = input()

if choice.lower() == "left":
    print("You came to a lake, there's an island in the middle of the lake. Type 'wait' to wait for a boat or Type 'swim' to swim across.")
    choice = input()
    if choice.lower() == "wait":
        print("You arrive at the island with help of a local fisherman. There is a house with 3 doors. One red, one yellow and the other blue. Which colour do you choose?")
        choice = input()
        if choice.lower == "blue":
            print("You enter a room full of savages, you are killed. \nGame Over.")
        elif choice.lower() == 'red':
            print("You enter a room full of beast. \nGame Over.")
        elif choice.lower() == 'yellow':
            print("You enter a room filled with Treasure. \nYOU WIN.")
        else:
            print("Not a valid response.")
    elif choice.lower() == "swim":
        print("You drowned trying to get across the lake. \nGame Over")
    else:
        print("Not a valid choice.")
elif choice.lower() == "right":
    print("You fell into a trap. \nGame Over")
else:
    print("Not a valid choice.")