from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)


end_of_bid = False

bids = []
while not end_of_bid:
    name = input("What is Your name? ")
    bid_given = int(input("What is your bid? "))

    # push the dictionary of name and bid value pairs to the bids list
    bids.append({"name":name,"bid_given":bid_given})

  # if user so no, the while loop will end
    conitnue = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    clear()
    if conitnue == "no":
        end_of_bid = True



highest_bid = 0
for bid in bids:
  if bid["bid_given"] > highest_bid:
    highest_bid = bid["bid_given"]
    winner_bidder = bid["name"]


print(f"The winner is {winner_bidder} with a bid of ${highest_bid}")
