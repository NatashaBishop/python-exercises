# set is an unordered collection of data items that are unique, collection of elements (Or objects) that contains no duplicate elements.
# used to represent a group of unique elements as a single entity

    # It is mutable which means we can change set items
    # Duplicate elements are not allowed
    # Heterogeneous (values of all data types) elements are allowed
    # Insertion order of elements is not preserved, so we can’t perform indexing on a Set

# create a set using curly brackets{,}
my_set = {100, 25.75, "Jessa"}
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# create a set using set class
my_set = set({100, 25.75, "Jessa"})
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# add element to set
my_set.add(300)
print(my_set)  # {25.75, 100, 'Jessa', 300}

# remove element from set
my_set.remove(100)
print(my_set)  # {25.75, 'Jessa', 300}
