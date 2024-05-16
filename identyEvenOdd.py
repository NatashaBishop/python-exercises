# Python that identifies the even or odd number

# ask the user for number and store it into variable userNumber
userEntry = input("Please, enter you number: ")

# the input is a string, we need to convert it to interger in order to perfom mathimatical operation
IntergerNumber = int(userEntry)

# Checking if its even. If the number can be devided by 2 without remainder, then it's even 
if IntergerNumber % 2 == 0:
    print("The number you have entered is even")
else:
    print("The number you have entered is odd")
