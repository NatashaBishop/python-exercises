#inspired by https://www.w3schools.com/python/python_examples.asp
a = "Hello, World!"
b = a.split(",")
print(b)
#output: ['Hello', ' World!']
#===== new file
#split particular index:
a = "Hello,c World! aaa"
b = a.split(" ")
c = b[0].split(",")
print(b)
print(c)
#out:
#['Hello,c', 'World!', 'aaa']
#['Hello', 'c']