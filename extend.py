# extend() function is a built-in method that is used to append multiple elements from an iterable 
# (such as another list, tuple, or any other sequence) to the end of an existing list. 
# unlike the append() method, which adds only one element at a time, extend() allows you to add several elements in a single operation.

# syntax for the extend() function is as follows: list_name.extend(iterable)

# Initializing an empty list
fruits = [‘apple’, ‘banana’]
# Adding elements from another list using extend()
additional_fruits = [‘orange’, ‘grape’, ‘mango’]
fruits.extend(additional_fruits)
print(fruits) 
# Output: [‘apple’, ‘banana’, ‘orange’, ‘grape’, ‘mango’]
