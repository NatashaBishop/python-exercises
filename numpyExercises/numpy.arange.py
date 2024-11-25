#numpy.arange([start, ]stop, [step, ]dtype=None, *, device=None, like=None)
#Return evenly spaced values within a given interval.

import numpy as np

np.arange(3)
#output: array([0, 1, 2])

np.arange(3.0)
#output: array([ 0.,  1.,  2.])

np.arange(3,7)
#output: array([3, 4, 5, 6])

np.arange(3,7,2)
#output: array([3, 5])
