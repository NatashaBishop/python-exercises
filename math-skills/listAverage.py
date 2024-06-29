# calculate average of  list 

# For Python 3.4+, use mean() from the new statistics module to calculate the average:
# v.1
from statistics import mean
list = [15, 18, 2, 36, 12, 78, 5, 6, 9]
print(mean(list)) 

# v.2
list = [11, 13, 12, 15, 17]
import statistics as s
s.mean(list)

# round result
print("Average of the list =", round(result, 2)) 

#  from the task: the resuly values are rounded integers, maybe: 
print("Average of the list =", int(result)) 

# v.3 
# Python program to get average of a list 
# Using mean() 

# importing mean() 
from statistics import mean 

def Average(lst): 
    return mean(lst) 

# Driver Code 
lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 

# Printing average of the list 
print("Average of the list =", round(average, 2)) 
