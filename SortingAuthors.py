# program name: Sorting Authors.py
import csv

def sort_csv(csv_file,sort_column,sorted_data, Columns_to_print):

    with open(csv_file,'r') as csvfile:
        csv_data = list(csv.DictReader(csvfile))
        sorted_data = sorted(csv_data, key=lambda row: row[sort_column])
        for row in sorted_data:         #for loop location that gives the output 
            output_row = {column: row[column] for column in Columns_to_print}
            print(output_row)
# call back to the function right here 
csv_file = '150 Author Geodata.csv'
sorted_data = 'Lastname'
Columns_to_print = ['Lastname','Firstname','Birthplace','Other Cities','County','education','adult residence','place of burial', 'Lifespan', 'Colors']

#sort_csv(csv_file, sort_column, Columns_to_print)
sort_csv(csv_file,sort_column,sorted_data, Columns_to_print)