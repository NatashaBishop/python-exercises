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

#missing data: 1st dictionary is one index shorter
# Initialize data of lists
data = [{'b': 2, 'c': 3}, {'a': 10, 'b': 20, 'c': 30}]
# Create pandas DataFrame
df = pd.DataFrame(data, index=['first', 'second'])
print(df)'''
    b   c     a
0   2   3   NaN
1  20  30  10.0'''
#NaN is printed instead of missing value@ the location df.loc[0, 'a'] or df.iloc[0, 2]
#loc vs iloc: loc is cocation by labels, iloc is location by indices

#DataFrame from DataFrame - getting chank of dataframe:
original_df = pd.DataFrame({
    'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
    'Age': [20, 21, 19, 18]
})
new_df = original_df[['Name']] 
print(new_df)'''
    Name
0    Tom
1   Nick
2  Krish
3   Jack'''


#DataFrame from a Dictionary of Series
# Initialize data to Dicts of series.
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}
# creates Dataframe.
df = pd.DataFrame(d)
print(df)'''
   one  two
a   10   10
b   20   20
c   30   30
d   40   40'''




# Create DataFrame using the zip() function 
# List1
Name = ['tom', 'krish', 'nick', 'juli']
# List2
Age = [25, 30, 26, 22]
# get the list of tuples from two lists.
# and merge them by using zip() - into list of tuples.
list_of_tuples = list(zip(Name, Age))
print("list_of_tuples:", list_of_tuples)
#  lists of tuples into Dataframe.
df = pd.DataFrame(list_of_tuples,
                  columns=['Name', 'Age'])
print(df)'''
list_of_tuples [('tom', 25), ('krish', 30), ('nick', 26), ('juli', 22)]
    Name  Age
0    tom   25
1  krish   30
2   nick   26
3   juli   22






