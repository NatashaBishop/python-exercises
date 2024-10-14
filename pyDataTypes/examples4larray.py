#1. Basic Array Creation
#create an array in Python using the array module, we need to specify the type code (which defines the type of elements) and a list of initial values.
'''Array Type Codes
The array module supports several type codes 2 define the type of elements the array holds:
Type_Code	C_Type          Python_Type
'b'	      signed char      int
'B'	      unsigned char	  int
'h'	      signed short	  int
'H'	      unsigned short	int
'i'	      signed int	    int
'I'	      unsigned int	  int
'f'	      float	          float
'd'	      double	        float
'''
from array import array

# Create an array of signed integers ('i' is the type code for integers)
arr = array('i', [1, 2, 3, 4, 5])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])
