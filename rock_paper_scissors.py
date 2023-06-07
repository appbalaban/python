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

import random


choose = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors. "))


if choose == 0:
  choose == rock
  print(rock)
if choose == 1:
  choose == paper
  print(paper)
if choose == 2:
  choose == scissors
  print(scissors)

computer_choose = random.randint(0,2)
print("Computer choise:")

if computer_choose == 0:
  computer_choose == rock
  print(rock)
if computer_choose == 1:
  computer_choose == paper
  print(paper)
if computer_choose == 2:
  computer_choose == scissors
  print(scissors)

if computer_choose == 0 and choose == 1:
  print("You win")
elif computer_choose == 0 and choose == 2:
  print("You lose")
elif computer_choose == 1 and choose == 0:
  print("You lose")
elif computer_choose == 1 and choose == 2:
  print("You win")
elif computer_choose == 2 and choose == 0:
  print("You win")
elif computer_choose == 2 and choose == 1:
  print("You lose")  
elif computer_choose == choose:
  print("Dead heat")
