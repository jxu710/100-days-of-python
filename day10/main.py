




#Calculator


#Add

def add(n1,n2):
  return n1+n2

# Subtract 

def subtract(n1,n2):
  return n1-n2

# Multiply

def multiply(n1,n2):
  return n1 * n2

# Divide

def divide(n1,n2):
  return n1 / n2

# create a dictonary named operations

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


num1 = int(input("what is the 1st number?"))


for symbol in operations:
  print(symbol)
   
  
operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the next number?: "))
# based on user selection, we find the corresponding operation function inside the operations dictionary 
calculation_function = operations[operation_symbol]
# call the corresponding function with user picked numbers and saved to answer variable
answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")