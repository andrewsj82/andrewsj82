import csv;

#Take user input for the file name desired, create two .csv names, add empty list that will be populated with column headers.

fileName = input('Enter your desired filename: ')
fileNameBackup = fileName + 'Backup' + '.csv'
fileName = fileName + ".csv"
print(fileName)
fileHeaders = []

#Uses a while loop to create as many column header names as necessary. Does not check illegal naming conventions.

def headerCreator():
  while True:
    newHeader = input('Enter the next table column header. "N" to stop: ')
    if newHeader == "N":
      break
    else:
      fileHeaders.append(newHeader)
  print(fileHeaders)
  return fileHeaders
headerCreator()

#Creates the two new .csv files as CSV dictionaries. Adds the column keys/headers input from header list created by the previous function. 

with open(fileName, 'w', newline='') as fileName:
  outputDictWriter = csv.DictWriter(fileName, fieldnames = fileHeaders)
  outputDictWriter.writeheader() 
  fileName.close

with open(fileNameBackup, 'w', newline='') as fileName2:
  outputDictWriter = csv.DictWriter(fileName2, fieldnames = fileHeaders)
  outputDictWriter.writeheader() 
  fileName.close
