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


