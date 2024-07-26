mylist = ["a", "b", "a", "c", "c"]
# Create a dictionary, using the List items as keys. This will automatically remove any duplicates because dictionaries cannot have duplicate keys: dict.fromkeys(mylist)
# Then convert the dictionary back into a list: list(...)
mylist = list(dict.fromkeys(mylist))
print(mylist) 
