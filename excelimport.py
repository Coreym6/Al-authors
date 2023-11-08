#import pandas as ps 
# need to set up an anaconda environment 
import pandas as ps
''' #added the path for the 150 author geographical data as an test '''
excel_file_path = '150 Authors Geography with Birthplace included.xlsx'
try:
     df = ps.read_excel(excel_file_path, sheet_name='150 Authors Geography with Birthplace included 1')

    # Iterate through rows and columns
     for index, row in df.iterrows():
        for column, value in row.items():
            print(f'Row {index}, Column {column}: {value}')

except FileNotFoundError:
    print(f"File not found: {excel_file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
'''#data frame 
df= ps.read_excel(excel_file_path)

print(df.head())
#temporary end of program '''
