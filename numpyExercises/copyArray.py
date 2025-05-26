import numpy as np
# Create a Python list
list1 = [3,6,4] 
# Convert list1 into a NumPy array, array1
array1 = np.array(list1)
x = array1.copy() # copy() produces a separate array in memory
x[0] = 5
print(array1)
print(x)
#out: 
#3,6,4
#5,6,4
