#function that looks 4 text
def process(line):
    if 'should you choose' in line.lower():
         print('found text')

#call function that looks for text while reading text file line by line
with open('input.txt') as f:
    for line in f:
        process(line)

