#

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
index=['row 1', 'row 2'],
columns=['col 1', 'col 2'])
df1.to_excel("output.xlsx")  
#specify the sheet name:
df2.to_excel("output.xlsx", sheet_name='Sheet_name_1')

# writing 2 datasets into one excel file
# write to multiple sheets: we need to create an ExcelWriter object with a target file name, and specify a sheet in the file to write to.
df2 = df1.copy() #create 2nd dataset
with pd.ExcelWriter('output.xlsx') as writer:  
    df1.to_excel(writer, sheet_name='Sheet_name_1')
    df2.to_excel(writer, sheet_name='Sheet_name_2')
