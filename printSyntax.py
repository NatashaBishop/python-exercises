#https://medium.com/@DoneWithWork/5-different-ways-to-print-in-python-17528bb5c173


print("Today's date =", myVariableName)
print(f'My text: {myVariable}')
#Print two messages, and specify the separator:
print("Hello", "how are you?", sep="---") # --- is the separatoe between strings
#output: Hello---how are you? 

print("Hello,", "how are you?") # coma incerts space
# output: Hello, how are you? 

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
#works similar to .format
#output: My name is Natasha and I am 18years old.

first_name = "ada"
last_name = "lovelace" 
#assign formated statement to a variale
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#print() with separator and end parameters:
a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')
'''output:
a =000005 #separator between "a =" and a is 00000


a =05'''

#prevent a line break: end=''
print ("Hello, Friend!", end='')
print ("It is awesome to see you!")
#output: Hello, Friend! It is awesome to see you!

