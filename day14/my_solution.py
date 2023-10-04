from game_data import data
from art import logo, vs
from replit import clear
import random


print(logo)

def game():
  point = 0
  end_game = False
  
  while not end_game:
    option_a = random.choice(data)
    option_b = random.choice(data)
    print(f"Compare A:{option_a['name']}, a {option_a['description']} , from {option_a['country']}")
    print(vs)
    print(f"Compare B:{option_b['name']}, a {option_b['description']} , from {option_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if guess == "A" and option_a["follower_count"] > option_b["follower_count"]:
      # compare option_a 's follower number with b's follower number 
      point = point +1
      clear()
      print(f"u right,current score {point}")

    elif guess == "B" and option_b["follower_count"] > option_a["follower_count"]:
      point = point +1
      clear()
      print(f"u right,current score {point}")

    elif guess == "A" and option_a["follower_count"] < option_b["follower_count"]:
      clear()
      print(f"Sorry, that's wrong. Final score: {point}")
      end_game = True
      
    elif guess == "B" and option_a["follower_count"] > option_b["follower_count"]:
      clear()
      print(f"Sorry, that's wrong. Final score: {point}")
      end_game = True
game()
