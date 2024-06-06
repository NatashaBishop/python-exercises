# How to split phrase into array of separate words (strings) from one input() call
# .split will separate input by individual strings and write them into array

str = []
str = input("Enter frase with 4 words: ").split()
print('word1 is:', str[0])
print('word2 is:', str[1])
print('word3 is:', str[2])
print('word3 is:', str[3])

# .split is a built-in function and wil split into array any string: 
#input = "I am xyz"
#output = input.split()
#print(output)
#output example:
#['I', 'am', 'xyz']
