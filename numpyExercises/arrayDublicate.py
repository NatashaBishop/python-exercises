import numpy as np
# Create a Python NumPy array
array1 = np.array([3,6,4])
x = array1 # assigned x to array1 (array1 dublicate)
x[0] = 5 #Modify the first element of x
print(array1)
print(x)
#out:
#5,6,4
#5,6,4

# we had assigned x = array1 without using .copy(), modifying x  has altered array1 as well, 
# because NumPy assigns references by default instead of creating copies.
# use copy() instead if need to leave array1 attached:
#x = copy(array1)  # copy() produces a separate array in memory
