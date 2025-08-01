# 4 built-in data types in Python: List, Tuple, Set, and Dictionary
# tuple is immutable (read-only version of the list): once we create a tuple, we can’t modify it
# in list, we use square brackets []. in tuple we use round brackets ()

# create a tuple
my_tuple = (11, 24, 56, 88, 78)
print(my_tuple)  # (11, 24, 56, 88, 78)
print(type(my_tuple))  # class 'tuple'

# Accessing 3rd element of a tuple
print(my_tuple[2])  # 56 - index as in list, starts with 0

# slice a tuple
print(my_tuple[2:7])  # (56, 88, 78)

# create a tuple using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)  # (10, 20, 30, 40)

# update an element
my_tuple[1] = 111
print(my_tuple)
# (11, 111, 56, 88, 78)
