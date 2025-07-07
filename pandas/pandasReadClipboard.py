#inspired by https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
df.to_clipboard()  
pd.read_clipboard()  '''
     A  B  C
0    1  2  3
1    4  5  6 '''
