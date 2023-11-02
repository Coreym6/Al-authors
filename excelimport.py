#import pandas as ps 
import openpyxl 
''' #added the path for the 150 author geographical data as an test '''
excel_file_path = '150 Authors Geography with Birthplace included.xlsx'
try:
     workbook = openpyxl.load_workbook(excel_file_path)
 # Select a specific sheet (replace 'Sheet1' with your sheet name)
     sheet = workbook['Sheet_authors']

    # Iterate through rows and columns
     for row in sheet.iter_rows():
            for cell in row:
                print(cell.value)  # Access the cell value

except FileNotFoundError:
    print(f"File not found: {excel_file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
'''#data frame 
df= ps.read_excel(excel_file_path)

print(df.head())
#temporary end of program '''
