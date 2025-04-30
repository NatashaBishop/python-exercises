# declare list:
list = ['I', 'am', 'xyz']

print(list)
#output: ['I', 'am', 'xyz']

print('index 0 is:', list[0])
print('index 1 is:', list[1])
print('index 3 is:', list[2])
'''output: 
index 0 is: I
index 1 is: am
index 3 is: xyz
'''
#Access last item of the list:
print(list[-1])

#Third, fourth, and fifth item (index 4, not 5):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# from the beginning to index 3 - 4th item:
print(thislist[:4])

# from "cherry" and to the end:
print(thislist[2:]) #from index 3 incl

#from index -4 (included) to index -1 (excluded)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
