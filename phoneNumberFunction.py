"""
#Phone number string checker function. Checks to see that only numbers have been entered in the appropriate places, then splits the sections. Includes a test list.

#phoneNumber = str(input("Enter your phone number in format xxx-xxx-xxxx: "))
def numbChecker(phoneNumber):
  areaCode = phoneNumber[0:3]
  preFix = phoneNumber[4:7]
  sufFix = phoneNumber[8:12]
  if areaCode.isdecimal():
    if preFix.isdecimal():
      if sufFix.isdecimal():
        newPhone = phoneNumber.split("-", 2)
        areaCode = newPhone[0] 
        preFix = newPhone[1]
        sufFix = newPhone[2]
        print(areaCode)
        print(preFix)
        print(sufFix)
      else:
        print("Invalid phone number format1. Try again using only integers and 2 hyphens.")
        
    else:
      print("Invalid phone number format2. Try again using only integers and 2 hyphens.")
      
  else:
    print("Invalid phone number format3. Try again using only integers and 2 hyphens.")
    

testList = ["208-447-8214", "2O8-447-8214", "208-44--8214", "208-447-82A4", "208-44L-82|4", "2*8-44}-821+"]
for i in testList:
  numbChecker(i)
"""

"""
#Attempted function using the re module. Non-working. 
def phoneNumberFunc():
  phoneNumber = str(input("Enter your phone number: "))
  if not re.match("^[0-9,+,-,\s]*$", phoneNumber):
    print("Enter the phone number in format +xxx xxx-xxx-xxxx.")
    phoneNumberFunc()
  elif len(phoneNumber) > 17:
    print("Phone number cannot be more than 17 characters, including special characters and a space.")
    phoneNumberFunc()
  else:
    print("Good to go.")
    return phoneNumber

phoneNumberFunc()
"""