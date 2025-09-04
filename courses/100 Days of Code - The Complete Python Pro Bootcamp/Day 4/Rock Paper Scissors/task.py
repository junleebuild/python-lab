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
picture = [rock, paper, scissors]
import random
my_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
computer_Choice = random.randint(0, 2)
print(picture[my_Choice])
print("Computer chose:")
print(picture[computer_Choice])

if my_Choice == computer_Choice:
    print("Draw")
elif (my_Choice == 0 and computer_Choice == 2) or (my_Choice == 2 and computer_Choice == 1) or (my_Choice == 1 and computer_Choice == 0):
    print("You win")
else:
    print("You lose")