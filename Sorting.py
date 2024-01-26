import csv

def sort_csv(file_path, column, column_name, ascending=True):
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


# Print the sorted data
for row in sorted_data:
    print(row)

# Approach 1: So there's really one of two ways we can do this; I can make it so the User can ask which county they want to search and then it will return the authors in that county based on the csv file
# or I can make it so the user can search for a specific author and it will return the county that author is from( this can be in tandem with the line above)
#Approach 2: I could just have it return all AUTHOR associations with All Counties County; displaying a list with the Authors and their respective counties
# PSUEDOCODE:  
# need to remove Unicode; https://www.pythonpool.com/remove-unicode-characters-python/#:~:text=Explanation%3A%201%20Firstly%2C%20we%20will%20take%20an%20input,output%20string%20with%20all%20the%20removed%20Unicode%20characters.