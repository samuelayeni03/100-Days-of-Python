#This is a Rock Paper Scissors game...
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

print("Rock and scissors...")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input())
computer_choice = random.randint(0, 2)

#print player's choice...
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Wrong input.")

#print computer's choice...
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if choice == 0 and computer_choice == 0:
    print("Draw: You both chose Rock.")
elif choice == 0 and computer_choice == 1:
    print("Loss: Paper wins over Rock.")
elif choice == 0 and computer_choice == 2:
    print("Win: Rock wins over scissors.")
elif choice == 1 and computer_choice == 0:
    print("Win: Paper wins over Rock.")
elif choice == 2 and computer_choice == 0:
    print("Loss: Rock wins over Scissors.")
elif choice == 1 and computer_choice == 1:
    print("Draw: You both chose paper")
elif choice == 2 and computer_choice == 2:
    print("Draw: You both chose Scissors.")
elif choice == 1 and computer_choice == 2:
    print("Loss: Scissors wins over Paper.")
elif choice == 2 and computer_choice == 1:
    print("Win: Scissors wins over Paper.")
else:
    print("You typed an invalid number.")


