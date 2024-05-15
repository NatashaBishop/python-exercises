#Given a dictionary, write a Python script that prints all the keys and their corresponding values 
#in the format "key: value".  
# creating dictionary
dictionary = {'hours': 7, 'days': 2, 'workers': 3, 'weeks': 4}

# inbuilt python items() method is used to iterate over the key-value pairs in the dictionary.
for key, value in dictionary.items():
# Print keys and values
    print(f"{key}: {value}")
    '''f-string  is used to fomat string the way we want: key:value where placeholders key and value 
    are replaced 
    with actual values while iterating through pairs'''
