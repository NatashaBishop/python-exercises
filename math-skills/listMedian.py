# Median comes from the Latin word medius, which also means middle. In math, the median is a number in the middle of a list. In the set 2, 3, 5, 10, 25, the median is 5. 
# Arrange the numbers in order by size. If the number of terms is odd, the median is the middle term. If the number of terms is even, add the two middlemost terms and then divide by 2.

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
