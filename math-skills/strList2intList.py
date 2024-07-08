#  task is converting a list of strings to a list of integers
# https://medium.com/@nawazmohtashim/convert-string-list-to-integer-list-in-python-489a61684496

string_list = ['1', '2', '3', 'four', '5']
integer_list = []

for s in string_list:
    try:
        integer_list.append(int(s))
    except ValueError:
        print(f"Warning: Unable to convert '{s}' to an integer.")

print(integer_list)
