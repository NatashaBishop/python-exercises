stringGiven = "Hello, my name is Natalia"
'''
reading slices where first value ":" is start, 
in our case it is omited (":") so we start at the defauls value (from the first value). 
The next ":"  is the point where we finish, similarly to the first value it is omitted, 
so default falue is usded, which is the end of the data. 
"-1" means one step at the time and direction is backwards "-".
''' 
reversed_string = stringGiven[::-1]
print(reversed_string)

#Start: Empty, meaning the slicing starts from the beginning of the string.
#Stop: Empty, meaning the slicing goes until the end of the string.
#Step: -1, which means the string will be traversed backwards, effectively reversing the string.
