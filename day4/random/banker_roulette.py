# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_int = random.randint(0,len(names)-1)

print(f"{names[random_int]} is going to buy the meal today!")

# Another solution, using choice method

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")