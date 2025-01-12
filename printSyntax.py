#https://medium.com/@DoneWithWork/5-different-ways-to-print-in-python-17528bb5c173


print("Today's date =", myVariableName)
print(f'My text: {myVariable}')
#Print two messages, and specify the separator:
print("Hello", "how are you?", sep="---") # --- is the separatoe between strings
#output: Hello---how are you? 

print("Hello", "how are you?")
# output: Hello how are you? 

#print string with variable inside, with f functionality
print(f'this is my variable value: {myVariableName}')

#embed variables inside of string with format function
print("{} is my first_name and {} is my last name".format(first_name,family_name))
