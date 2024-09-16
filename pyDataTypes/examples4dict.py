# 4 built-in data types in Python: List, Tuple, Set, and Dictionary
# Python dictionaries are unordered collections of unique values stored in (Key-Value) pairs.

# A heterogeneous (i.e., str, list, tuple) elements are allowed for both key and value in a dictionary. But An object can be a key in a dictionary if it is hashable.
# The dictionary is mutable which means we can modify its items
# Dictionary is unordered so we can’t perform indexing and slicing 

# create a dictionary
my_dict = {1: "Smith", 2: "Emma", 3: "Jessa"}

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# create a dictionary using a dit class
my_dict = dict({1: "Smith", 2: "Emma", 3: "Jessa"})

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# access value using a key name
print(my_dict[1])  # Smith

# change the value of a key
my_dict[1] = "Kelly"
print(my_dict[1])  # Kelly
