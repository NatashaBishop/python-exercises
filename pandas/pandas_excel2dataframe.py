#Class for parsing tabular Excel sheets into DataFrame objects: pandas.ExcelFile
#class pandas.ExcelFile(path_or_buffer, engine=None, storage_options=None, engine_kwargs=None)


Class for parsing tabular Excel sheets into DataFrame objects.
file = pd.ExcelFile('myfile.xlsx')  
with pd.ExcelFile("myfile.xls") as xls:  
df1 = pd.read_excel(xls, "Sheet1")  
