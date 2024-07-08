# Import statistics Library for calculations
import statistics

f = open('data.txt', 'r')
#print(f.read())

# a function that checks if every element in this list is integer (which is false):
def checkIntegers(f):
    # return True if all elements are integers, False otherwise

# To check whether all elements in a list are integers
    set(map(type, f)) == {int}
    return True
print(statistics.mean(f)) 
print("Average: ", int(statistics.mean(f)))

#f.close()
