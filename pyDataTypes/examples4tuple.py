# 4 built-in data types in Python: List, Tuple, Set, and Dictionary
# tuple is immutable (read-only version of the list): once we create a tuple, we can’t modify it
# in list, we use square brackets [], in tuple we use round brackets ()

# create a tuple
my_tuple = (11, 24, 56, 88, 78)
print(my_tuple)  # (11, 24, 56, 88, 78)
print(type(my_tuple))  # class 'tuple'

# Accessing 3rd element of a tuple
print(my_tuple[2])  # 56 - index as in list, starts with 0
# Access Tuple using Negative Index. unlike positive indexes negative count from -1 (not from 0) will go from first element from the end: 
print("Value in tup[-1] = ", my_tuple[-1])
print("Value in tup[-2] = ", my_tuple[-2])
print("Value in tup[-3] = ", my_tuple[-3])
# output: 
# Value in my_tuple[-1] =  78
# Value in my_tuple[-2] =  88
# Value in my_tuple[-3] =  56

# slice a tuple
print(my_tuple[2:7])  # (56, 88, 78)

# create a tuple using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)  # (10, 20, 30, 40)

# not possible update an element
my_tuple[1] = 111
print(my_tuple)
# output: 
# TypeError: 'my_tuple' object does not support item assignment

# concatenating 2 tuples:
tupConcatenated = (my_tuple + my_tuple2) # concatenate them
print(tupConcatenated)
print(my_tuple + my_tuple2) # can concatenate directly, without storage
# output: # (11, 24, 56, 88, 78, 10, 20, 30, 40)
#can b different datatypes: (0, 1, 2, 3, 'Natasha', 'Bishop')

# Nesting of tuples: 
tupNested = (my_tuple, my_tuple2)
print(tupNested)
# output: ((11, 24, 56, 88, 78), (10, 20, 30, 40))
#can b different datatypes: ((0, 1, 2, 3), ('Natasha', 'Bishop'))

# Repetition in tuples:
tupNatasha = ('Natasha',)*4
print(tupNatasha)
# output: ('Natasha', 'Natasha', 'Natasha', 'Natasha')

# Tuples slicing:
tup = (0 ,1, 2, 3)

print(tup[1:])
print(tup[::-1])
print(tup[2:4]) 

''' Output:
(1, 2, 3)
(3, 2, 1, 0)
(2, 3)'''







