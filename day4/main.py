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

#Write your code below this line 👇

user_choice = int(input('"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)


# generate computer choice here 
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(f"Computer chose:\n {rock}")
elif computer_choice == 1:
  print(f"Computer chose:\n {paper}")
else:
  print(f"Computer chose:\n {scissors}")

# Determine who win the game 

if user_choice == computer_choice:
  print("It's a tie")
elif user_choice == 0 and computer_choice ==1:
  print("You lose")
elif user_choice == 0 and computer_choice ==2:
  print("You win")
elif user_choice ==1 and computer_choice ==0:
  print("You win")
elif user_choice ==1 and computer_choice ==2:
  print("You lose")
elif user_choice ==2 and computer_choice ==0:
  print("You lose")
else:
  print("You win")