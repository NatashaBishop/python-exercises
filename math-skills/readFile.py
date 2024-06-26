# we are reading file data.txt with data needed for calculation
# The second optional argument that the open() function accepts is mode. It specifies whether you want to read ("r"), write ("w"), or append ("a") to filename. 
# The default mode is the read ("r") mode.

# 'r' 	It opens a file for reading only.
# 'w' 	It opens a file for writing. If the file exists, it overwrites it, otherwise, it creates a new file.
# 'a' 	It opens a file for appending only. If the file doesn't exist, it creates the file.
# 'x' 	It creates a new file. If the file exists, it fails.
# '+' 	It opens a file for updating. 
# https://www.dataquest.io/blog/read-file-python/
# https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/
# 


f = open('data.txt', 'r')
print(f.read())
f.close()
