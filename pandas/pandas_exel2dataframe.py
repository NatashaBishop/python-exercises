
file = pd.ExcelFile('myfile.xlsx')  
with pd.ExcelFile("myfile.xls") as xls:  
df1 = pd.read_excel(xls, "Sheet1")  
