#inspired by https://www.digitalocean.com/community/tutorials/vectors-in-python
import numpy as np 

list1 = [10,20,30,40,50] 
list2 = [1,2,3,4,5]
vector1 = np.array(list1) 
vector2 = np.array(list2) 

divideVectors = vector1*vector2
print("Division of two vectors: ",divideVectors)
'''
Output:
Division of two vectors: [10  10  10 10 10]
'''
