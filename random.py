import random
#generate random between 10 and 20
print(random.randrange(10,20))
#output: 12

#random from given list:
num =[1,2,3,4,5]
print(random.choice(num))
#output: 4

#shuffle randomly the list
random.shuffle(num)

print(num)
#output: [4, 2, 3, 1, 5]

#generate random without fotmating: 
print(random.random())
##output: 0.7608972700234574




