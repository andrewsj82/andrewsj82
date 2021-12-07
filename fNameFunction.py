"""
Take input field information from a user submitted form. Test each field against a RegEx expression to ensure that only appropriate information is applied in the field and sent to the DB. Set up the field info pulls as individual functions?
"""
import re

def fNameFunc():
  fName = str(input("Enter first name: "))
  if not re.match("^[a-z,A-Z]*$", fName):
    print("Error! Only letters a to z allowed!")
    fNameFunc()
    if len(fName) > 20:
    print("Max length of 20 letters for the first name.")
    fNameFunc()
    else:
      print("Good to go.")
      return fName
  else:
    print("Good so far.")
    return fName
  
fNameFunc()