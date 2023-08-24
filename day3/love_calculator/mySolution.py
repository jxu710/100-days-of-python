# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

first_score = 0
second_score = 0

# two people's score of letter t in True
t_times = lower_name1.count("t")
t2_times = lower_name2.count("t")
first_score += t_times
first_score += t2_times


# two people's score of letter r in True
r_times = lower_name1.count("r")
r2_times = lower_name2.count("r")
first_score += r_times
first_score += r2_times

# two people's score of letter u in True

u_times = lower_name1.count("u")
u2_times = lower_name2.count("u")
first_score += u_times
first_score += u2_times

# two people's score of letter e in True

e_times = lower_name1.count("e")
e2_times = lower_name2.count("e")
first_score += e_times
first_score += e2_times

## two people's score of letter l in LOVE

l_times = lower_name1.count("l")
l2_times = lower_name2.count("l")
second_score +=l_times
second_score += l2_times

## two people's score of letter o in LOVE

o_times = lower_name1.count("o")
o2_times = lower_name2.count("o")
second_score +=o_times
second_score += o2_times

## two people's score of letter v in LOVE

v_times = lower_name1.count("v")
v2_times = lower_name2.count("v")
second_score +=v_times
second_score += v2_times

## two people's score of letter e in LOVE

second_score +=e_times
second_score += e2_times

totalScore = int(str(first_score) + str(second_score))

if totalScore <10 or totalScore > 90:
    print(f"Your score is {totalScore},you go together like coke and mentos.")
elif 40 < totalScore < 50:
    print(f"Your score is {totalScore},you are alright together.")

else: 
    print(f"Your score is {totalScore}")
