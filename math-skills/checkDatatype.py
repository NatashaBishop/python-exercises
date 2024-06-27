a = 42
b = 3.14
c = "Hello, World!"
d = [1, 2, 3]
e = (1, 2, 3)
f = {"name": "John", "age": 30}

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>
print(type(d))  # Output: <class 'list'>
print(type(e))  # Output: <class 'tuple'>
print(type(f))  # Output: <class 'dict'>

# a function that checks if every element in this list is integer (which is false):

x = [1, 2.5, 'a']

def checkIntegers(x):
    # return True if all elements are integers, False otherwise
