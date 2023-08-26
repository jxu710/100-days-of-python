
# import random module to use for generating random stuff
import random 

# import module from my_module , the module I created 
import my_module

# random interget between 1 and 10, inclusively 
random_interger = random.randint(1,10)

print(random_interger)


print(my_module.date)

# random float number between 0 and 1, not include 0 and 1 
random_float = random.random()
print(random_float)

# 0 ... to 4.999999
random_float * 5 