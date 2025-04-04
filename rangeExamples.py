#inspired by https://pynative.com/python-range-function/
'''syntax of the range() function: 
range(start, stop[, step])
It takes three arguments. Out of the three, two are optional. The start and step are optional arguments and the stop is the mandatory argument.
start - optional  argument, default value is 0 if not specified.
step - optional  argument. Specify the increment value. Each next number in the sequence is generated by adding the step value to a preceding number. 
    The default value is 1 if not specified. It is nothing but a difference between each number in the result. 
    For example, range(0, 6, 1) - where step = 1.
stop - mandatory argument, range() never includes the stop number in its result'''

#Return Value of range() is the object of class range. for example:
print(type(range(10)))
# Output: <class 'range'>

# Generate numbers between 0 to 6
for i in range(6): #where 6 is mandatory argument stop
    print(i)
'''
Output:
0
1
2
3
4
5
'''
#Pass the step value to range()
#The step specifies the increment. For example:
for i in range(0, 6, 2) #step = 2 
    print(i)
#output: [0, 2, 4] #6 is not included because we are dealing with numbers up to 6 (from 0 to 5)

#range() loop example with stop argument:
# Print first 10 numbers (stop = 10)
for i in range(10):
    print(i, end=' ') #end indicates hou the each iteration ends: separated by spaces instead of starting on a new line.

# output 0 1 2 3 4 5 6 7 8 9
# outputwithout end=' '
'''
0
1
2
3
4
5
6
7
8
9

Note:

    Here, start = 0 and step = 1 as a default value.
    If you set the stop as a 0 or some negative value, then the range will return an empty sequence.
    If you want to start the range at 1 use range(1, 10).'''

#range(start, stop, step)
# Numbers from 10 to 15
# start = 10
# stop = 50
# step = 5
for i in range(10, 50, 5):
    print(i, end=' ')

# Output: 10 15 20 25 30 35 40 45 - starting from the start number, increments by step number, and stops before a stop number.

#Use range() to generate a sequence of numbers starting from 9 to 100 divisible by 3.
# start = 9
# stop = 100
# step = 3 (increment)
for i in range(9, 100, 3):
    print(i)


#Iterate a list using range() and for loop
list1 = ['Jessa', 'Emma', 20, 30, 75.5]
for i in range(len(list1)):
    print(list1[i])
'''Output:
Jessa
Emma
20
30
75.5
'''
#Reverse range Using negative step: 
# start = 5
# stop = -1
# step = -1 - cause the for loop to iterate in reverse order
for i in range(5, -1, -1):
    print(i)
'''Output:
5
4
3
2
1
0'''


