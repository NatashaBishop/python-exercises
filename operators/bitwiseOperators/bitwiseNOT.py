# bitwise operations manipulate the binary representations of the numbers
#    Bitwise NOT (~)
#    Bitwise right shift (>>)
#    Bitwise left shift (<<)
#    Bitwise AND (&)
#    Bitwise XOR (^)
#    Bitwise OR (|)

'''Bitwise NOT (~) Operator

The bitwise NOT operator (~) inverts all the bits in a number. In other words, it changes all 1s to 0s and all 0s to 1s. This operation is also called bitwise complement.

However, because of how negative numbers are stored in Python (using a system called two's complement), the result of a bitwise NOT might seem a little counterintuitive at first. But let’s break it down step by step.
How Bitwise NOT Works:

    Binary Representation:
        A number in binary is a sequence of bits (0s and 1s). The bitwise NOT operator flips these bits.
        For example, inverting the binary number 1010 (which is 10 in decimal) will result in 0101.

    Two's Complement:

        In most programming languages (including Python), negative numbers are represented using two's complement. This means:
            The highest bit (leftmost bit) in a number is treated as a sign bit.
            Positive numbers have a 0 in the sign bit, while negative numbers have a 1 in the sign bit.
            For negative numbers, two's complement works by inverting the bits of the positive number and adding 1.

        As a result, when you apply the bitwise NOT operation on a positive integer, you effectively get a negative number.

Example:

Let’s take an example of 10 in binary, which is 1010 in binary (ignoring leading zeros).
'''
a = 10        # Binary: 00000000 00000000 00000000 00001010 (32-bit representation)
b = ~a        # Apply bitwise NOT
print(b)      # Output: -11
'''
Here’s what happens:

    The binary representation of 10 is 00000000 00000000 00000000 00001010.
    Applying ~ flips all bits: 11111111 11111111 11111111 11110101 (this is the two's complement representation of -11).

Thus, ~10 gives -11.
Why is the Result Negative?

This is due to the two's complement system. When you flip all the bits of a positive number, you essentially get the negative counterpart plus one. So, when you perform a bitwise NOT on 10, you get -11.
Another Example:

'''

x = 5        # Binary: 00000000 00000000 00000000 00000101
y = ~x       # Apply bitwise NOT
print(y)     # Output: -6
'''
Explanation:

    The binary of 5 is: 00000000 00000000 00000000 00000101.
    Applying the bitwise NOT flips all the bits: 11111111 11111111 11111111 11111010 (which represents -6 in two's complement).

Bitwise NOT for Negative Numbers:

Let’s see how bitwise NOT works for a negative number:

'''

x = -3       # Binary: 11111111 11111111 11111111 11111101 (two's complement representation of -3)
y = ~x       # Apply bitwise NOT
print(y)     # Output: 2
'''
Explanation:

    The binary of -3 is 11111111 11111111 11111111 11111101.
    Applying ~ flips all the bits: 00000000 00000000 00000000 00000010 (which is 2 in decimal).

In Summary:

    The bitwise NOT operator flips all the bits of a number.
    Due to two's complement representation, applying ~ on a positive number results in a negative number.
    For a number n, ~n is equivalent to -(n + 1).
