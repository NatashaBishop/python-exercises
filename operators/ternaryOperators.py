#  Ternary operators also known as conditional expressions
# Ternary Operator determines if a condition is true or false and then returns appropriate value as the result
# Syntax: true_value if condition else false_value

# Example Ternary If Else:
a = 10
b = 20
# python ternary operator
min = "a is minimum" if a < b else "b is minimum"
print(min)
#Output:
#a is minimum

# Ternary Operator in Nested If else
# Syntax: true_value  if condition1 else (true_value if condition2  else false_value)

# Python program to demonstrate nested ternary operator
a = 10
b = 20
print("Both are equal" if a == b else "a is greater"
      if a > b else "b is greater")
#Output:
#b is greater

#Syntax: (condition_is_false, condition_is_true)[condition]
n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)  
#Output: Odd
