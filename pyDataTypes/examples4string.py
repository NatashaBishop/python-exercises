# In Python, A string is a sequence of characters enclosed within a single quote or double quote. 
# These characters could be anything like letters, numbers, or special symbols enclosed within double quotation marks. For example, "PYnative" is a string. 

platform = "PYnative"
print(type(platform))  # <class 'str'>

# display string
print(platform)  # 'PYnative'

# accessing 2nd character of a string
print(platform[1])  # Y 


# The string is immutable, i.e., it can not be changed once defined. 
# You need to create a copy of it if you want to modify it. This non-changeable behavior is called immutability. 

platform = "PYnative"
# Now let's try to change 2nd character of a string.
platform[0] = 'p'
# Gives TypeError: 'str' object does not support item assignment
