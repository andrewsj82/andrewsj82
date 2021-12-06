import re

def zipCodeFunc():
  zipCode = str(input("Enter your zipcode: "))
  zipCodeCheck = re.search("[^0-9]", zipCode)
  if zipCodeCheck != None:
    print("Enter the zipcode in numbers only.")
    zipCodeFunc()
  elif len(zipCode) != 5:
    print("Zipcode must be 5 digits.")
    zipCodeFunc()
  else:
    print("Good to go.")
    return zipCode

zipCodeFunc()