string_num = "225"
print(type(string_num))
# Output class 'str'

# converting str to integer
num1 = int(string_num)

print("Integer number 1:", num1)
# Output 225
print(type(num1))
# Output class 'int'

# When converting string type to int type, a string must contain integral value only and should be base-10. Otherwise we will have ValueError: 
string_num = 'Score is 25'
print(type(string_num))
# Output class 'str'

# ValueError: invalid literal for int() with base 10: 'Score is 25'
num = int(string_num)
print(num)
