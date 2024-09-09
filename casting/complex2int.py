# The real numbers are a subset of Complex numbers and the complex numbers are the superset of real numbers.
# complex number has two parts, real and imaginary 

# access the real and imaginary part of a complex data type as float respectively:

# complex data type
x = 4 + 6j
#access the real part of the data 
print(x.real) # Output 4.0
#access the imaginary part of the data
print(x.imag) # Output 6.0

# we will first use the real attribute to change the complex number to a float 
# and then further use the int() function to convert the float data type to an integer: 

#complex data type
x = 4 + 6j
 
#the given complex number 
print("The given complex number: ", x)  # Output: The given complex number:  (4+6j)
 
#access the real part of the data and store it in a new variable 
r = x.real
 
#change the float to int 
i = int(r) 
 
#the equivalent integer
print("The equivalent integer: ", i) # Output: The equivalent integer:  4

# P.S. we cannot convert a larger data type to a smaller data type since it leads to the loss of data. 
# changing a complex to integer will result in the loss of the imaginary part of the number. 
# !!!this kind of type casting is not supported by Python
# there4 we cannot convert directly complex to integer
