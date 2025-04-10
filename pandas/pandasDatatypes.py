import numpy as np
import pandas as pd

# Data using NumPy array
data = np.array([
    ['Blue', [1, 2], 1.1],
    ['Red', [3, 4], 2.2],
    ['Pink', [5, 6], 3.3],
    ['Grey', [7, 8], 4.4],
    ['Black', [9, 10], 5.5]
], dtype=object) # when we want to put different data types in a numpy array, we shoul declare the dtype as object

# Create DataFrame
df_from_numpy = pd.DataFrame(data, index=[1, 3, 5, 7, 9], columns=['color', 'list', 'number'])
print("DataFrame from NumPy Array:")
print(df_from_numpy)

# Data using Pandas Series
color_series = pd.Series(['Blue', 'Red', 'Pink', 'Grey', 'Black'], index=[1, 3, 5, 7, 9])
list_series = pd.Series([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], index=[1, 3, 5, 7, 9])
number_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5], index=[1, 3, 5, 7, 9])

# Create DataFrame
df_from_series = pd.DataFrame({
    'color': color_series,
    'list': list_series,
    'number': number_series
})
print("\nDataFrame from Pandas Series:")
print(df_from_series)

#1.2 Print the types for every column and the types of the first value of every column
# Print column types
# Print the types for every column
print("\nTypes of each column (NumPy DataFrame):")
for col in df_from_numpy.columns:
    print(f"{col}: {type(df_from_numpy[col])}")

print("\nTypes of each column (Pandas Series DataFrame):")
for col in df_from_series.columns:
    print(f"{col}: {type(df_from_series[col])}")

# Print types of the first value in each column
print("\nTypes of the first value in each column (NumPy DataFrame):")
for col in df_from_numpy.columns:
    print(f"{col}: {type(df_from_numpy[col].iloc[0])}")

print("\nTypes of the first value in each column (Pandas Series DataFrame):")
for col in df_from_series.columns:
    print(f"{col}: {type(df_from_series[col].iloc[0])}")
    


