# Define a function named divide_numbers that takes two parameters: x and y.
def divide_numbers(x, y):
    try:
        # Attempt to perform the division operation and store the result in the 'result' variable.
        result = x / y
        # Print the result of the division.
        print("Result:", result)
    except ZeroDivisionError:
        # Handle the exception if a division by zero is attempted.
        print("The division by zero operation is not allowed.")

#usage
x = 100
y = 0
divide_numbers(x, y)
