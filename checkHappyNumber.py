# https://en.wikipedia.org/wiki/Happy_number
# A happy number is defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

# Function to check if a number is a Happy Number
def is_Happy_num(n):
    past = set()  # Set to store previously encountered numbers during the process
    while n != 1:  # Continue the process until the number becomes 1 (a Happy Number) or a cycle is detected
        n = sum(int(i) ** 2 for i in str(n))  # Calculate the sum of squares of each digit in the number
        if n in past:  # If the current number has been encountered before, it forms a cycle
            return False  # The number is not a Happy Number
        past.add(n)  # Add the current number to the set of past numbers
    return True  # If the process reaches 1, the number is a Happy Number

# Test cases
print(is_Happy_num(7))
print(is_Happy_num(932))
print(is_Happy_num(6))

# Output:
# True
# True
# False

