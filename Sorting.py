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
county_list = [
    'Autauga County',
    'Baldwin County',
    'Barbour County',
    'Bibb County',
    'Blount County',
    'Bullock County',
    'Butler County',
    'Calhoun County',
    'Chambers County',
    'Cherokee County',
    'Chilton County',
    'Choctaw County',
    'Clarke County',
    'Clay County',
    'Cleburne County',
    'Coffee County',
    'Colbert County',
    'Conecuh County',
    'Coosa County',
    'Covington County',
    'Crenshaw County',
    'Cullman County',
    'Dale County',
    'Dallas County',
    'DeKalb County',
    'Elmore County',
    'Escambia County',
    'Etowah County',
    'Fayette County',
    'Franklin County',
    'Geneva County',
    'Greene County',
    'Hale County',
    'Henry County',
    'Houston County',
    'Jackson County',
    'Jefferson County',
    'Lamar County',
    'Lauderdale County',
    'Lawrence County',
    'Lee County',
    'Limestone County',
    'Lowndes County',
    'Macon County',
    'Madison County',
    'Marengo County',
    'Marion County',
    'Marshall County',
    'Mobile County',
    'Monroe County',
    'Montgomery County',
    'Morgan County',
    'Perry County',
    'Pickens County',
    'Pike County',
    'Randolph County',
    'Russell County',
    'St. Clair County',
    'Shelby County',
    'Sumter County',
    'Talladega County',
    'Tallapoosa County',
    'Tuscaloosa County',
    'Walker County',
    'Washington County',
    'Wilcox County',
    'Winston County'
    
]

# Sort the CSV file
sorted_data = sort_csv(file_path, column, ascending)
file_path = 'ALL Author Geography Metadata.csv'
column = 'County'
order = 'asc'
# Print the sorted data
for row in sorted_data:
    print(row)
