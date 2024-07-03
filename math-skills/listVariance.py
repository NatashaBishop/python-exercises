# How to calculate Variance in maths?
# Variance is the spread between numbers in a data set. Variance is a statistical measurement used to determine how far each number is from the mean and from every other number in the set. You can calculate the variance by taking the difference between each point and the mean.
# It is the average of each point from the mean. 



# Python3 code to demonstrate working out Variance of List, using mean
# using loop + formula 
 
# initialize list 
test_list = [6, 7, 3, 9, 10, 15] 
 
# printing original list 
print("The original list is : " + str(test_list)) 
 
# Variance of List 
# using loop + formula 
mean = sum(test_list) / len(test_list) 
res = sum((i - mean) ** 2 for i in test_list) / len(test_list) 
 
# printing result 
print("The variance of list is : " + str(res)) 

