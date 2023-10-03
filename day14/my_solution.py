from game_data import data
from art import logo, vs
from replit import clear
import random


print(logo)

option_a = random.choice(data)
option_b = random.choice(data)

print(f"Compare A:{option_a['name']}, a {option_a['description']} , from {option_a['country']}")
print(vs)
print(f"Compare B:{option_b['name']}, a {option_b['description']} , from {option_b['country']}")

input("Who has more followers? Type 'A' or 'B': ")