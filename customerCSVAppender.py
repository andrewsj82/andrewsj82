#Take user input and append the info to two different CSV files for storing.
def custCSVAppender():
  with open("custDict.csv", 'a', newline='') as fileName:
    fileHeaders = ["fName","lName","DOB","sAddress","cityName","stateAbbr","zipCode","emailAddress","phoneNumber","primaryKey","currentTime"]
    outputDictWriter = csv.DictWriter(fileName, fieldnames = fileHeaders)
    outputDictWriter.writerow(theCustomer)
    fileName.close
  with open("custBackupDict.csv", 'a', newline='') as fileName2:
    fileHeaders = ["fName","lName","DOB","sAddress","cityName","stateAbbr","zipCode","emailAddress","phoneNumber","primaryKey","currentTime"]
    outputDictWriter = csv.DictWriter(fileName2, fieldnames = fileHeaders)
    outputDictWriter.writerow(theCustomer)
    fileName.close
custCSVAppender()