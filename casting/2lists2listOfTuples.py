
# initialize 1st list
Name = ['tom', 'krish', 'nick', 'juli']
# initialize 2nd list
Age = [25, 30, 26, 22]
# get the list of tuples from two lists.
# and merge them by using zip().
list_of_tuples = list(zip(Name, Age))
print("list_of_tuples:", list_of_tuples)
print(df)
'''output: 
list_of_tuples: [('tom', 25), ('krish', 30), ('nick', 26), ('juli', 22)]
