import pandas as ps 
#added the path for the 150 author geographical data as an test 
excel_file_path = '150 Authors Geography with Birthplace included.xlsx'
#data frame 
df= ps.read_excel(excel_file_path)

print(df.head())
#temporary end of program 