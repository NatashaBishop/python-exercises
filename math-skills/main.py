# Import statistics Library for calculations
import statistics

intList = [] # create empty list to store integers
with open('data.txt') as f:
    intList = [int(line.strip()) for line in f if line.strip()] # converting lines into integer and avoid empty lines (strip)

if not intList:  # Check if the list is empty
    print("The list is empty, cannot calculate average.")
else:
    print("Average:", int(statistics.mean(intList)))
    print("Median:", int(statistics.median(intList)))
    print("Variance:", int(statistics.variance(intList) if len(intList) > 1 else 0)) # Variance requires at least 2 data points
    print("Standard Deviation:", int(statistics.stdev(intList) if len(intList) > 1 else 0)) # Standard deviation requires at least 2 data points
