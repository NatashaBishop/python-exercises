#if file doesn’t exist, creates  it  
f = open("demofile2.txt", "a") #the "a" means append mode, adds new content to the end of the file, does not erase what’s already there


f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read()) 

# Open the file "demofile3.txt" and overwrite the content:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read()) 
