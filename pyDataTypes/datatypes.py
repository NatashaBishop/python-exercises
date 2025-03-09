numpy_21_array = np.array([
    22,                     # Integer index0 ok
    35.19,                  # Float index1 ok
    "nice weather",         # String index2 
    [48, 2, 19],            # List index3
    (48, 2, 19),             # Tuple index4
    {"key": "value"},       # Dictionary index5 https://www.geeksforgeeks.org/python-dictionary/
    {48, 2, 19},              # Set index6
    True                    # Boolean index7
], dtype=object)  # Specify object dtype
