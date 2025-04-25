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
