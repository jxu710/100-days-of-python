# Choosing a random number between 1 and 100 
from random import randint 
answer = randint(1,100)


#  A Function to check user's number against actual answer.
def check_answer(guess,answer):
  if guess > answer:
    print("too high")
  elif guess < answer:
    print("too low")
  else:
    print(f"You got it! the answer is {answer}")

#  Make function to set difficulty 

EASY_LEVEL_TURNS = 10 
HARD_LEVEL_TURNS = 5
def set_difficulty():
  level = input("choose a difficulty, easy or hard: ")

  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

# Let user guess the number 
turns = set_difficulty()
guess = int(input("Make a guess: "))
print(f"you have {turns} to guess the number")


#  Track the number of turns and reduce by 1 if they get it wrong 

#  Repeat the guessing functionality if they get it right

