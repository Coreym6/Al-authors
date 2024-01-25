import csv

def sort_csv(file_path, column, ascending=True):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    data.sort(key=lambda row: row[column], reverse=not ascending)
    return data

# Prompt the user for the file path
file_path = input("Enter the file path: ")

# Prompt the user for the column to sort by
column = input("Enter the column to sort by: ")

# Prompt the user for the sorting order
order = input("Enter the sorting order (asc/desc): ")

# Convert the sorting order to a boolean value
ascending = True if order.lower() == 'asc' else False

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
]

# Sort the CSV file
sorted_data = sort_csv(file_path, column, ascending)
file_path = 'ALL Author Geography Metadata.csv'
column = 'County'
order = 'asc'
# Print the sorted data
for row in sorted_data:
    print(row)
