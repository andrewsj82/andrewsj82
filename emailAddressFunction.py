"""
emailAddress checker function appears to work. they cannot have an email longer than 60 characters. It will also let them use special characters, including multiple @ symbols. it will only let them use .com email addresses, currently. It uses string splitting and concatenation to check from the last @ symbol to check if the format for the email is valid.
"""

def emailAddressFunc():
  emailAddress = str(input("Enter your email address: "))
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
    print(sEmailA)
    print(sEmailB)
    if not re.match(".com", sEmailB):
      print("Good to go.")
      print(emailAddress)
      return emailAddress
    else:
      print("Enter a valid email format.")
      emailAddressFunc()

emailAddressFunc()