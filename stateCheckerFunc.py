
#Checks the letters input are only alpha characters, then checks to make sure the lenght is only 2 characters, then makes sure that the two letters are actual abbreviations for real states from a list of the states. 
#Could probably just do the list check if statement to make it less lines of code....

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

"""
#Alternate shorter method. not sure if this will prevent hacking type attempts, or not.

def stateChecker():
  theState = str(input("Enter your 2 character state abbreviation: "))
  theState = theState.upper()
  if theState in stateAbbrList:
    print("Thank you!")
    print(theState)
    return theState
  else:
    print("That is not a valid abbreviation for a state. Please try again. ")
    stateChecker()
  
stateChecker()
"""