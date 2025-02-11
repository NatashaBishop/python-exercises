# read text from file in2 string:
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print(type(text))
#get 1st 30 characters:
print(text[:30])
#get from 3rd to 1st 30 characters:
print(text[2:30])
'''output:
Specifically, we’ll present th
ecifically, we’ll present th
'''
