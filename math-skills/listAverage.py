# calculate average of  list 

# For Python 3.4+, use mean() from the new statistics module to calculate the average:
# v.1
from statistics import mean
list = [15, 18, 2, 36, 12, 78, 5, 6, 9]
print(mean(list)) 

# v.2
list = [11, 13, 12, 15, 17]
import statistics as s
s.mean(list)
