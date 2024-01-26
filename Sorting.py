import csv

def sort_csv(file_path, column, ascending=True):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    data.sort(key=lambda row: row[column], reverse=not ascending)
    return data

# Prompt the user for the file path
#change the file path to the AL Authors csv
file_path = 'ALL Author Geography Metadata.csv'

# Prompt the user for the column to sort by
column = 'County'
# want it to specifically be the county column

# Prompt the user for the sorting order
order = input("Enter the sorting order (asc/desc): ")
order = order.lower()
# Convert the sorting order to a boolean value
ascending = True if order.lower() == 'asc' else False
descending = False if order.lower() == 'desc' else True

#A place to put the First Name and Last Name column to return such, for ex. HENRY AARON 
column_name = 'Author_First_Name_Last_Name'
# making the list of the couunty associations 
# all 67 counties in Alabama 
county_list = [ [
        'Autauga',
        'Baldwin',
        'Barbour',
        'Bibb ',
        'Blount',
        'Bullock',
        'Butler',
        'Calhoun',
        'Chambers',
        'Cherokee',
        'Chilton',
        'Choctaw',
        'Clarke',
        'Clay',
        'Cleburne',
        'Coffee',
        'Colbert',
        'Conecuh',
        'Coosa',
        'Covington',
        'Crenshaw',
        'Cullman',
        'Dale',
        'Dallas',
        'DeKalb',
        'Elmore',
        'Escambia',
        'Etowah',
        'Fayette',
        'Franklin',
        'Geneva',
        'Greene',
        'Hale',
        'Henry',
        'Houston',
        'Jackson',
        'Jefferson',
        'Lamar',
        'Lauderdale',
        'Lawrence',
        'Lee',
        'Limestone',
        'Lowndes',
        'Macon',
        'Madison',
        'Marengo',
        'Marion',
        'Marshall',
        'Mobile',
        'Monroe',
        'Montgomery',
        'Morgan',
        'Perry',
        'Pickens',
        'Pike',
        'Randolph',
        'Russell',
        'St. Clair',
        'Shelby',
        'Sumter',
        'Talladega',
        'Tallapoosa',
        'Tuscaloosa',
        'Walker',
        'Washington',
        'Wilcox',
        'Winston'
    ]
] # REMEMBER THIS IS COLUMN 7 IN THE CSV FILE , "COUNTY"
# this will be helpful for the 400+ authors on the list, but for the other amount, we will likely need something to sort out the html text
# Sort the CSV file
#COLUMN 3 is the column for 'Author_First_Name_Last_Name'
sorted_data = sort_csv(file_path, column,column_name, ascending)
file_path = 'ALL Author Geography Metadata.csv'
column = 'County'
column_name = 'Author_First_Name_Last_Name'
order = 'asc'
# Print the sorted data
for row in sorted_data:
    print(row)
