"""
Take input field information from a user submitted form. Test each field against a RegEx expression to ensure that only appropriate information is applied in the field and sent to the DB. Set up the field info pulls as individual functions?
"""
import re

def lNameFunc():
  lName = str(input("Enter last name: "))
  if not re.match("^[a-z,A-Z,\s,',-]*$", lName):
    print("Error! Only letters a to z allowed!")
    lNameFunc()
  if len(lName) > 25:
    print("Max length of 25 letters for the last name.")
    lNameFunc()
  else:
    print("Good so far.")
  
lNameFunc()