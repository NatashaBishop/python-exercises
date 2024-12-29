#inspired by https://www.digitalocean.com/community/tutorials/vectors-in-python
import numpy as np 

list1 = [10,20,30,40,50] 
list2 = [1,2,3,4,5]
vector1 = np.array(list1) 
vector2 = np.array(list2) 

subtractVectors = vector1-vector2
print("subtraction  of two vectors: ",subtractVectors)
'''
Output:
subtraction of two vectors:  [ 9 18 27 36 45]
'''
