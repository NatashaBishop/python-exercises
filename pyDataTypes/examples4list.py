# enspired by https://pynative.com/python-data-types/#h-example-4

# 4 built-in data types in Python: List, Tuple, Set, and Dictionary

# # The Python List is an ordered collection (also known as a sequence ) of elements.
# List elements can be accessed, iterated, and removed according to the order they were inserted at the creation time.
# The list can contain data of all data types such as  int, float, string.
# Duplicates elements are allowed in the list.
# The list is mutable (we can modify the value of list elements).

my_list = ["Jessa", "Kelly", 20, 35.75]
# display list
print(my_list)  # ['Jessa', 'Kelly', 20, 35.75]
print(type(my_list))  # class 'list'

# Accessing first element of list
print(my_list[0])  # 'Jessa'

# slicing list elements
print(my_list[1:5])  # ['Kelly', 20, 35.75]

# modify 2nd element of a list
my_list[1] = "Emma"
print(my_list[1])  # 'Emma'

# create list using a list class
my_list2 = list(["Jessa", "Kelly", 20, 35.75])
print(my_list2)  # ['Jessa', 'Kelly', 20, 35.75]
