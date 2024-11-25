# numpy.full(shape, fill_value, dtype=None, order='C', *, device=None, like=None)
# Returns a new array of given shape and type, filled with fill_value.

import numpy as np

np.full((2, 2), np.inf)
#output array([[inf, inf],
#output        [inf, inf]])

np.full((2, 2), 10)
#output array([[10, 10],
 #output       [10, 10]])

np.full((2, 2), [1, 2])
#output array([[1, 2],
#output        [1, 2]])
