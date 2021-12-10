import re

def cityFunc():
  cityName = str(input("Enter your city: "))
  if not re.match("^[a-z,A-Z,\s]*$", cityName):
    print("Error! Only letters a to z allowed!")
    cityFunc()
    if len(cityName) > 25:
      print("Max length of 25 letters for the city name.")
      cityFunc()
    else:
      print("Good to go.")
      return cityName
  else:
    print("Good so far.")
    print(cityName)
    return cityName
    
 
cityFunc()

"""
def cityFunc():
  cityName = str(input("Enter your city: "))
  if not re.match("^[a-z,A-Z,\s]*$", cityName):
    print("Error! Only letters a to z allowed!")
    cityFunc()
  if len(cityName) > 25:
    print("Max length of 25 letters for the city name.")
    cityFunc()
  else:
    print("Good so far.")
  
cityFunc()
"""