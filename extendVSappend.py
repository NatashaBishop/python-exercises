# difference between extend() and append() methods

# assigning two lists
list_one = [2, 3, 4]
list_two = [2, 3, 4]
x = [5, 6]
# use the two different methods
list_one.append(x)
list_two.extend(x)

# displaying the lists using the print statement.
print(list_one)
#printing the second list
print(list_two)

# Output
# [2, 3, 4, [5, 6]]
# [2, 3, 4, 5, 6]
