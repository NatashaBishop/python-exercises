import numpy as np 
#create list
myLst = [10,20,30,40,50] 
#create vector (numPy array)
myVector = np.array(myLst) 
print(f'Vector created from the list myLst (NumPy array):\n{myVector}')
# Output:
# Vector created from the list myLst (NumPy array):
# [10 20 30 40 50]

#converting to list with tolist()
newList = myVector.tolist()
print(f'new list: {newList}')

#multi-dimensional NumPy Array 2 List:
# 2d array to list
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

print(f'NumPy Array:\n{arr_2}')

# 2d array to list
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f'NumPy Array:\n{arr_2}')
list_2 = arr_2.tolist()
print(f'List: {list_2}')

#output: [[1, 2, 3], [4, 5, 6]]

