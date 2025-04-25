# DataFrame is Pandas datatype
import pandas as pd

# Empty DataFrame created:
df = pd.DataFrame()
print(df)
'''Output 
Empty DataFrame
Columns: []
Index: []'''

# dictionary to dataframe
#create dictionary@
dataDic = {'clientName': ['Nataliya', 'Alex', 'Alex', 'Jack'],
        'Age': [44, 24, 18, 18]}
# dictionary to dataframe
df = pd.DataFrame(dataDic)
print(df)
'''output:
    Name       Age
0   Nataliya   44
1   Alex       24
2   Alex       18
3   Jack       18'''
#dataframe has index column, can be customized

# DataFrame from Lists or Arrays
#Creating list of lists
data = [['Nataliya', 10], ['Alex', 15], ['Alex', 14]]

# Lists or Arrays to DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

#DataFrame from List of Dictionaries
#create List of Dictionaries:
# Initialize List of Dictionaries
data = [{'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}]
# list to DataFrame.
df = pd.DataFrame(data)
print(df)
'''output
    a   b   c
0   1   2   3
1   10  20  30'''

#pass custom indices
df = pd.DataFrame(data, index=['first', 'second'])
'''output
        a   b   c
first   1   2   3
second  10  20  30'''

