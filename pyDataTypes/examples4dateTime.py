#inspired by https://www.programiz.com/python-programming/datetime
import datetime
# getting current date and time:
curTime = datetime.datetime.now()
print(curTime)
#Output: 2022-12-27 08:26:49.219717

#getting current date:
#import datetime - done in 1st example
current_date = datetime.date.today()
print(current_date)
#Output: 2022-12-27

#date object to represent a date:
#import datetime - done in 1st example
# setting datetime variable toa particular date
setDate = datetime.date(2022, 12, 25)
print(setDate)
#Output: 2022-12-25

#we can import the date class only from the datetime modulein case we are not dealing with time
from datetime import date
d = date(2022, 12, 25)
print(d)
#Output: 2022-12-25

# getting current date from server using today() :
from datetime import date
# today() to get current date
todays_date = date.today()
print("Today's date =", todays_date)
#Output: Today's date = 2022-12-27
