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

# bitwise right shift moves the bits of a number to the right by a specified number of positions. 
# empty spaces on the left are filled with zeros (for unsigned numbers) or the sign bit (for signed numbers)
# Shifting right effectively divides the number by 2 for each position shifted

# example: take 20 in binary (10100):
# In binary: 10100 (which is 20 in decimal)
# Shift it right by 1 position (>> 1):
# 10100 becomes 1010 (which is 10 in decimal)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#    Right Shift by 1: >> 1 is the same as dividing by 2.
#    Right Shift by 2: >> 2 is the same as dividing by 4 (2^2).
#    Right Shift by 3: >> 3 is the same as dividing by 8 (2^3), and so on.

b = 20  # Binary: 10100
b = b >> 1  # Right shift by 1
print(b)    # Output: 10
# shifting too far right can leave you with 0
b = 5  # Binary: 101
b = b >> 3  # Shift right by 3 positions
print(b)    # Output: 0 (since all bits are shifted out)

