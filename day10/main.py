from replit import clear
from art import logo
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

def calculator():

  print(logo)
  continue_calculation = True
  
  num1 = float(input("what is the 1st number? "))
    
  for symbol in operations:
    print(symbol)
       
  while continue_calculation:
    
    
      
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    # based on user selection, we find the corresponding operation function inside the operations dictionary 
    calculation_function = operations[operation_symbol]
    # call the corresponding function with user picked numbers and saved to answer variable
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      continue_calculation = False
      clear()
      calculator()
  
calculator()

