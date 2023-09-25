#Number Guessing Game Objectives:
import random
from art import logo

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def play_game():
  '''function to play this game'''
  
  
  EASY = 10
  DIFFICULT = 5

  ANSWER = random.randint(1, 100)
  print(logo)
  print(
      "Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100."
  )
  print("Pssst, the correct answer is", ANSWER)
  level_of_game = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  end_of_game = False
  if level_of_game == "easy":
      print(f"You have {EASY} attempts remaining to guess the number.")
      while not end_of_game:
        guess = int(input("Make a guess: "))
        if guess == ANSWER:
          print(f"You got it! The answer was {ANSWER}.")
          end_of_game = True
        elif guess > ANSWER:
          EASY= EASY -1 
          print("Too high.")
          print(f"You have {EASY} attempts remaining to guess the number.")
        elif guess < ANSWER:
          EASY= EASY -1 
          print("Too Low.")
          print(f"You have {EASY} attempts remaining to guess the number.")
        
        if EASY == 0:
          print("You've run out of guesses, you lose.")
          end_of_game = True
  else:
    print(f"You have {DIFFICULT} attempts remaining to guess the number.")
    while not end_of_game:
      guess = int(input("Make a guess: "))
      if guess == ANSWER:
        print(f"You got it! The answer was {ANSWER}.")
        end_of_game = True
      elif guess > ANSWER:
        DIFFICULT= DIFFICULT -1 
        print("Too high.")
        print(f"You have {DIFFICULT} attempts remaining to guess the number.")
      elif guess < ANSWER:
        DIFFICULT= DIFFICULT -1 
        print("Too Low.")
        print(f"You have {DIFFICULT} attempts remaining to guess the number.")
      
      if DIFFICULT == 0:
        print("You've run out of guesses, you lose.")
        end_of_game = True
play_game()