import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:2]) #from index [0] to up2 [2], but not including [2]
#output: [1 2] 
#Negative Slicing

#Use the minus operator to refer to an index from the end:
#Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1]) 
#output: [5 6] 

#step value determines the step of the slicing:
print(arr[1:5:2]) 
#output: [2 4]

#Return every other element from the entire array:
print(arr[::2]) # :: from start-to finish indexes, 2 - step value
#output: [1 3 5 7]

#Slicing 2-D Arrays
#From the second element, slice elements from index 1 to index 4 (not included):
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1, 1:4]) 
#output: [7 8 9]


