# How to split a string with phrase into a list of separate strings: 
# calling .split fanction will separate initial string (by spaces) into individual strings and write them into list

# declare empty list:
list = []
# initiate string:
str = "I am xyz"
list = str.split()
print('word1 is:', str[0])
print('word2 is:', str[1])
print('word3 is:', str[2])
print('word3 is:', str[3])
print(list)
#output: ['I', 'am', 'xyz']

print('word1 in string is:', str[0])
print('word2 in string is:', str[1])
print('word3 in string is:', str[2])
print('word3 in string is:', str[3])
