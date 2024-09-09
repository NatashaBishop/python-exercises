# changing an integer data type to a complex data type using the complex() function

# x contains an integer value
x = 4
 
# print the integer
print(x) # Output: 4

# print the value of x after type casting it to a complex data type
print(complex(x)) # Output: (4+0j)

# P.S. we cannot convert a larger data type to a smaller data type since it leads to the loss of data. 
# changing a complex to integer will result in the loss of the imaginary part of the number. 
# !!!this kind of type casting is not supported by Python
