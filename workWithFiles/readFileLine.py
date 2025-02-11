#Read one line of the file:
f = open("input.txt", "r")
print(f.readline()) 
#Read 2 lines of the file:
f = open("input.txt", "r")
print(f.readline()) 
print(f.readline()) 
#Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x) 
f.close()
