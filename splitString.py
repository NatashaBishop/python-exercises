#inspired by https://www.w3schools.com/python/python_examples.asp
a = "Hello, World!"
b = a.split(",") #will form list with bits of text separated by coma
print(b)
#output: ['Hello', ' World!']
#===== new file
#split particular index:
a = "Hello,c World! aaa"
b = a.split(" ") #splitting by space into array
c = b[0].split(",") #splitting by coma first element of the array
print(a)
print(b)
print(c)
#output:
# Hello,c World! aaa
# ['Hello,c', 'World!', 'aaa']
# ['Hello', 'c']
