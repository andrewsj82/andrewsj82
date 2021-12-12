def cityFunc():
  cityName = str(input("Enter your city: "))
  if not re.match("^[a-z,A-Z,\s]*$", cityName):
    print("Error! Only letters a to z allowed!")
    cityFunc()
    if len(cityName) > 25:
      print("Max length of 25 letters for the city name.")
      cityFunc()
    else:
      return cityName
  else:
    return cityName
"""
cityFunc sort of works. If the first entry does not have a match,
and a subsequent entry is correctly matched, but doesn't meet the
character requirement it will still pass the incorrect length entry,
but will overwright it again when it loops back for the third entry
that ends up meeting both criteria.
"""


#v2
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
#v1
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
    return dateOfBirth
  else:
    return dateOfBirth
"""
Checks that the DOB entry field only is supplied with numbers 0-9,
and that there are eight total digits. May need to
use string splitting later to ensure the last 4
digits comprising of the year are within a 
realistic realm, like 1930 to whatever year it 
actually is. Also would split the first two and 
second two digits to send as three separate 
strings to the DB.
"""


def fNameFunc():
  fName = str(input("Enter first name: "))
  if not re.match("^[a-z,A-Z,',\s]*$", fName):
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

def lNameFunc():
  lName = str(input("Enter last name: "))
  if not re.match("^[a-z,A-Z,',\s]*$", lName):
    print("Error! Only letters a to z allowed!")
    lNameFunc()
    if len(lName) > 25:
      print("Max length of 25 letters for the last name.")
      lNameFunc()
    else: 
      print("Good to go.")
  else:
    print("Good so far.")    
"""
Checks the first and last name entries independently. 
Won't allow special characters other than apostrophes and spaces.
Also limits character length.
"""


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
"""
Checks zipcode to ensure that it is only integers input,
and that the length is exactly 5 integers long.
"""


def sAddressFunc():
  sAddress = str(input("enter street address: "))
  if not re.match("^[0-9,a-z,A-Z,\s,.,']*$", sAddress):
    print("Only special characters allowed are periods and apostrophes. Please reenter street address.")
    sAddressFunc()
  elif len(sAddress) > 60:
    print("Max length of 60 characters for the street address.")
    sAddressFunc()
  else:
    if sAddress == "":
      print("Street address cannot be blank.")
      sAddressFunc()
    else:
      return sAddress      
sAddressFunc()
"""
Checks to see that the street address only includes numbers, letters, periods, apostrophes, and is less than 60 characters in total length.
"""


def emailAddressFunc():
  emailAddress = emailAddressEntry.get()
  if not re.match("^[a-z,A-Z,0-9,',.,@,#,*,&,_,$,!,%,(,),-]*$", emailAddress):
    print("Use a valid email format!")
    emailAddressFunc()
  elif len(emailAddress) > 60:
    print("Email address must be less than 60 total characters.")
    emailAddressFunc()
  else:
    findAtSymbol = emailAddress.rfind("@")
    newEmail = emailAddress[:findAtSymbol] + "," + emailAddress[findAtSymbol:]
    splitEmail = newEmail.split(",")
    sEmailA = splitEmail[0]
    sEmailB = splitEmail[1]
    if not re.match(".com", sEmailB):
      return emailAddress
    else:
      print("Enter a valid email format.")
      emailAddressFunc()
"""
emailAddress checker function appears to work. they cannot have an email longer than 60 characters. It will also let them use special characters, including multiple @ symbols. it will only let them use .com email addresses, currently. It uses string splitting and concatenation to check from the last @ symbol to check if the format for the email is valid.
"""

def numbChecker():
  phoneNumber = phoneNumberEntry.get()
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
        phone4DB = int(areaCode + preFix + sufFix)
      else:
        print("Invalid phone number format. Try again using only integers and 2 hyphens.") 
    else:
      print("Invalid phone number format. Try again using only integers and 2 hyphens.")
  else:
    print("Invalid phone number format. Try again using only integers and 2 hyphens.")
"""
Phone number checking function. Uses the isdecimal() string method and string splicing to make sure that the phone number is in xxx-xxx-xxxx format, then splits the number and concatenates the parts for adding to the DB without the hyphens, after converting back from string to integer format.
"""


stateAbbrList = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def stateChecker():
  theState = str(input("Enter your 2 character state abbreviation:  "))
  if theState.isalpha() == True:
    if len(theState) == 2:
      theState = theState.upper()
      if theState in stateAbbrList:
        return theState
        print("Thank you!")
        print(theState)
      else:
        print("That is not an abbreviation for a state. Please try again. ")
        stateChecker()
    else:
      print("The state abbreviation may only include two letters. Please try again.")
      stateChecker()
  else: 
    print("You may only submit letters for your state abbreviation. Please try again.")
stateChecker()
#Checks the letters input are only alpha characters, then checks to make sure the lenght is only 2 characters, then makes sure that the two letters are actual abbreviations for real states from a list of the states. 
#Could probably just do the list check if statement to make it less lines of code....

