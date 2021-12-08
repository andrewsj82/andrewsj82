import re

def DOBfunc():
  while True:
    dateOfBirth = str(input("Enter Date of Birth: "))
    DOBcheck = re.compile(r'\d{2}-\d{2}-\d{4}')
    DOB = DOBcheck.match(dateOfBirth)
    if DOB == None:
      print("Enter the DOB in format xx-xx-xxxx.")
      continue
    else:
      return dateOfBirth
      break

DOBfunc() 

"""
Take input field information from a user submitted form. Test each field against a RegEx expression to ensure that only appropriate information is applied in the field and sent to the DB. Set up the field info pulls as individual functions?



def DOBfunc():
  dateOfBirth = str(input("Enter Date of Birth: "))
  DOBcheck = re.search("[^0-9]", dateOfBirth)
  if DOBcheck != None:
    print("Enter the DOB in numbers only.")
    DOBfunc()
  elif len(dateOfBirth) != 8:
    print("DOB must be 8 digits.")
    DOBfunc()
  elif len(dateOfBirth) == 8:
    print("DOB looks good, so far.")
    print(dateOfBirth)
  else:
    print(dateOfBirth)
    return dateOfBirth

"""