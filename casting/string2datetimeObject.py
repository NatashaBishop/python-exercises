#Convert a String to a datetime Object in Python 
#inspired by: https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime

#datetime and time modules both include a strptime() class method to convert strings to objects.
# The syntax for the datetime.strptime() method:
# datetime.strptime(date_string, format)

# 1. Convert String to datetime.datetime() Object Example:
from datetime import datetime
datetime_str = '09/19/22 13:55:26'
datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
print(type(datetime_object))
print(datetime_object)  # printed in default format
'''output:
<class 'datetime.datetime'>
2022-09-19 13:55:26

