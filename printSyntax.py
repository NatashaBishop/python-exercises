#https://medium.com/@DoneWithWork/5-different-ways-to-print-in-python-17528bb5c173


print("Today's date =", myVariableName)
print(f'My text: {myVariable}')
#Print two messages, and specify the separator:
print("Hello", "how are you?", sep="---") # --- is the separatoe between strings
#output: Hello---how are you? 

print("Hello", "how are you?") # coma incerts space
# output: Hello how are you? 

#print string with variable inside, with f functionality
print(f'this is my variable value: {myVariableName}')

#embed variables inside of string with format function
print("{} is my first_name and {} is my last name".format(first_name,family_name))

# coma vs +: coma leave a space between variables and strings whereas "+" joins variables and strings as is. 
name = "Natasha"
age = 18
print("My name is" + name + "and I am" + age + "years old.")
#output: 
# My name isNatashaand I am18years old.
print("My name is", name, "and I am", age, "years old.")
#output: 
# My name is Natasha and I am 18years old.

#Using String Formatting:
#using the % operator to format string, followed by a variable name enclosed in curly braces {}
print("My name is %s and I am %d years old." % (name, age))
#output: 
# My name is Natasha and I am 18years old.
