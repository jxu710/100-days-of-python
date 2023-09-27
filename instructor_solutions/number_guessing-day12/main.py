from random import randint 



#  A Function to check user's number against actual answer.
EASY_LEVEL_TURNS = 10 
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
  """check answer against guess, Returns the number of turns remaining"""
  if guess > answer:
    print("too high")
    return turns -1 
  elif guess < answer:
    print("too low")
    return turns -1 
  else:
    print(f"You got it! the answer is {answer}")

#  Make function to set difficulty 


def set_difficulty():
  level = input("choose a difficulty, easy or hard: ")

  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  # Choosing a random number between 1 and 100 
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  print(f"Pssst, the correct answer is {answer}") 
  
  turns = set_difficulty()
 
  #  Repeat the guessing functionality if they get it right
  guess = 0
  while guess != answer:
    print(f"you have {turns} to guess the number")
  
    # Let user guess the number
    guess = int(input("Make a guess: "))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
#  Track the number of turns and reduce by 1 if they get it wrong 

game()
