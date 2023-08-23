#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

totalBill = float(input("What is the total bill cost? "))
tipPercent = float(input("what percentage of tips u would like to give, 10, 12, or 15 ? "))
num_of_people = float(input("how many people to split the bill? "))
try:
  singleBill = (totalBill / num_of_people) * (1+ tipPercent/100)
  roundedNumber = round(singleBill, 2)
  print("Each person should pay $",roundedNumber)
except:
  print("Invalid Input, please type a valid number")
  quit()