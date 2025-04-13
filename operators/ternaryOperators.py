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
#Output: b is greater

#Syntax: (condition_is_false, condition_is_true)[condition]
n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)  
#Output: Odd

# Example with == condition
x = 5
y = 5

# Ternary operator to check equality
result = "x is equal to y" if x == y else "x is not equal to y"
print(result)
# Output: x is equal to y

#=======================
# Ternary operators, also known as conditional expressions
# Syntax: true_value if condition else false_value

# Example: Determine which value is smaller
a, b = 10, 20
print("a is minimum" if a < b else "b is minimum")  # Output: a is minimum

# Example: Nested ternary operator
a, b = 10, 20
print("Both are equal" if a == b else "a is greater" if a > b else "b is greater")  # Output: b is greater

# Example: Check if a number is odd or even
n = 7
print("Even" if n % 2 == 0 else "Odd")  # Output: Odd

# Example: Check equality between two numbers
x, y = 5, 5
print("x is equal to y" if x == y else "x is not equal to y")  # Output: x is equal to y

# Example: Check if a list is empty
my_list = []
print("List is empty" if not my_list else "List is not empty")  # Output: List is empty

Improvements:

    Concise variable declarations:
        Used tuple unpacking (a, b = 10, 20) for cleaner variable initialization.

    Removed redundant comments:
        Simplified comments while keeping them descriptive.

    Direct print statements:
        Avoided intermediate variables like result where they are not necessary.

    Pythonic syntax:
        Used not my_list to check for an empty list, which is cleaner and more Pythonic.

This version is simpler, cleaner, and follows Python's idiomatic style, making it easier to read and maintain.

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights

    Settings

Files
t

accessElements
casting
count
imgs
listManipulation
math-skills
numpyExercises
operators

bitwiseOperators
==VSis.py
arithmeticOperators.py
assignmentOperators.py
identityOperators.py
logicalOperators.py
membershipOperators.py

    ternaryOperators.py

pandas
pyDataTypes
pyModules
stringManipulation
workWithFiles
README.md
absoluteValue.py
add_three_numbers.py
callFunctionFromFunction.py
checkHappyNumber.py
dialogWithUser-8.py
divisionByZeroErrorHandling.py
extend.py
extendVSappend.py
globalVariable.py
identifyEvenOdd.py
input2listORtuple.py
inputExeption.py
joinItemsInList.py
listLength.py
multipleStringsInput.py
passVar2func.py
passwordGenerator.py
print1-10for-loop.py
printDatatype.py
printDictionaryPairs.py
printEvenIndexCharacters.py
printSyntax.py
printVersion.py
pythonDOMexample.py
random.py
rangeExamples.py
readFileExtention.py
readFile_skip_line_writeFile.py
readingSlices.py
removeDuplicatesFromList.py
spaceRemover.py
splitInputWordsIntoArray.py
squaresTable.py
storeFunction2Variable.py
takeInputFromPrintStatement.py

    write2existingFile.py

    python-exercises/operators

/ternaryOperators.py
NatashaBishop
NatashaBishop
Update ternaryOperators.py
4e856de
 · 
Apr 12, 2025

    python-exercises/operators

/ternaryOperators.py

38 lines (31 loc) · 990 Bytes
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
#Output: b is greater

#Syntax: (condition_is_false, condition_is_true)[condition]
n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)  
#Output: Odd

# Example with == condition
x = 5
y = 5

# Ternary operator to check equality
result = "x is equal to y" if x == y else "x is not equal to y"
print(result)
# Output: x is equal to y


