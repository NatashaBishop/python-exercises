#Read one line of the file:
f = open("input.txt", "r")
print(f.readline()) 
f.close()
#Read 2 lines of the file:
f = open("input.txt", "r")
print(f.readline()) 
print(f.readline()) 
#Loop through the file line by line:
f = open("input.txt", "r")
for x in f:
  print(x) 
f.close()

#stripping the newline character:
with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
