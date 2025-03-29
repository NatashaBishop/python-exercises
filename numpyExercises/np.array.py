import numpy as np

np.array([1, 2, 3])
#output: array([1, 2, 3])

#Upcasting:
np.array([1, 2, 3.0])
#output: array([ 1.,  2.,  3.])

#More than one dimension:
np.array([[1, 2], [3, 4]])
#output: array([[1, 2],
#output:        [3, 4]])

#Minimum dimensions 2:
np.array([1, 2, 3], ndmin=2)
#output: array([[1, 2, 3]])

#Type provided:
np.array([1, 2, 3], dtype=complex)
#output: array([ 1.+0.j,  2.+0.j,  3.+0.j])

#Data-type consisting of more than one element:
x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
x['a']
#output: array([1, 3])

#Creating an array from sub-classes:
np.array(np.asmatrix('1 2; 3 4'))
#output: array([[1, 2],
#output:        [3, 4]])
np.array(np.asmatrix('1 2; 3 4'), subok=True)
#output: matrix([[1, 2],
#output:         [3, 4]])

'''Multidimensional lists in Python can have inconsistent types or dimensions, making conversion to a NumPy array impossible. 
For example, the list''' 
a = [[1, 2, 3, 4], [5, 6, 7], [8, 9]] #cannot be converted into a NumPy array.
