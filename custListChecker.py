#This function is used to check the number of current registered users saved in a CSV file. This number is used as part of the primary key.
def custListCheck():
  file = open("custBackupDict.csv")
  reader = csv.reader(file)
  lines = len(list(reader))
  print(lines)
  return lines
myCustList = custListCheck()