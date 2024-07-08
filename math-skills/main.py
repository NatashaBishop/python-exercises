# Import statistics Library for calculations
import statistics

intList = [] # create empty list to store integers
with open('data.txt') as f:
  intList = [ int(i) for i in f ] # converting lines into integer

print("Average: ", int(statistics.mean(intList)))


#f.close()
