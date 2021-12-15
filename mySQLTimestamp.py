#This function takes the current date and time, then reformats them data into the format necessary for a mySQL database column
import datetime;

currentTime = str("")
def mySQLTimeStamp():
  cTime = str(datetime.datetime.now())[::-1].split('.', 1)
  cTimeB = cTime[1]
  currentTime = cTimeB[::-1]
  return currentTime
currentTime = mySQLTimeStamp()