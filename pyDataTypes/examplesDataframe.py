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
     Name  Age
0   Nataliya   44
1   Alex   24
2   Alex   18
3   Jack   18'''
#dataframe has index column, can be customized


