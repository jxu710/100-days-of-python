from art import logo 
from game_data import data 
import random 
# display art
print(logo)


def format_data(account):
  '''format the account data into printable format '''
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]

  return f"{account_name}, a {account_descr}, from {account_country}"

# generate a random account from the game data 
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A : {format_data(account_a)}")
print(f"Compare B : {format_data(account_b)}")

# ask user for a guess

# check if user is correct 
## get follower count of each account
## use if statement to check if user if correct 

# give user feedback on their guess 
# make the game repeatable

# making account at position B become the next account at position A

# clear the screen