import numpy as np

np.ones(5)
#output: array([1., 1., 1., 1., 1.])
##########
np.ones((5,), dtype=int)
#output: array([1, 1, 1, 1, 1])
##########
np.ones((2, 1))
#output: array([[1.],
#output:        [1.]])
##########
s = (2,2)
np.ones(s)
#output: array([[1.,  1.],
#output:        [1.,  1.]])
