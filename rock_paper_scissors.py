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
game_image = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 foe Scissors.\n"))
if user_choice >=0 and user_choice <=2:
    print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("computer choice:")
print(game_image[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("You type an invalid number. YOU LOSE!")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN!")
elif computer_choice == 0 and user_choice ==2:
    print("YOU LOSE!")
elif computer_choice > user_choice:
    print("YOU LOSE!")
elif user_choice > computer_choice:
    print("YOU WIN!")
elif computer_choice == user_choice:
    print("IT'S A DRAW!")
