# Exercise within tha New city colledge course "AI programming with Python Level 3"
# Python script (code) to add two vectors using a non-vectorized approach (for loop)
list_A = [5,16,66,0,2,9]
list_B = [5,7,9,22,14,1]
result = []
for i in range(len(list_A)): #looping throug the list_A and adding item by item from list_B
    adding2lists = list_A[i] + list_B[i]
    result.append(result) # adding 2 result every item we went throug while adding

# Vectorized approach for Addition of Two Vectors
import numpy as np #numpy has to be installed from terminal: pip install numpy
list_A = [5,16,66,0,2,9]
list_B = [5,7,9,22,14,1]
result = []
np_array_A = np.array(list_A) # converting list  list_A into vector with help of numpy (issigned to np @ import stage)
np_array_B = np.array(list_B) #c above
adding2vectors = np_array_A + np_array_B # 2 vectors just add @ index level
