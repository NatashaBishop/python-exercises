#inspired by https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_hints_with_solutions.md
# pip install numpy

#install from inside of the file, installs only 4 that file:
# %pip install numpy

# in jupiter notebook and some OS  sometimes needs % too in the terminal:
# %pip install numpy

# Importing the NumPy library with an alias 'np'
import numpy as np #np is just an alias

# Printing the version of NumPy installed
print(np.__version__)

# Printing the configuration details of NumPy
print(np.show_config())

# Use inbuilt help: printing information about the np.add function using the np.info() method
print(np.info(np.add))
