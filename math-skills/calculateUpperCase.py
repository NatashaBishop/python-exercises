# accepts a sentence and calculate the # calculate number of upper case letters and lower case letters. 
# 4 example: input is "Hello world!". Then, the output will be: UPPER CASE 1 LOWER CASE 9 
#  input data supplied  is a console input

s = input()
# Initialize Dictionary.
# This initializes a dictionary d with two keys: "UPPER CASE" and "LOWER CASE", both with value of 0.
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s: #terate Over String. this iterates over each character c in the string s: 
    if c.isupper():
        d["UPPER CASE"]+=1 # increment the value associated with the key "UPPER CASE" by 1.
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass # If c is neither uppercase nor lowercase (digits, punctuation, space...), do nothing
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
