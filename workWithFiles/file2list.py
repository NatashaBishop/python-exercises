#convert a text file into list
with open('input.txt') as f:
    my_list = list(f)
print(my_list)
#strip new line character
with open('input.txt') as f:
  my_list = [x.rstrip() for x in f]
print(my_list)
