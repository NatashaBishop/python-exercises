# difference between extend() and append() methods
# append() and extend() are specific to lists only

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

# The append() function is used to add a single element to the end of the list. It is simple and efficient for appending individual elements.

# The extend() function is employed to add multiple elements from an iterable (e.g., another list, tuple) to the end of the list. It is useful for combining or merging lists efficiently.

#  extend() can add elements from any iterable, including lists, tuples, strings, and other sequences. 
# As long as the iterable is compatible with the list, it can be used with extend()
