# Syntax of complex() in Python: complex datatype components are: real number and imaginary number 
complex(real, imaginary)

# example1: 
real = 3
imaginary = 5
z = complex(real, imaginary)
print("The complex number is ", z)
# Output: The complex number is  (3+5j)

# example2: 
# We can also declare a Complex Data Type in Python using the string literal of type “a + bj”.
# Defining Complex Number using the string literal
complex_num = 2 + 4j
print("The complex number is ", complex_num)
# Output: The complex number is  (2+4j)

# Example 3 
# The Arithmetic Operations such as Addition, Subtraction, Multiplication 
# and Division can be performed on the Complex Data Type in Python.
# Declaring Complex Numbers:
a = 2 + 3j
b = 1 - 2j
# Performing Arithmetic Operations
z1 = a + b
z2 = a - b
z3 = a * b
z4 = a / b
# Printing Output
print("The result of addition is ", z1)
print("The result of subtraction is ", z2)
print("The result of multiplication is ", z3)
print("The result of division is ", z4)
