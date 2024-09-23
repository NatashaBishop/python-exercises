# Python program to illustrate the use of 'is' identity operator

# is          True if the operands are identical : Returns True if both objects refers to same memory location, else returns False. Syntax: obj1 is obj2
# is not      True if the operands are not identical : Returns False if both object refers to same memory location, else returns True. Syntax: obj1 is not obj2
num1 = 5
num2 = 5
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1
str1 = "hello world"
str2 = "hello world"
# using 'is' identity operator on different datatypes
print(num1 is num2)
print(lst1 is lst2)
print(str1 is str2)
print(str1 is str2)

# Python program to illustrate the use of 'is not' identity operator
num1 = 5
num2 = 5
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1
str1 = "hello world"
str2 = "hello world"
# using 'is not' identity operator on different datatypes
print(num1 is not num2)
print(lst1 is not lst2)
print(str1 is not str2)
print(str1 is not str2)
