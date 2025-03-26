'''Upcasting in the context of NumPy arrays refers to promoting an element in an array to a higher data type to accommodate operations or maintain precision. For example, when performing calculations between arrays of different data types, NumPy promotes the result to the most precise data type among the inputs.'''
np.array([1, 2, 3.0])
array([ 1.,  2.,  3.]) # interger is upcasted to 
print(array.dtype)  # Result: float64
#the integer 1 is upcast to a float64 to match the precision of the float 3.0
