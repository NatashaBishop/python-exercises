# https://www.geeksforgeeks.org/python-operators/

# bitwise operations manipulate the binary representations of the numbers
#    Bitwise NOT (~)
#    Bitwise right shift (>>)
#    Bitwise left shift (<<)
#    Bitwise AND (&)
#    Bitwise XOR (^)
#    Bitwise OR (|)
a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
# Output
# 0
# 14
# -11
# 14
# 2
# 40

# bitwise left shift moves the bits of a number to the left by a specified number of positions
# In binary, each bit represents a power of 2 
# and shifting the bits to the left is like multiplying the number by 2 for every shift.
# example: shift the number 5 (which is 101 in binary) to the left by 1 position. 
# the bits move one position to the left and a zero is added to the right.
# The 101 becomes 1010 (which is 10 in decimal)
#!!!!!!!!!! 
# Left Shift by 1: << 1 is the same as multiplying by 2.
# Left Shift by 2: << 2 is the same as multiplying by 4 (2^2).
# Left Shift by 3: << 3 is the same as multiplying by 8 (2^3), and so on.

b = 5       # Binary: 101
b = b << 1  # Left shift by 1 (binary 1010)
print(b)    # Output: 10



