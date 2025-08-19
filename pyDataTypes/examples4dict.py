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

# create a dictionary using a dict class
my_dict = dict({1: "Smith", 2: "Emma", 3: "Jessa"})

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# access value using a key name
print(my_dict[1])  # Smith
# Access using get() - caling by key of first pair
print(my_dict.get(1))  # Smith

#dictionary with different datatype elements: 
dict = { "name": "Natasha", 1: "Number one", (1, 2): [3,4,5] }

# edit dictionary.
## update elements - change the value of a key
#original: my_dict = dict({1: "Smith", 2: "Emma", 3: "Jessa"})
my_dict[1] = "Kelly"
print(my_dict[1])  # Kelly
#output: {1: "Kelly", 2: "Emma", 3: "Jessa"}
# add new key-value pair:
my_dict["Natasha"] = 17
# output: 
# {1: "Kelly", 2: "Emma", 3: "Jessa", "Natasha": 17}

# Removing items from dictionary.
# with del  (by key): 
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}
del d["age"]
print(d)
# output: {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# Clear the whole dictionary
d.clear()
print(d)
# output: {}


