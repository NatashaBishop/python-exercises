# Open the file in read mode:
with open('data.txt', 'r') as file:
lines = file.readlines()   # Read line by line into a list

# Print the list of lines:
print(lines) 

# or
myIntegerList = [] # do I need to create empty list?
with open('data.txt') as f:
  myIntegerList = [ int(i) for i in f ] # converting lines into integer
  print(myIntegerList)  

