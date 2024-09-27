# comparing objects in Pyhton.
# Equality operator "==" and Identity operator "is" r defferent
# The equality operator "==" is used to compare the value of two variables. 
# The identities operator "is" is used to compare the memory location of two variables.

' Example: 
# we have two lists that contains same data. The we used the identity ‘is’ operator and equality ‘==’ operator to compare both the lists. 
# Python program to illustrate the use
# of 'is' and '==' operators
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
# using 'is' and '==' operators
print(lst1 is lst2)
print(lst1 == lst2)

