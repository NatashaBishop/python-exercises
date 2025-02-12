#basic way - casting
lst = list(open(input.txt))

#convert a text file into list
with open('input.txt') as f:
    my_list = list(f)
print(my_list)
#strip new line character
with open('input.txt') as f:
  my_list = [x.rstrip() for x in f]
print(my_list)

#simple way to read lines into list with \n stripped:
f = open('input.txt') # Open file on read mode
lines = f.read().splitlines() # List with stripped line-breaks
f.close() # Close file
