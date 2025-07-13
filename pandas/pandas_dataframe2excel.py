#

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
index=['row 1', 'row 2'],
columns=['col 1', 'col 2'])
df1.to_excel("output.xlsx")  
#specify the sheet name:
df2.to_excel("output.xlsx", sheet_name='Sheet_name_1')
