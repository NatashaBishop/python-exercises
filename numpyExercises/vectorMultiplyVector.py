#inspired by https://www.digitalocean.com/community/tutorials/vectors-in-python
import numpy as np 

list1 = [10,20,30,40,50] 
list2 = [1,2,3,4,5]
vector1 = np.array(list1) 
vector2 = np.array(list2) 

multiplyVectors = vector1*vector2
print("Multiplication of two vectors: ",multiplyVectors)
'''
Output:
Multiplication of two vectors: [10  40  90 160 250]
'''
