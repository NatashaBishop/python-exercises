# Python script (code) to add two vectors using a non-vectorized approach (for loop)
list_A = [5,16,66,0,2,9]
list_B = [5,7,9,22,14,1]
result = []
for i in range(len(list_A)):
    multiply2lists = list_A[i]+list_B[i]
    result.append(result)

# Vectorized Addition of Two Vectors
import numpy as np
list_A = [5,16,66,0,2,9]
list_B = [5,7,9,22,14,1]
result = []
np_array_A = np.array(list_A)
np_array_B = np.array(list_B)
multiply2vectors = np_array_A+ np_array_B
