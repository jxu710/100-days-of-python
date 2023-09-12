# to create documentation for functions we write, we could use docstrings, so when we call the function, the documentation will pop up

def format_name (fname,lname):
  '''
  take first and last name as inputs and return the title case version of them
  '''
  formatted_f = fname.title()
  formatted_l = lname.title()

  return f"{formatted_f} {formatted_l}"

print(format_name("JOHN","DOE"))
  