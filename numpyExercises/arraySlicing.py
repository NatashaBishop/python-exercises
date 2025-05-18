import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:2]) #from index [0] to up2 [2], but not including [2]
#output: [1 2] 
#Negative Slicing

#Use the minus operator to refer to an index from the end:
#Slice from the index -3 (start from the end ) to index -1 (from the end it is the 1st index, no 0 index at the end):
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
print(arr2[1, 1:4]) #first "1" is the index of row, second row. then  in thet row 1:4 (not included index [4])
#output: [7 8 9]


arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
'''This creates a 2D NumPy array (arr2) with two rows and five columns:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]'''
print(arr2[0:2, 2]) 
'''selects rows from index 0 to 1 (0:2 means rows 0 and 1) and column at index 2.
Breakdown:
    arr2[0, 2] → 3 (Row 0, Column 2)
    arr2[1, 2] → 8 (Row 1, Column 2)'''
#output: [3 8]

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2, 1:4]) 
#output: [2 3 4 7 8 9]


