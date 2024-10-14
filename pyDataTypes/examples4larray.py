#1. Basic Array Creation
#create an array in Python using the array module, we need to specify the type code (which defines the type of elements) and a list of initial values.
from array import array

# Create an array of signed integers ('i' is the type code for integers)
arr = array('i', [1, 2, 3, 4, 5])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])
