# accepts a sentence and calculate the # calculate number of upper case letters and lower case letters. 
# 4 example: input is "Hello world!". Then, the output will be: UPPER CASE 1 LOWER CASE 9 
#  input data supplied  is a console input

s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
