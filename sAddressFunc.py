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
      print(sAddress)
      return sAddress      
sAddressFunc()