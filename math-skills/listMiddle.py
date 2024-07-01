# Import statistics Library
import statistics 
# The list can be of any size and the numbers are not guaranteed to be in any particular order
list = [15, 9, 55, 41, 35, 20, 62, 49] 
# Calculate middle values
print(statistics.median(list))
# v.2 
import numpy as np
m = np.median([0, 2, 5, 6, 8, 9, 9])
print("ans:", m)
# ans: 6.0
