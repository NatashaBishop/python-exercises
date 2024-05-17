#print even index characters 

# ask user for input
input = input('Enter input ')

# print input
print("Original String:", input)

# get the length of a string
size = len(input)

print("Printing only even index chars: ")

# for loop iterates over a range of numbers from 0 up to size - 1, incrementing by 2 each time
for i in range(0, size - 1, 2): 

# print index i enclosed within square brackets along with the value of input[i]
# input variable is iterable object. This line will print the value of input at indices 0, 2, 4, etc., depending on the size of input.
    print("index[", i, "]", input[i])
