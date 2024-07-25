# this exercise was inspired by the following article: 
# https://medium.com/@codingcampus/python-call-a-function-from-another-file-c41b9502ce70

# Creating the file you want to call the function from

# importing everything from file.py
# from file import * tells the compiler to import all the available functions in file.py
from file import *

# storing Hello_world() return value to world variable
world = Hello_World()
#printing world varaible to the screen
print(world)

# v.2
from file as fl
fl.Hello_World()
fl.addition()

# in case file.py is in another directory: 
from rootfolder.folder1.folder2.file import addition, subtract 
# notice that file extention is not there? 

